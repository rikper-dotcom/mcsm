"""System related helper functions."""

from __future__ import annotations

import platform
import shutil
import subprocess

from mcsm.config import PAPER_JAR, SERVER_DIRECTORY, SERVICE_NAME


def python_version() -> str:
    """Return the installed Python version."""
    return platform.python_version()


def java_version() -> str | None:
    """Return the installed Java version."""

    java = shutil.which("java")

    if java is None:
        return None

    result = subprocess.run(
        [java, "-version"],
        capture_output=True,
        text=True,
        check=False,
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

    result = subprocess.run(
        [git, "--version"],
        capture_output=True,
        text=True,
        check=False,
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
    return shutil.which("systemctl") is not None


def has_minecraft_service() -> bool:
    """Return True if the Minecraft systemd service exists."""

    result = subprocess.run(
        ["systemctl", "list-unit-files", f"{SERVICE_NAME}.service"],
        capture_output=True,
        text=True,
        check=False,
    )

    return f"{SERVICE_NAME}.service" in result.stdout


def minecraft_service_running() -> bool:
    """Return True if the Minecraft service is running."""

    result = subprocess.run(
        ["systemctl", "is-active", SERVICE_NAME],
        capture_output=True,
        text=True,
        check=False,
    )

    return result.stdout.strip() == "active"


def server_directory_exists() -> bool:
    """Return True if the server directory exists."""
    return SERVER_DIRECTORY.exists()


def paper_jar_exists() -> bool:
    """Return True if paper.jar exists."""
    return PAPER_JAR.exists()