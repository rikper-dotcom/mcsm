"""Download helper functions."""

from __future__ import annotations

from pathlib import Path
from urllib.error import HTTPError, URLError

from mcsm.services.http import open_url


def download_file(
    url: str,
    destination: Path,
) -> bool:
    """Download a file."""

    try:
        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open_url(url) as response:
            destination.write_bytes(response.read())

        return True

    except (
        HTTPError,
        URLError,
        OSError,
    ):
        return False