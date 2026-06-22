"""Doctor service."""

from __future__ import annotations

from mcsm.services.system import (
    has_git,
    has_java,
    has_minecraft_service,
    has_systemctl,
    minecraft_service_running,
    paper_jar_exists,
    python_version,
    server_directory_exists,
)


def doctor() -> dict[str, str | bool]:
    """Run basic system diagnostics."""

    return {
        "python_version": python_version(),
        "java": has_java(),
        "git": has_git(),
        "systemctl": has_systemctl(),
        "minecraft_service": has_minecraft_service(),
        "minecraft_running": minecraft_service_running(),
        "server_directory": server_directory_exists(),
        "paper_jar": paper_jar_exists(),
    }