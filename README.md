# OIC Listo 🌮

Multi-platform app to **securely** list Oracle Integration Cloud (OIC) Gen3 Integrations.

**Platforms**
- **CLI** → Python (Typer + Rich + httpx + keyring)
- **Web** → React + Vite + TypeScript
- **Mobile** → Flutter

**Core features**
1. User login / session
2. Configure OIC Gen3 instance + OAuth credentials
3. Call OIC Gen3 REST API (`GET /ic/api/integration/v1/integrations`)
4. Display the list of integrations

**Security learning focus**
- Credential & token storage (different techniques per platform)
- OAuth 2.0 flows (Client Credentials / Resource Owner Password / Authorization Code)
- Secure transport, least privilege, secret handling
- Never hard-code secrets, never log tokens

¡Sí, está listo!

## Project structure

```
oic-listo/
├── cli/                     # Python CLI
│   ├── pyproject.toml
│   ├── src/oic_listo/
│   │   ├── main.py
│   │   ├── commands/        # login, config, integrations
│   │   ├── services/        # secure_store, oic_client (soon)
│   │   ├── models/
│   │   └── utils/
│   └── README.md
├── web/                     # React + Vite + TS (already npm installed)
│   ├── src/
│   ├── package.json
│   └── ...
├── mobile/                  # Flutter skeleton
│   ├── lib/
│   ├── pubspec.yaml
│   └── README.md
├── docs/
│   ├── architecture.md
│   └── oic-api-notes.md
├── .gitignore
└── README.md
```

## Quick status

- [x] Repo created
- [x] Stack chosen: Python / React / Flutter
- [x] High-level architecture & security design
- [x] CLI scaffold (commands + secure_store ready)
- [x] Web scaffold (Vite React-TS)
- [x] Mobile scaffold (basic Flutter structure)
- [ ] Implement OAuth + list integrations (CLI first)
