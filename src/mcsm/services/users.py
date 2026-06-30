"""User management helper functions."""

from __future__ import annotations

import pwd
import subprocess

from mcsm.config import (
    MINECRAFT_DIRECTORY,
    MINECRAFT_USER,
)


def minecraft_user_exists() -> bool:
    """Return True if the minecraft user exists."""

    try:
        pwd.getpwnam(MINECRAFT_USER)
        return True

    except KeyError:
        return False


def create_minecraft_user() -> bool:
    """Create the minecraft system user."""

    if minecraft_user_exists():
        return True

    result = subprocess.run(
        [
            "useradd",
            "--system",
            "--home",
            str(MINECRAFT_DIRECTORY),
            "--shell",
            "/usr/sbin/nologin",
            MINECRAFT_USER,
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    return result.returncode == 0