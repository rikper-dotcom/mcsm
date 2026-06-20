import typer

from mcsm.version import VERSION

app = typer.Typer(
    no_args_is_help=True,
    help="Minecraft Server Manager",
)


@app.command()
def version() -> None:
    """Show version information."""
    print(f"Minecraft Server Manager v{VERSION}")


@app.callback()
def main() -> None:
    """Minecraft Server Manager."""