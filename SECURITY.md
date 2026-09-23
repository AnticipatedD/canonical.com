# Security Policy & Threat Model

## Reporting Vulnerabilities
If you discover a security vulnerability within this repository, please contact the maintainers directly rather than opening a public issue. All vulnerability reports will be reviewed promptly.

## Secret Management & Provisioning
Sensitive operational keys and credentials (such as `MARKETO_API_SECRET`, `SENTRY_DSN`, `DIRECTORY_API_TOKEN`, and `SERVICE_ACCOUNT_PRIVATE_KEY`) are strictly managed:
- **Environment Injection**: Provisioned securely via GitHub Actions secrets and runtime environment variables.
- **Version Control Exclusion**: Secrets are never hardcoded or committed to the repository (local development relies on `.env` which is excluded via `.gitignore`).

## Threat Model & Trust Boundaries
- **Environment Variables & Secrets**: Operational keys are isolated to secure environment stores and injected only at runtime.
- **Public Website Endpoints**: Publicly accessible routes are strictly read-only or validate input payload structures securely.
- **Third-Party Integrations**: Integrations with external APIs (Greenhouse and Marketo) utilize authenticated API clients with explicit token-based authorization.
- **Application Proxy**: The `/careers/application` proxy endpoint in `webapp/application.py` sanitizes and validates incoming form payloads before forwarding requests to upstream ATS services.
