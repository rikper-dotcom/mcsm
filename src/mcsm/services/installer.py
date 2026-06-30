"""Minecraft installer service."""

from __future__ import annotations

from collections.abc import Callable

from mcsm.models.installer import InstallResult, InstallStep
from mcsm.services.system import (
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
) -> None:
    """Run a check and append the result."""

    success = check()

    result.steps.append(
        InstallStep(
            success=success,
            message=success_message if success else failure_message,
        )
    )


def _verify_prerequisites(result: InstallResult) -> None:
    """Verify that all installation prerequisites are met."""

    add_check(
        result,
        has_java,
        "Java detected.",
        "Java not found.",
    )

    add_check(
        result,
        has_systemctl,
        "systemd detected.",
        "systemd not found.",
    )

    add_check(
        result,
        server_directory_exists,
        "Server directory exists.",
        "Server directory not found.",
    )

    add_check(
        result,
        paper_jar_exists,
        "Paper server found.",
        "Paper server not found.",
    )


def install() -> InstallResult:
    """Verify Minecraft server prerequisites."""

    result = InstallResult(success=True)

    _verify_prerequisites(result)

    result.steps.append(
        InstallStep(
            success=False,
            message="Installation is not implemented yet.",
        )
    )

    result.success = all(step.success for step in result.steps)

    return result