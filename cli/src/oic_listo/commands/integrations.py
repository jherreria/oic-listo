"""Commands to list and inspect OIC integrations."""

import typer
from rich.console import Console

app = typer.Typer(help="List and inspect Oracle OIC Gen3 Integrations")
console = Console()


@app.command("list")
def list_integrations(
    limit: int = typer.Option(50, help="Max number of integrations to return"),
    status: str | None = typer.Option(None, help="Filter by status (e.g. ACTIVATED)"),
) -> None:
    """List integrations from the configured OIC Gen3 instance."""
    console.print("[yellow]🚧 Not implemented yet – will call /ic/api/integration/v1/integrations[/]")


@app.command("get")
def get_integration(
    integration_id: str = typer.Argument(..., help="Integration ID (code|version)"),
) -> None:
    """Get details of a single integration."""
    console.print(f"[yellow]🚧 Not implemented yet – would fetch {integration_id}[/]")
