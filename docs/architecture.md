# OIC Listo – Architecture & Security Design

## 1. Goal

Build the **same functional app** three times (CLI / Web / Mobile) so we can compare security patterns side-by-side while learning.

## 2. Tech Stack (Option B)

| Platform | Language / Framework | Why |
|----------|----------------------|-----|
| CLI      | Python 3.11+ + Typer + Rich + httpx | Great for learning secrets management (`keyring`, `cryptography`) |
| Web      | React + Vite + TypeScript | Browser security model (CSP, secure storage, OAuth redirects) |
| Mobile   | Flutter + Dart        | Platform keychain / Keystore, biometric options later |

## 3. Core Flow (same on all platforms)

```
┌─────────────┐     1. Login / Session
│   User      │ ──────────────────────────────┐
└─────────────┘                               │
                                              ▼
┌─────────────┐     2. Configure OIC Instance + Credentials
│  Settings   │ ──────────────────────────────┐
└─────────────┘                               │
                                              ▼
┌─────────────┐     3. Obtain OAuth Access Token
│  Auth Layer │ ──────────────────────────────┐
└─────────────┘                               │
                                              ▼
┌─────────────┐     4. GET /ic/api/integration/v1/integrations
│  OIC Client │ ──────────────────────────────┐
└─────────────┘                               │
                                              ▼
┌─────────────┐     5. Display list of Integrations
│     UI      │
└─────────────┘
```

## 4. Oracle OIC Gen3 Reality Check (important)

- Endpoint: `GET {oic-base}/ic/api/integration/v1/integrations`
- Gen3 design-time often requires query param: `?integrationInstance=<service-instance-name>`
- **Basic Auth is NOT supported** for the Integration REST APIs in Gen3.
- We must use **OAuth 2.0 Bearer tokens**.

Recommended grant types we will support (in order of simplicity for learning):

1. **Resource Owner Password Credentials** (closest to old Basic Auth – username + password + client id/secret)
2. **Client Credentials** (machine-to-machine)
3. Later: Authorization Code + PKCE (best for Web & Mobile)

## 5. Security Principles we will enforce everywhere

- Secrets never live in source code or plain config files committed to git
- Tokens stored in the **most secure store available** on each platform
- Access tokens are short-lived; we always prefer refresh tokens when available
- All HTTP calls use HTTPS only
- Never log access tokens, client secrets, or passwords
- Least privilege: the OIC user/app only needs permission to list integrations
- Clear separation between “app login” (local session) and “OIC credentials”

## 6. Platform-specific credential storage strategy

| Platform | Storage Mechanism | Notes |
|----------|-------------------|-------|
| CLI      | `keyring` library (OS keychain) + optional encrypted file fallback | Cross-platform (macOS Keychain, Windows Credential Manager, Linux Secret Service) |
| Web      | Never store long-lived secrets in localStorage. Prefer memory + secure HttpOnly cookies if we add a backend later, or browser Password Manager + sessionStorage for short tokens | For pure SPA we will use sessionStorage + short-lived tokens and document the risks |
| Mobile   | Flutter `flutter_secure_storage` (iOS Keychain / Android Keystore) | Best practice. Can add biometric unlock later |

## 7. Next implementation steps

1. Document the exact OAuth payload we need (this file)
2. Scaffold Python CLI with Typer + secure config
3. Scaffold React app
4. Scaffold Flutter app
5. Implement the OIC client + token handling in each

---

**Mexican security proverb of the day**  
“El que guarda su secreto, guarda su taco.”  
(The one who guards his secret, guards his taco.)
