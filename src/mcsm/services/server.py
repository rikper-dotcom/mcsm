"""Minecraft server service."""

from __future__ import annotations

import subprocess

from mcsm.config import SERVICE_NAME, SYSTEMCTL
from mcsm.models.server import ServerResult


def start_server() -> ServerResult:
    """Start the Minecraft server."""

    result = subprocess.run(
        [SYSTEMCTL, "start", SERVICE_NAME],
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode == 0:
        return ServerResult(
            success=True,
            message="Server started.",
        )

    return ServerResult(
        success=False,
        message="Failed to start server.",
    )