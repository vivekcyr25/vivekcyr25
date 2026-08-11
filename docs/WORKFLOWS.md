# GitHub Actions Workflows Reference

This repository includes automated CI/CD pipelines to validate code, test SVG assets, generate status dashboards, and maintain contribution animations.

## Workflow Summary

| Workflow File | Name | Trigger | Description |
|---|---|---|---|
| `tests.yml` | Test Suite | Push, PR | Runs pytest suite across Python 3.10, 3.11, 3.12 |
| `validate-svgs.yml` | Validate SVGs | Push (`assets/*.svg`) | Validates XML formatting & size thresholds for all SVGs |
| `update-stats.yml` | Update Stats | Cron (Daily 00:00 UTC) | Runs `generate_stats.py` and updates profile dashboard |
| `snake.yml` | Snake Grid | Cron (Daily 00:00 UTC) | Renders contribution snake SVG grid |
| `accessibility.yml` | Accessibility Audit | Push (`assets/*.svg`) | Audits accessibility metadata (title, role, aria-label) |

## Running Workflows Locally

You can test workflow scripts locally via Makefile:
```bash
make test          # Runs pytest suite
make validate      # Runs SVG validator
make access-check  # Runs accessibility audit
```
