"""Models for systemd operations."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SystemdResult:
    """Result from a systemctl command."""

    success: bool
    returncode: int
    stdout: str
    stderr: str
