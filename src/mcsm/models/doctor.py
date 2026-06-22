"""Doctor data model."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class DoctorResult:
    """Result returned by the doctor service."""

    python_version: str

    java_version: str | None

    git_version: str | None

    systemctl: bool

    minecraft_service: bool

    minecraft_running: bool

    server_directory: bool

    paper_jar: bool

    @property
    def ok(self) -> bool:
        """Return True if every check passed."""

        return all(
            (
                self.java_version is not None,
                self.git_version is not None,
                self.systemctl,
                self.minecraft_service,
                self.minecraft_running,
                self.server_directory,
                self.paper_jar,
            )
        )