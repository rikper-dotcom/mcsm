"""Minecraft server service."""

from __future__ import annotations

from mcsm.config import SERVICE_NAME
from mcsm.models.server import ServerResult
from mcsm.services.systemd import (
    run_systemctl,
    systemd_error_message,
)


def _run_server_command(
    command: str,
    success_message: str,
) -> ServerResult:
    """Run a Minecraft server command."""

    result = run_systemctl(command, SERVICE_NAME)

    if result.success:
        return ServerResult(
            success=True,
            message=success_message,
        )

    return ServerResult(
        success=False,
        message=systemd_error_message(result.stderr),
    )


def start_server() -> ServerResult:
    """Start the Minecraft server."""

    return _run_server_command(
        "start",
        "Server started.",
    )


def stop_server() -> ServerResult:
    """Stop the Minecraft server."""

    return _run_server_command(
        "stop",
        "Server stopped.",
    )


def restart_server() -> ServerResult:
    """Restart the Minecraft server."""

    return _run_server_command(
        "restart",
        "Server restarted.",
    )