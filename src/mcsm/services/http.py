"""HTTP helper functions."""

from __future__ import annotations

from urllib.request import Request, urlopen

from mcsm.config import HTTP_USER_AGENT


def open_url(url: str):
    """Open a URL with the required headers."""

    request = Request(
        url,
        headers={
            "User-Agent": HTTP_USER_AGENT,
        },
    )

    return urlopen(request)