"""Doctor service."""

from __future__ import annotations

from mcsm.models.doctor import DoctorResult
from mcsm.services.system import (
    git_version,
    has_minecraft_service,
    has_systemctl,
    java_version,
    minecraft_service_running,
    paper_jar_exists,
    python_version,
    server_directory_exists,
)


def doctor() -> DoctorResult:
    """Run basic system diagnostics."""

    return DoctorResult(
        python_version=python_version(),
        java_version=java_version(),
        git_version=git_version(),
        systemctl=has_systemctl(),
        minecraft_service=has_minecraft_service(),
        minecraft_running=minecraft_service_running(),
        server_directory=server_directory_exists(),
        paper_jar=paper_jar_exists(),
    )