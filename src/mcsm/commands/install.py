"""Install command."""

from __future__ import annotations

import typer

from mcsm.console import console
from mcsm.services.installer import install

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main() -> None:
    """Install Minecraft server."""

    result = install()

    console.print()
    console.print("[bold cyan]Minecraft Installation[/bold cyan]")
    console.rule()

    for step in result.steps:
        if step.success:
            console.print(f"[green]✓[/green] {step.message}")
        else:
            console.print(f"[red]✗[/red] {step.message}")

    console.rule()

    if result.success:
        console.print("[bold green]Installation completed successfully.[/bold green]")
    else:
        console.print("[bold red]Installation failed.[/bold red]")

    console.print()