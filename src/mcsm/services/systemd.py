"""systemd helper functions."""

from __future__ import annotations

from importlib import resources

from mcsm.config import (
    DEFAULT_MAX_MEMORY,
    DEFAULT_MIN_MEMORY,
    JAVA_EXECUTABLE,
    MINECRAFT_GROUP,
    MINECRAFT_USER,
    SERVER_DIRECTORY,
    SERVICE_FILE,
    SYSTEMCTL,
)
from mcsm.services.command import run_command


def run_systemctl(
    command: str,
    service: str,
):
    """Run a systemctl command."""

    return run_command(
        SYSTEMCTL,
        command,
        service,
    )


def systemd_error_message(stderr: str) -> str:
    """Return a user-friendly systemd error message."""

    stderr = stderr.lower()

    if "interactive authentication required" in stderr:
        return "Administrator privileges are required."

    if "unit" in stderr and "not found" in stderr:
        return "Minecraft service is not installed."

    if "permission denied" in stderr:
        return "Permission denied."

    return "systemctl command failed."


def render_service_template() -> str:
    """Render the minecraft.service template."""

    template = (
        resources.files("mcsm.templates")
        .joinpath("minecraft.service")
        .read_text()
    )

    values = {
        "{{USER}}": MINECRAFT_USER,
        "{{GROUP}}": MINECRAFT_GROUP,
        "{{SERVER_DIRECTORY}}": str(SERVER_DIRECTORY),
        "{{JAVA_EXECUTABLE}}": JAVA_EXECUTABLE,
        "{{MIN_MEMORY}}": DEFAULT_MIN_MEMORY,
        "{{MAX_MEMORY}}": DEFAULT_MAX_MEMORY,
    }

    for key, value in values.items():
        template = template.replace(key, value)

    return template


def create_minecraft_service() -> bool:
    """Create the minecraft.service file."""

    try:
        SERVICE_FILE.write_text(
            render_service_template(),
        )
        return True

    except OSError:
        return False