"""Tests for system services."""

from __future__ import annotations

from mcsm.services.system import (
    git_version,
    python_version,
)


def test_python_version_returns_string() -> None:
    """python_version() should return a non-empty string."""

    version = python_version()

    assert isinstance(version, str)
    assert version


def test_git_version_returns_string() -> None:
    """git_version() should return the installed Git version."""

    version = git_version()

    assert isinstance(version, str)
    assert version
    assert "git" in version.lower()