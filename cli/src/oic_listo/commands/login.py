"""Login / session commands."""

import typer
from rich.console import Console

app = typer.Typer(help="Manage local authentication session")
console = Console()


@app.command("status")
def status() -> None:
    """Show current login status."""
    console.print("[yellow]🚧 Not implemented yet – coming in the next taco[/]")


@app.command("logout")
def logout() -> None:
    """Clear local session and tokens."""
    console.print("[yellow]🚧 Not implemented yet – coming in the next taco[/]")
