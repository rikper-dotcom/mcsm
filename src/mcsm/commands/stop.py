"""Stop command."""

from __future__ import annotations

import typer

from mcsm.commands.helpers import run_server_command
from mcsm.services.server import stop_server

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main() -> None:
    """Stop the Minecraft server."""

    run_server_command(
        "Minecraft Stop",
        stop_server,
    )