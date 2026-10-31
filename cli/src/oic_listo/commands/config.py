"""Configuration commands – OIC instance + credentials."""

import typer
from rich.console import Console

app = typer.Typer(help="Configure OIC instance and OAuth credentials")
console = Console()


@app.command("set")
def set_config() -> None:
    """Interactively set OIC base URL, instance name and OAuth credentials."""
    console.print("[yellow]🚧 Not implemented yet – secrets will go into the OS keyring[/]")


@app.command("show")
def show_config() -> None:
    """Show current configuration (secrets redacted)."""
    console.print("[yellow]🚧 Not implemented yet[/]")


@app.command("clear")
def clear_config() -> None:
    """Remove stored OIC credentials from the keyring."""
    console.print("[yellow]🚧 Not implemented yet[/]")
