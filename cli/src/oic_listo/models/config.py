"""Configuration models – what we store about the OIC instance."""

from pydantic import BaseModel, Field, HttpUrl


class OICConfig(BaseModel):
    """Non-secret configuration that can live in a normal file or env."""

    base_url: HttpUrl = Field(..., description="OIC design-time or runtime base URL")
    integration_instance: str = Field(
        ..., description="Service instance name (required for many Gen3 calls)"
    )
    # OAuth related (non-secret parts)
    token_url: HttpUrl | None = Field(
        None, description="IDCS / OAuth token endpoint"
    )
    client_id: str | None = Field(None, description="OAuth client id (not secret)")
    scope: str = Field(
        default="offline_access",
        description="OAuth scopes requested",
    )


class OICCredentials(BaseModel):
    """Secrets that MUST live only in the OS keyring."""

    client_secret: str | None = None
    username: str | None = None
    password: str | None = None
    # We will also store access_token / refresh_token here later
