"""Systemd service helpers."""

from __future__ import annotations

import subprocess

from mcsm.config import SYSTEMCTL
from mcsm.models.systemd import SystemdResult


def systemd_error_message(stderr: str) -> str:
    """Return a user-friendly systemd error message."""

    stderr = stderr.strip()

    if "Interactive authentication required" in stderr:
        return "Administrator privileges are required."

    if "Access denied" in stderr:
        return "Administrator privileges are required."

    if "Unit" in stderr and "not found" in stderr:
        return "Minecraft service is not installed."

    return stderr or "Unknown systemd error."


def run_systemctl(*args: str) -> SystemdResult:
    """Run a systemctl command."""

    result = subprocess.run(
        [
            SYSTEMCTL,
            "--no-ask-password",
            *args,
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    return SystemdResult(
        success=result.returncode == 0,
        returncode=result.returncode,
        stdout=result.stdout.strip(),
        stderr=result.stderr.strip(),
    )