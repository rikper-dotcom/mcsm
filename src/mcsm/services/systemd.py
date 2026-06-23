"""Systemd service helpers."""

from __future__ import annotations

import subprocess

from mcsm.config import SYSTEMCTL
from mcsm.models.systemd import SystemdResult


def run_systemctl(*args: str) -> SystemdResult:
    """Run a systemctl command."""

    result = subprocess.run(
        [SYSTEMCTL, *args],
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