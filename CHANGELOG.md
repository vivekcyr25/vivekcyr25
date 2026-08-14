# Changelog

All notable changes to the GitHub profile README are documented here.

## [2.2.0] - 2026-08-11

### Added
- VisionOS SVG badge generator script (`scripts/generate_badge.py`)
- Animated badge guide documentation (`docs/BADGE_GUIDE.md`)
- SVG accessibility inspector (`scripts/inspect_accessibility.py`)
- GitHub Actions workflow for Accessibility auditing (`.github/workflows/accessibility.yml`)
- Workflow reference documentation (`docs/WORKFLOWS.md`)
- Markdown table formatter utility (`scripts/generate_table.py`)
- Profile statistics exporter for JSON & CSV summaries (`scripts/export_stats.py`)
- Reusable SVG template components (`scripts/templates.py`)
- Comprehensive test coverage for all new tools (`tests/test_badge.py`, `tests/test_table.py`, `tests/test_accessibility.py`, `tests/test_optimizer.py`, `tests/test_export.py`, `tests/test_templates.py`)

### Fixed
- Fixed UTF-8 BOM encoding compatibility issue in `pyproject.toml` and `setup.cfg` for Python 3.14.

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

## [Unreleased] - UI Overhaul Batch

### Fixed
- Truncated 'VISIONOS INTERF' banner title restored to 'VISIONOS INTERFACE'
- Streak stats card self-hosted to remove external service dependency

### Improved
- Connectivity card border radius increased to 12px
- Logo icons scaled to 38px for improved visibility  
- Animated border stroke-width thickened to 1.8px
- Platform label font upgraded to 700 weight, 12.5px size
- Bottom accent lines added to all platform cards
- Stats dashboard background gradient deepened for contrast
- Streak ring enhanced with dashed purple accent overlay
- Section divider opacity improved from 0.25 to 0.35

### Added
- CARD_SUBTITLES map for platform role descriptions
- VisionOS color palette constants in scripts/constants.py
- strip_svg_comments() and normalize_svg_whitespace() in svg_optimizer.py
- slugify() utility function in scripts/utils.py
- SVG title and desc elements for screen reader accessibility
- Footer watermark in streak stats card

### Refactored
- Brand and label colors moved to scripts/colors.py
- VisionOS constants imported into generate_stats.py
- Connectivity banner output normalized with whitespace cleaner
