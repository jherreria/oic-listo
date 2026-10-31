# Oracle OIC Gen3 – Integration List API Notes

## Endpoint

```
GET {base-url}/ic/api/integration/v1/integrations
```

### Typical Gen3 base URL examples
- Design-time: `https://design.integration.{region}.ocp.oraclecloud.com`
- Runtime: `https://{instance}.integration.{region}.ocp.oraclecloud.com`

### Important query parameter (Gen3)
```
?integrationInstance={service-instance-name}
```
You can find the service instance name on the OIC “About” page.

## Authentication

**Only OAuth 2.0 Bearer tokens** are accepted for the Integration REST APIs in Gen3.  
Basic Auth is rejected.

Header:
```
Authorization: Bearer {access_token}
Accept: application/json
```

## Useful query parameters

| Param     | Description                          | Example                  |
|-----------|--------------------------------------|--------------------------|
| `q`       | Filter (name, status, style…)        | `q={status: 'ACTIVATED'}`|
| `orderBy` | `name` or `time`                     | `orderBy=name`           |
| `limit`   | Page size                            | `limit=50`               |
| `offset`  | Pagination offset                    | `offset=0`               |
| `expand`  | `connection` for extra details       | `expand=connection`      |

## Token acquisition (we will implement)

We will start with **Resource Owner Password** grant because it is the closest mental model to the old username/password:

```
POST {idcs}/oauth2/v1/token
Content-Type: application/x-www-form-urlencoded

grant_type=password
&username=...
&password=...
&client_id=...
&client_secret=...
&scope=https://{oic-instance}/ic/api/ offline_access
```

Later we can add Client Credentials and full Authorization Code + PKCE.
