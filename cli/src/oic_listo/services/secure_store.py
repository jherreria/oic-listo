"""Secure credential storage using the OS keyring.

This is the first place we practice good security:
- Never write secrets to disk in plain text
- Use the platform keychain / credential manager
"""

from __future__ import annotations

import keyring
from keyring.errors import KeyringError

SERVICE_NAME = "oic-listo"


class SecureStore:
    """Thin wrapper around keyring for OIC Listo secrets."""

    def set(self, key: str, value: str) -> None:
        try:
            keyring.set_password(SERVICE_NAME, key, value)
        except KeyringError as exc:
            raise RuntimeError(f"Failed to store secret '{key}': {exc}") from exc

    def get(self, key: str) -> str | None:
        try:
            return keyring.get_password(SERVICE_NAME, key)
        except KeyringError as exc:
            raise RuntimeError(f"Failed to read secret '{key}': {exc}") from exc

    def delete(self, key: str) -> None:
        try:
            keyring.delete_password(SERVICE_NAME, key)
        except KeyringError:
            # Already gone – fine
            pass


# Singleton-style convenience
store = SecureStore()
