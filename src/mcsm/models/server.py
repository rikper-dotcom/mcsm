"""Models for Minecraft server operations."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ServerResult:
    """Result of a Minecraft server operation."""

    success: bool
    message: str
