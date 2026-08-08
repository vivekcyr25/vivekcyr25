# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Do not** open a public issue
2. Email: viveklpu008@gmail.com
3. Include detailed steps to reproduce
4. Allow up to 48 hours for an initial response

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.1.x   | :white_check_mark: |
| 2.0.x   | :white_check_mark: |
| < 2.0   | :x:                |

## Security Practices

- All API tokens are stored as GitHub Secrets
- No sensitive data is committed to the repository
- GitHub Actions use minimal required permissions
- Dependencies are monitored via Dependabot
- SVG files are validated for XSS-safe content on every PR

## Scope

This policy covers:
- The Python scripts in `scripts/`
- GitHub Actions workflows in `.github/workflows/`
- SVG assets that may embed external references

This policy does **not** cover:
- Third-party badge services (shields.io, etc.)
- The GitHub API itself