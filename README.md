# CodeRifts — Minimal Python Example

Minimal Python script that calls the CodeRifts public preflight endpoint and aborts execution when the API is unsafe.

## Quick Start

```bash
pip install requests
python main.py
```

## How It Works

1. Calls `GET /api/v1/public/preflight?url=<spec_url>` — no API key required
2. Reads the `decision` field from the response
3. If `BLOCK` → aborts the workflow
4. If `PENDING` → retries after 5 seconds
5. If `ALLOW` → proceeds with the API call

## Example Output

```
[CODERIFTS] decision: ALLOW
[CODERIFTS] risk_score: 12
[CODERIFTS] safe_for_agent: true
[EXECUTION] Proceeding with API call...
```

## Links

- [CodeRifts Docs](https://coderifts.com)
- [Public Preflight API](https://app.coderifts.com/api/v1/public/preflight?url=https://petstore3.swagger.io/api/v3/openapi.json)
- [Demo Trace](https://app.coderifts.com/api/v1/demo/trace)
