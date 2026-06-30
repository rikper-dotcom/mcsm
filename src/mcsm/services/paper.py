"""PaperMC helper functions."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.request import urlopen

from mcsm.services.download import download_file

PAPER_API = "https://api.papermc.io/v2/projects/paper"


def latest_version() -> str:
    """Return the latest Paper version."""

    with urlopen(PAPER_API) as response:
        data = json.load(response)

    return data["versions"][-1]


def latest_build() -> int:
    """Return the latest Paper build number."""

    version = latest_version()

    with urlopen(f"{PAPER_API}/versions/{version}") as response:
        data = json.load(response)

    return data["builds"][-1]


def latest_download_url() -> str:
    """Return the latest Paper download URL."""

    version = latest_version()
    build = latest_build()

    return (
        f"{PAPER_API}/versions/{version}"
        f"/builds/{build}"
        f"/downloads/paper-{version}-{build}.jar"
    )


def download_latest_paper(destination: Path) -> bool:
    """Download the latest Paper server."""

    return download_file(
        latest_download_url(),
        destination,
    )