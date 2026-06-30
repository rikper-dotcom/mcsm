"""User management helper functions."""

from __future__ import annotations

import pwd

from mcsm.config import (
    MINECRAFT_DIRECTORY,
    MINECRAFT_USER,
)
from mcsm.services.command import run_command


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

    result = run_command(
        "useradd",
        "--system",
        "--home",
        str(MINECRAFT_DIRECTORY),
        "--shell",
        "/usr/sbin/nologin",
        MINECRAFT_USER,
    )

    return result.returncode == 0