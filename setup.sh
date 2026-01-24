#!/bin/bash
# Setup script for Multi-AI Chatbot

echo "======================================"
echo "Multi-AI Chatbot Setup"
echo "======================================"
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

echo ""
echo "Setting up environment file..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ Created .env file from .env.example"
    echo ""
    echo "⚠ IMPORTANT: Please edit .env and add your API keys!"
else
    echo "✓ .env file already exists"
fi

echo ""
echo "Creating output directories..."
mkdir -p generated_images
mkdir -p generated_videos
echo "✓ Output directories created"

echo ""
echo "======================================"
echo "Setup Complete!"
echo "======================================"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your API keys"
echo "2. Run 'python test_chatbot.py' to verify setup"
echo "3. Run 'python cli.py' for CLI interface"
echo "4. Run 'python web_app.py' for web interface"
echo ""
