SHELL := /bin/bash

usage:
	@echo "Usage:"
	@echo "	usage (default)"
	@echo "	interpreter"
	@echo "	venv install"
	@echo "	venv lint"
	@echo "	venv format"
	@echo "	clean"


# Variables
VENV_NAME?=venv
VENV_DIR?=./$(VENV_NAME)
PYTHON=${VENV_DIR}/bin/python
PIP=${VENV_DIR}/bin/pip

# By default, set up the virtual environment and install dependencies
all: venv install


interpreter:
	@pyenv install --skip-existing 3.11
	@pyenv local 3.11

# Create venv if not exists already
venv:
	test -d $(VENV_DIR) || pyenv exec python3.11 -m venv $(VENV_DIR)

# install dependencies, to activate environment run source venv/bin/activate
install: venv
	$(PIP) install -r requirements.dev.txt
	$(PYTHON) -m pre-commit install

# Check the project with ruff
lint: venv
	$(PYTHON) -m ruff check .

# Format project files with ruff
format: venv
	$(PYTHON) -m ruff format .
	$(PYTHON) -m ruff check --fix .

# Clean up the virtual environment and other generated files
clean:
	rm -rf $(VENV_NAME)
	find . -name "*.pyc" -exec rm {} \;
	find . -name "__pycache__" -exec rm -r {} \;