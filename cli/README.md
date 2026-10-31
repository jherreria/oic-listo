# OIC Listo – Python CLI

Secure command-line client for listing Oracle OIC Gen3 Integrations.

## Quick start (once implemented)

```bash
cd cli
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -e .

oic-listo --help
oic-listo config set
oic-listo integrations list
```

## Security highlights (learning goals)

- Secrets stored via the OS keyring (`keyring` library)
- No secrets in git, env files committed to the repo, or plain text
- Tokens never logged
- HTTPS only
