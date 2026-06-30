"""Download helper functions."""

from __future__ import annotations

from pathlib import Path
from urllib.error import URLError
from urllib.request import urlretrieve


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

        urlretrieve(
            url,
            destination,
        )

        return True

    except URLError:
        return False