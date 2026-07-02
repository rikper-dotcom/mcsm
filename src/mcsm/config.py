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

MINECRAFT_DIRECTORY = Path("/srv/minecraft")

SERVER_DIRECTORY = MINECRAFT_DIRECTORY / "server"

PAPER_JAR = SERVER_DIRECTORY / "paper.jar"

WORLD_DIRECTORY = SERVER_DIRECTORY / "world"

BACKUP_DIRECTORY = MINECRAFT_DIRECTORY / "backups"

DOWNLOAD_DIRECTORY = MINECRAFT_DIRECTORY / "downloads"

# ---------------------------------------------------------------------
# PaperMC
# ---------------------------------------------------------------------

PAPER_PROJECT = "paper"

PAPER_API = "https://fill.papermc.io/v3/projects"

HTTP_USER_AGENT = (
    "mcsm/0.1 "
    "(https://github.com/rikardpersson/mcsm)"
)

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