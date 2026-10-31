"""OIC Listo CLI entry point."""

import typer
from rich.console import Console

from oic_listo import __version__
from oic_listo.commands import config, integrations, login

app = typer.Typer(
    name="oic-listo",
    help="🌮 OIC Listo – securely list Oracle OIC Gen3 Integrations",
    add_completion=False,
    no_args_is_help=True,
)
console = Console()

# Register sub-commands
app.add_typer(login.app, name="login", help="Authenticate / manage local session")
app.add_typer(config.app, name="config", help="Configure OIC instance & credentials")
app.add_typer(integrations.app, name="integrations", help="List / inspect integrations")


@app.callback()
def main(
    version: bool = typer.Option(
        False, "--version", "-V", help="Show version and exit"
    ),
) -> None:
    """OIC Listo – the secure multi-platform OIC companion."""
    if version:
        console.print(f"[bold green]oic-listo[/] version {__version__}")
        raise typer.Exit()


if __name__ == "__main__":
    app()
