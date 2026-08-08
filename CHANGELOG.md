# Changelog

All notable changes to the GitHub profile README are documented here.

## [2.1.0] - 2026-08-08

### Added
- SVG optimizer script for size analysis (scripts/svg_optimizer.py)
- Centralized constants module (scripts/constants.py)
- Type hints throughout scripts/utils.py
- Comprehensive test suite (	ests/)
- pytest configuration with shared fixtures (conftest.py)
- Integration tests for all SVG assets
- Code of Conduct (Contributor Covenant v2.1)
- Architecture documentation (ARCHITECTURE.md)
- CI workflow for automated testing (Python 3.10–3.12)
- pyproject.toml for modern Python tooling
- New Makefile targets: 	est, lint, optimize, clean

### Changed
- Expanded .gitignore with venv, testing, and temp patterns
- Improved CONTRIBUTING.md with setup instructions and commit conventions
- Expanded SECURITY.md with version support table and scope
- Bumped version to 2.1.0 across all manifests

## [2.0.0] - 2026-08-07

### Added
- Centralized configuration (config.json) for theming
- Shared utility module (scripts/utils.py)
- SVG validation script (scripts/validate_svgs.py)
- Separator SVG generator script
- GitHub issue templates and PR template
- CODEOWNERS for automated reviews
- Contributing guidelines and security policy
- EditorConfig for consistent formatting
- Comprehensive .gitignore

### Changed
- Improved stats dashboard color contrast
- Enhanced animation timing for smoother UX
- Updated snake workflow schedule

### Fixed
- IST timezone handling in streak calculations