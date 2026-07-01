"""Filesystem helper functions."""

from __future__ import annotations

from pathlib import Path

from mcsm.config import (
    BACKUP_DIRECTORY,
    DOWNLOAD_DIRECTORY,
    MINECRAFT_DIRECTORY,
    MINECRAFT_GROUP,
    MINECRAFT_USER,
    SERVER_DIRECTORY,
)
from mcsm.services.command import run_command


def create_directory(path: Path) -> bool:
    """Create a directory if it does not exist."""

    try:
        path.mkdir(
            parents=True,
            exist_ok=True,
        )
        return True

    except OSError:
        return False


def create_minecraft_directories() -> bool:
    """Create all required Minecraft directories."""

    directories = (
        MINECRAFT_DIRECTORY,
        SERVER_DIRECTORY,
        BACKUP_DIRECTORY,
        DOWNLOAD_DIRECTORY,
    )

    for directory in directories:
        if not create_directory(directory):
            return False

    return True


def directory_exists(path: Path) -> bool:
    """Return True if a directory exists."""

    return path.exists() and path.is_dir()


def set_directory_ownership() -> bool:
    """Set ownership of the Minecraft directory."""

    result = run_command(
        "chown",
        "-R",
        f"{MINECRAFT_USER}:{MINECRAFT_GROUP}",
        str(MINECRAFT_DIRECTORY),
    )

    return result.success


def configure_filesystem() -> bool:
    """Configure the Minecraft filesystem."""

    return set_directory_ownership()