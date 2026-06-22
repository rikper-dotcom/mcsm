from __future__ import annotations

from mcsm.services.system import (
    has_git,
    has_java,
    has_minecraft_service,
    has_systemctl,
    minecraft_service_running,
    python_version,
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
    }