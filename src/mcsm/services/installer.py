"""Minecraft installer service."""

from __future__ import annotations

from mcsm.models.installer import InstallResult, InstallStep
from mcsm.services.system import has_java


def install() -> InstallResult:
    """Install Minecraft server prerequisites."""

    result = InstallResult(success=True)

    if has_java():
        result.steps.append(
            InstallStep(
                success=True,
                message="Java detected.",
            )
        )
    else:
        result.steps.append(
            InstallStep(
                success=False,
                message="Java not found.",
            )
        )
        result.success = False

    result.steps.append(
        InstallStep(
            success=False,
            message="Installation is not implemented yet.",
        )
    )

    result.success = False

    return result