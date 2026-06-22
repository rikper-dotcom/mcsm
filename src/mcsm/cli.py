import platform

import typer

from mcsm.console import console
from mcsm.version import VERSION

app = typer.Typer(
    no_args_is_help=True,
    help="Minecraft Server Manager",
)


@app.callback()
def main() -> None:
    """Minecraft Server Manager."""


@app.command()
def version() -> None:
    """Show version information."""

    console.print()
    console.print("[bold green]Minecraft Server Manager[/bold green]")
    console.print(f"Version : [cyan]{VERSION}[/cyan]")
    console.print(f"Python  : [yellow]{platform.python_version()}[/yellow]")
    console.print(f"System  : [magenta]{platform.system()}[/magenta]")
    console.print()