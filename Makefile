.PHONY: venv install run-etl test clean

# Default python executable
PYTHON = python3
VENV = venv

# Create virtual environment
venv:
	$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created. Activate with: source $(VENV)/bin/activate"

# Install requirements
install:
	pip install --upgrade pip
	pip install -r requirements.txt

# Run the data processing pipeline
run-etl:
	python scripts/etl.py

# Run unit tests
test:
	pytest -v

# Clean up Python cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	@echo "Cleaned temporary files."
