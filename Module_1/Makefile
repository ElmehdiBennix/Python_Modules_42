.DEFAULT_GOAL := help
SHELL := /bin/bash

PY_DIRS := ex00 ex01 ex02 ex03 ex04 ex05

# Entry point of each exercise (the subject runs zoom.py / rotate.py directly).
TARGETS := ex00:tester.py ex01:tester.py ex02:tester.py \
           ex03:zoom.py ex04:rotate.py ex05:tester.py

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

activate: ## Activate the virtual environment
	@source .venv/bin/activate && echo "venv activated: $$VIRTUAL_ENV"

install: ## Install / sync the project dependencies
	uv sync

test: ## Run the tester of every exercise
	@failed=0; \
	for target in $(TARGETS); do \
		dir=$${target%%:*}; \
		file=$${target##*:}; \
		printf "  %-6s %-12s " "$$dir" "$$file"; \
		out=$$(cd $$dir && MPLBACKEND=Agg ../.venv/bin/python $$file 2>&1); \
		if [ $$? -eq 0 ]; then \
			echo "OK"; \
		else \
			echo "FAILED"; \
			echo "$$out" | head -20; \
			failed=1; \
		fi; \
	done; \
	if [ $$failed -ne 0 ]; then \
		echo "Some testers failed."; exit 1; \
	fi; \
	echo "All testers passed."

lint: ## Check the code norm (flake8, exposed as norminette)
	uv run norminette .

norminette: lint ## Alias of lint

format: ## Format the code with black (79 chars, norm compatible)
	uv run black .

clean: ## Remove the Python caches
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf .pytest_cache .mypy_cache .ruff_cache

fclean: clean ## Remove the virtual environment as well
	rm -rf .venv

.PHONY: help activate install test lint norminette format clean fclean
