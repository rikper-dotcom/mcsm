"""Main command line interface for MCSM."""

from __future__ import annotations

import platform

import typer

from mcsm.__about__ import __version__
from mcsm.commands.doctor import app as doctor_app
from mcsm.commands.install import app as install_app
from mcsm.commands.status import app as status_app
from mcsm.console import console

app = typer.Typer(
    no_args_is_help=True,
    help="Minecraft Server Manager",
)

app.add_typer(
    doctor_app,
    name="doctor",
)

app.add_typer(
    install_app,
    name="install",
)

app.add_typer(
    status_app,
    name="status",
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