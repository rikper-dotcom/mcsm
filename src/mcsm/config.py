"""
Global configuration for MCSM.

All paths and service names should be defined here.
"""

from pathlib import Path

# ---------------------------------------------------------------------
# Minecraft
# ---------------------------------------------------------------------

SERVICE_NAME = "minecraft"

SYSTEMCTL = "systemctl"

SERVER_DIRECTORY = Path("/srv/minecraft/server")

PAPER_JAR = SERVER_DIRECTORY / "paper.jar"

WORLD_DIRECTORY = SERVER_DIRECTORY / "world"

BACKUP_DIRECTORY = Path("/srv/minecraft/backups")

DOWNLOAD_DIRECTORY = Path("/srv/minecraft/downloads")

# ---------------------------------------------------------------------
# systemd
# ---------------------------------------------------------------------

SYSTEMD_DIRECTORY = Path("/etc/systemd/system")

SERVICE_FILE = SYSTEMD_DIRECTORY / f"{SERVICE_NAME}.service"

# ---------------------------------------------------------------------
# Java
# ---------------------------------------------------------------------

JAVA_EXECUTABLE = "/usr/bin/java"

# ---------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------

MINECRAFT_USER = "minecraft"

MINECRAFT_GROUP = "minecraft"

# ---------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------

DEFAULT_MIN_MEMORY = "2G"

DEFAULT_MAX_MEMORY = "2G"