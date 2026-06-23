"""Models for installation operations."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class InstallStep:
    """Represents a single installation step."""

    success: bool
    message: str


@dataclass(slots=True)
class InstallResult:
    """Result of an installation operation."""

    success: bool
    steps: list[InstallStep] = field(default_factory=list)