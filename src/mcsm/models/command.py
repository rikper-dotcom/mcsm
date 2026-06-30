"""Command result model."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CommandResult:
    """Result from a system command."""

    returncode: int
    stdout: str
    stderr: str

    @property
    def success(self) -> bool:
        """Return True if the command completed successfully."""
        return self.returncode == 0

    @property
    def failed(self) -> bool:
        """Return True if the command failed."""
        return not self.success