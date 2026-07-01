"""Minecraft installer service."""

from __future__ import annotations

from collections.abc import Callable

from mcsm.config import PAPER_JAR
from mcsm.models.installer import InstallResult, InstallStep
from mcsm.services.filesystem import create_minecraft_directories
from mcsm.services.paper import download_latest_paper
from mcsm.services.system import (
    has_java,
    has_systemctl,
    is_root,
    paper_jar_exists,
    server_directory_exists,
)
from mcsm.services.systemd import create_minecraft_service
from mcsm.services.users import create_minecraft_user


def add_check(
    result: InstallResult,
    check: Callable[[], bool],
    success_message: str,
    failure_message: str,
) -> bool:
    """Run a check, append the result and return the outcome."""

    success = check()

    result.steps.append(
        InstallStep(
            success=success,
            message=success_message if success else failure_message,
        )
    )

    return success


def _verify_prerequisites(result: InstallResult) -> bool:
    """Verify installation prerequisites."""

    success = True

    success &= add_check(
        result,
        has_java,
        "Java detected.",
        "Java not found.",
    )

    success &= add_check(
        result,
        has_systemctl,
        "systemd detected.",
        "systemd not found.",
    )

    success &= add_check(
        result,
        is_root,
        "Running as administrator.",
        "Administrator privileges are required.",
    )

    return success


def _create_user(result: InstallResult) -> bool:
    """Create the minecraft system user."""

    success = create_minecraft_user()

    result.steps.append(
        InstallStep(
            success=success,
            message=(
                "Minecraft user ready."
                if success
                else "Failed to create minecraft user."
            ),
        )
    )

    return success


def _create_directories(result: InstallResult) -> bool:
    """Create the required Minecraft directories."""

    success = create_minecraft_directories()

    result.steps.append(
        InstallStep(
            success=success,
            message=(
                "Minecraft directories ready."
                if success
                else "Failed to create Minecraft directories."
            ),
        )
    )

    return success


def _create_service(result: InstallResult) -> bool:
    """Create the minecraft.service file."""

    success = create_minecraft_service()

    result.steps.append(
        InstallStep(
            success=success,
            message=(
                "minecraft.service created."
                if success
                else "Failed to create minecraft.service."
            ),
        )
    )

    return success


def _install_server(result: InstallResult) -> bool:
    """Install the Minecraft server."""

    success = download_latest_paper(PAPER_JAR)

    result.steps.append(
        InstallStep(
            success=success,
            message=(
                "Paper server downloaded."
                if success
                else "Failed to download Paper server."
            ),
        )
    )

    return success


def _verify_installation(result: InstallResult) -> bool:
    """Verify the completed installation."""

    success = True

    success &= add_check(
        result,
        server_directory_exists,
        "Server directory verified.",
        "Server directory missing.",
    )

    success &= add_check(
        result,
        paper_jar_exists,
        "Paper server verified.",
        "Paper server not found.",
    )

    return success


def install() -> InstallResult:
    """Install the Minecraft server."""

    result = InstallResult(success=True)

    if not _verify_prerequisites(result):
        result.success = False
        return result

    if not _create_user(result):
        result.success = False
        return result

    if not _create_directories(result):
        result.success = False
        return result

    if not _create_service(result):
        result.success = False
        return result

    if not _install_server(result):
        result.success = False
        return result

    result.success = _verify_installation(result)

    return result