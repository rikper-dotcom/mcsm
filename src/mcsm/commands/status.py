"""Status command."""

from __future__ import annotations

import typer

from mcsm.console import console
from mcsm.services.system import minecraft_service_running

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main() -> None:
    """Show Minecraft server status."""

    running = minecraft_service_running()

    console.print()

    if running:
        console.print("[bold green]Minecraft server is running.[/bold green]")
    else:
        console.print("[bold red]Minecraft server is stopped.[/bold red]")

    console.print()