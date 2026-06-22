"""Doctor command."""

from __future__ import annotations

import typer

from mcsm.console import console
from mcsm.services.doctor import doctor

app = typer.Typer()


def status(ok: bool) -> str:
    """Return a colored status symbol."""

    return "[green]✓[/green]" if ok else "[red]✗[/red]"


@app.callback(invoke_without_command=True)
def main() -> None:
    """Run system diagnostics."""

    result = doctor()

    console.print()
    console.print("[bold cyan]MCSM Doctor[/bold cyan]")
    console.rule()

    console.print("[bold]System[/bold]")
    console.print(f"{status(True)} Python              {result.python_version}")
    console.print(f"{status(result.java_version is not None)} Java                {result.java_version or 'Not installed'}")
    console.print(f"{status(result.git_version is not None)} Git                 {result.git_version or 'Not installed'}")
    console.print(f"{status(result.systemctl)} systemd")

    console.print()
    console.print("[bold]Minecraft[/bold]")
    console.print(f"{status(result.minecraft_service)} Service installed")
    console.print(f"{status(result.minecraft_running)} Service running")
    console.print(f"{status(result.server_directory)} Server directory")
    console.print(f"{status(result.paper_jar)} Paper JAR")

    console.rule()

    if result.ok:
        console.print("[bold green]Everything looks good![/bold green]")
    else:
        console.print("[bold red]One or more checks failed.[/bold red]")

    console.print()