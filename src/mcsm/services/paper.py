"""PaperMC helper functions."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.error import HTTPError, URLError

from mcsm.config import PAPER_API, PAPER_PROJECT
from mcsm.services.download import download_file
from mcsm.services.http import open_url


def latest_download_url() -> str | None:
    """Return the latest stable Paper download URL."""

    try:
        with open_url(f"{PAPER_API}/{PAPER_PROJECT}") as response:
            project = json.load(response)

        for versions in project["versions"].values():
            version = versions[0]

            with open_url(
                f"{PAPER_API}/{PAPER_PROJECT}/versions/{version}/builds"
            ) as response:
                builds = json.load(response)

            stable = next(
                (
                    build
                    for build in builds
                    if build["channel"] == "STABLE"
                ),
                None,
            )

            if stable is not None:
                return stable["downloads"]["server:default"]["url"]

    except (
        HTTPError,
        URLError,
        KeyError,
        ValueError,
        TypeError,
    ):
        return None

    return None


def download_latest_paper(destination: Path) -> bool:
    """Download the latest Paper server."""

    url = latest_download_url()

    if url is None:
        return False

    return download_file(
        url,
        destination,
    )