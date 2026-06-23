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
    console.print("[bold cyan]Minecraft Status[/bold cyan]")
    console.rule()

    if running:
        console.print("[green]✓[/green] Running")
    else:
        console.print("[red]✗[/red] Stopped")

    console.rule()
    console.print()