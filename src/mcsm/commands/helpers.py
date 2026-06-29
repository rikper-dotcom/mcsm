"""Command helper functions."""

from __future__ import annotations

from collections.abc import Callable

from mcsm.console import console
from mcsm.models.server import ServerResult


def run_server_command(
    title: str,
    command: Callable[[], ServerResult],
) -> None:
    """Run a server command and display the result."""

    result = command()

    console.print()
    console.print(f"[bold cyan]{title}[/bold cyan]")
    console.rule()

    if result.success:
        console.print(f"[green]✓[/green] {result.message}")
    else:
        console.print(f"[red]✗[/red] {result.message}")

    console.rule()
    console.print()