.PHONY: stats connectivity separator validate all

# Generate stats dashboard SVG
stats:
	python scripts/generate_stats.py

# Build connectivity cards
connectivity:
	python scripts/build_connectivity.py

# Generate separator SVG
separator:
	python scripts/generate_separator.py

# Validate all SVG assets
validate:
	python scripts/validate_svgs.py

# Run all generators
all: stats connectivity separator validate
	@echo "✅ All assets generated and validated"
