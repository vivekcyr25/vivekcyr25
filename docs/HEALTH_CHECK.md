# Repository Health Check & Diagnostics Guide

The health check utility (`scripts/health_check.py`) performs integrity verification across key assets and configuration files in the repository.

## Checks Performed

1. **Configuration Validation**:
   - Ensures `config.json` is properly structured.
   - Verifies required sections (`profile`, `dashboard`, `animation`, `stats`).

2. **README Assets Verification**:
   - Scans `README.md` for image/asset references matching `./assets/...`.
   - Confirms that every referenced file actually exists in the `assets/` directory.

3. **Workflow Integrity**:
   - Ensures `.github/workflows/` contains active YAML automation workflows.

4. **Script Imports**:
   - Verifies Python modules import cleanly without missing dependencies or syntax errors.

## Running Health Checks

```bash
# Direct execution
python scripts/health_check.py

# Via Makefile
make health-check
```
