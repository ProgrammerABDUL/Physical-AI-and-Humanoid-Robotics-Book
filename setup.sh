#!/bin/bash
# Setup script for the Physical AI & Humanoid Robotics course book

# Create Python virtual environment
python3 -m venv rag-backend/venv

# Activate the virtual environment
source rag-backend/venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r rag-backend/requirements.txt

echo "Virtual environment setup complete. Activate with: source rag-backend/venv/bin/activate"