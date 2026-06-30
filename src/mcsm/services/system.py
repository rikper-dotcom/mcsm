"""System related helper functions."""

from __future__ import annotations

import os
import platform
import shutil

from mcsm.config import PAPER_JAR, SERVER_DIRECTORY, SERVICE_NAME, SYSTEMCTL
from mcsm.services.command import run_command


def python_version() -> str:
    """Return the installed Python version."""
    return platform.python_version()


def java_version() -> str | None:
    """Return the installed Java version."""

    java = shutil.which("java")

    if java is None:
        return None

    result = run_command(
        java,
        "-version",
    )

    output = result.stderr.splitlines()

    if not output:
        return None

    return output[0].replace('"', "")


def git_version() -> str | None:
    """Return the installed Git version."""

    git = shutil.which("git")

    if git is None:
        return None

    result = run_command(
        git,
        "--version",
    )

    output = result.stdout.strip()

    if not output:
        return None

    return output


def has_java() -> bool:
    """Return True if Java is installed."""
    return java_version() is not None


def has_git() -> bool:
    """Return True if Git is installed."""
    return git_version() is not None


def has_systemctl() -> bool:
    """Return True if systemctl is available."""
    return shutil.which(SYSTEMCTL) is not None


def is_root() -> bool:
    """Return True if the current user is root."""
    return os.geteuid() == 0


def has_minecraft_service() -> bool:
    """Return True if the Minecraft systemd service exists."""

    result = run_command(
        SYSTEMCTL,
        "list-unit-files",
        f"{SERVICE_NAME}.service",
    )

    return f"{SERVICE_NAME}.service" in result.stdout


def minecraft_service_running() -> bool:
    """Return True if the Minecraft service is running."""

    result = run_command(
        SYSTEMCTL,
        "is-active",
        SERVICE_NAME,
    )

    return result.stdout.strip() == "active"


def server_directory_exists() -> bool:
    """Return True if the server directory exists."""
    return SERVER_DIRECTORY.exists()


def paper_jar_exists() -> bool:
    """Return True if paper.jar exists."""
    return PAPER_JAR.exists()


def ensure_server_directory() -> bool:
    """Create the server directory if needed."""

    try:
        SERVER_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True,
        )
        return True

    except OSError:
        return False