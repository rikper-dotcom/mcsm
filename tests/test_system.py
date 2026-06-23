"""Tests for system services."""

from __future__ import annotations

from mcsm.services.system import python_version


def test_python_version_returns_string() -> None:
    """python_version() should return a non-empty string."""

    version = python_version()

    assert isinstance(version, str)
    assert version
