"""Main command line interface for MCSM."""

from __future__ import annotations

import platform

import typer

from mcsm.__about__ import __version__
from mcsm.commands.doctor import app as doctor_app
from mcsm.commands.install import app as install_app
from mcsm.commands.start import app as start_app
from mcsm.commands.status import app as status_app
from mcsm.console import console
from mcsm.commands.stop import app as stop_app
from mcsm.commands.restart import app as restart_app

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
    start_app,
    name="start",
)

app.add_typer(
    status_app,
    name="status",
)

app.add_typer(
    stop_app,
    name="stop",
)

app.add_typer(
    restart_app,
    name="restart",
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