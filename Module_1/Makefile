

.DEFAULT_GOAL := help

##########################################################################

help:


activate:
	source .venv/bin/activate

install:
	uv sync

test:
	

lint:
	uv run flake8 .

format:

	
clean:
	find . -type d -name "__pycache__" -exec rm -rf {}


fclean: clean
	rm -rf .venv
	
	
##########################################################################

.PHONY: install test lint format clean