import platform

import typer

from mcsm.__about__ import __version__
from mcsm.commands.doctor import app as doctor_app
from mcsm.console import console

app = typer.Typer(
    no_args_is_help=True,
    help="Minecraft Server Manager",
)

app.add_typer(
    doctor_app,
    name="doctor",
)


@app.callback()
def main() -> None:
    """Minecraft Server Manager."""


@app.command()
def version() -> None:
    """Show version information."""

    console.print()
    console.print("[bold green]Minecraft Server Manager[/bold green]")
    console.print(f"Version : [cyan]{__version__}[/cyan]")
    console.print(f"Python  : [yellow]{platform.python_version()}[/yellow]")
    console.print(f"System  : [magenta]{platform.system()}[/magenta]")
    console.print()
