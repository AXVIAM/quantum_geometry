#!/bin/bash

# Set up Python virtual environment for AXVIAM
echo "Creating virtual environment 'venv'..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing required Python packages..."
pip install --upgrade pip
pip install numpy pandas matplotlib scipy jupyter ipykernel

echo "Registering Jupyter kernel..."
python -m ipykernel install --user --name=axviam_env --display-name "Python (AXVIAM)"

echo "Saving current environment to requirements.txt..."
pip freeze > requirements.txt

echo "AXVIAM Python environment setup complete."
