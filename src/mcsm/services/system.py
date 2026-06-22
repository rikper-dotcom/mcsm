from __future__ import annotations

import platform
import shutil
import subprocess


def python_version() -> str:
    """Return the installed Python version."""
    return platform.python_version()


def has_java() -> bool:
    """Return True if Java is installed."""
    return shutil.which("java") is not None


def has_git() -> bool:
    """Return True if Git is installed."""
    return shutil.which("git") is not None


def has_systemctl() -> bool:
    """Return True if systemd is available."""
    return shutil.which("systemctl") is not None


def has_minecraft_service() -> bool:
    """Return True if minecraft.service exists."""

    result = subprocess.run(
        ["systemctl", "list-unit-files", "minecraft.service"],
        capture_output=True,
        text=True,
        check=False,
    )

    return "minecraft.service" in result.stdout


def minecraft_service_running() -> bool:
    """Return True if minecraft.service is running."""

    result = subprocess.run(
        ["systemctl", "is-active", "minecraft"],
        capture_output=True,
        text=True,
        check=False,
    )

    return result.stdout.strip() == "active"
