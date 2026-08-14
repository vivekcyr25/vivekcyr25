.PHONY: stats connectivity separator badge access-check health-check validate optimize test lint all clean

# Run health check integrity suite
health-check:
	python scripts/health_check.py


# Generate stats dashboard SVG
stats:
	python scripts/generate_stats.py

# Build connectivity cards
connectivity:
	python scripts/build_connectivity.py

# Generate separator SVG
separator:
	python scripts/generate_separator.py

# Generate status badge SVG
badge:
	python scripts/generate_badge.py

# Run accessibility audit on SVGs
access-check:
	python scripts/inspect_accessibility.py

# Validate all SVG assets
validate:
	python scripts/validate_svgs.py

# Analyze SVG sizes and optimization opportunities
optimize:
	python scripts/svg_optimizer.py

# Run all tests
test:
	python -m pytest tests/ -v --tb=short

# Run linter
lint:
	python -m ruff check scripts/ tests/

# Run all generators and validation
all: stats connectivity separator badge access-check validate
	@echo "✅ All assets generated and validated"

# Remove generated artifacts
clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	rm -rf .pytest_cache .coverage htmlcov