"""Command execution helper functions."""

from __future__ import annotations

import subprocess

from mcsm.models.command import CommandResult


def run_command(
    *command: str,
) -> CommandResult:
    """Run a system command."""

    completed = subprocess.run(
        list(command),
        capture_output=True,
        text=True,
        check=False,
    )

    return CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )