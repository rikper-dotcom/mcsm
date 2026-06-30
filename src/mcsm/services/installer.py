"""Minecraft installer service."""

from __future__ import annotations

from collections.abc import Callable

from mcsm.config import PAPER_JAR
from mcsm.models.installer import InstallResult, InstallStep
from mcsm.services.paper import download_latest_paper
from mcsm.services.system import (
    ensure_server_directory,
    has_java,
    has_systemctl,
    paper_jar_exists,
    server_directory_exists,
)


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

    return success


def _prepare_system(result: InstallResult) -> bool:
    """Prepare the system for installation."""

    success = ensure_server_directory()

    result.steps.append(
        InstallStep(
            success=success,
            message=(
                "Server directory ready."
                if success
                else "Failed to create server directory."
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

    if not _prepare_system(result):
        result.success = False
        return result

    if not _install_server(result):
        result.success = False
        return result

    result.success = _verify_installation(result)

    return result