from __future__ import annotations

import typer

from mcsm.console import console
from mcsm.services.doctor import doctor

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main() -> None:
    """Run system diagnostics."""

    result = doctor()

    console.print()
    console.print("[bold green]MCSM Doctor[/bold green]")
    console.print()

    console.print(
        f"Python              : {'✓' if result['python_version'] else '✗'} {result['python_version']}"
    )
    console.print(
        f"Java                : {'✓' if result['java'] else '✗'}"
    )
    console.print(
        f"Git                 : {'✓' if result['git'] else '✗'}"
    )
    console.print(
        f"systemd             : {'✓' if result['systemctl'] else '✗'}"
    )

    console.print()

    console.print(
        f"Minecraft service   : {'✓' if result['minecraft_service'] else '✗'}"
    )
    console.print(
        f"Service running     : {'✓' if result['minecraft_running'] else '✗'}"
    )

    console.print()