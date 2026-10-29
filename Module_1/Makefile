.DEFAULT_GOAL := help

######################################################################################
           
help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Install / sync the project dependencies
	uv sync

activate: ## Start a shell with the virtual environment activated
	@if [ ! -f .venv/bin/activate ]; then \
		echo "No .venv found - run 'make install' first."; \
		exit 1; \
	fi
	@echo "Entering a shell with the virtualenv activated (type 'exit' to return)."
	@bash -c 'source .venv/bin/activate && exec "$$SHELL" -i'

lint: ## Check the code norm (flake8)
	uv run flake8 .

norm: lint ## Alias to lint

clean: ## Remove the Python caches
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	
fclean: clean ## Remove the virtual environment as well
	find . -type d -name ".venv" -exec rm -rf {} + 2>/dev/null || true 

######################################################################################

.PHONY: help install activate lint norm clean fclean
