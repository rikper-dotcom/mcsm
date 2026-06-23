"""Minecraft server service."""

from __future__ import annotations

from mcsm.config import SERVICE_NAME
from mcsm.models.server import ServerResult
from mcsm.services.systemd import run_systemctl


def start_server() -> ServerResult:
    """Start the Minecraft server."""

    result = run_systemctl("start", SERVICE_NAME)

    if result.success:
        return ServerResult(
            success=True,
            message="Server started.",
        )

    return ServerResult(
        success=False,
        message="Failed to start server.",
    )