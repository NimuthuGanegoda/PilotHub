@echo off
REM Setup script for Multi-AI Chatbot (Windows)

echo ======================================
echo Multi-AI Chatbot Setup
echo ======================================
echo.

REM Check Python version
echo Checking Python version...
python --version
if errorlevel 1 (
    echo Error: Python is not installed
    exit /b 1
)

echo.
echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies
    exit /b 1
)

echo.
echo Setting up environment file...
if not exist .env (
    copy .env.example .env
    echo Created .env file from .env.example
    echo.
    echo IMPORTANT: Please edit .env and add your API keys!
) else (
    echo .env file already exists
)

echo.
echo Creating output directories...
if not exist generated_images mkdir generated_images
if not exist generated_videos mkdir generated_videos
echo Output directories created

echo.
echo ======================================
echo Setup Complete!
echo ======================================
echo.
echo Next steps:
echo 1. Edit .env and add your API keys
echo 2. Run 'python test_chatbot.py' to verify setup
echo 3. Run 'python cli.py' for CLI interface
echo 4. Run 'python web_app.py' for web interface
echo.
pause
