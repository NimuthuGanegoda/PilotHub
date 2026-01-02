#!/usr/bin/env python3
"""
Simple test script for the AI Chatbot
"""
import os
import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))


def test_imports():
    """Test that all modules can be imported"""
    print("Testing imports...")
    try:
        from config import Config
        from base_provider import AIProvider, ImageGenerator, VideoGenerator
        from openai_provider import OpenAIProvider, DALLEGenerator
        from gemini_provider import GeminiProvider
        from video_provider import SimpleVideoGenerator
        from chatbot import UnifiedAIChatbot
        print("✓ All imports successful")
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False


def test_config():
    """Test configuration loading"""
    print("\nTesting configuration...")
    try:
        from config import Config
        
        # Ensure output directories can be created
        Config.ensure_output_dirs()
        
        # Check if directories were created
        if Config.IMAGE_OUTPUT_DIR.exists() and Config.VIDEO_OUTPUT_DIR.exists():
            print("✓ Output directories created successfully")
            return True
        else:
            print("✗ Failed to create output directories")
            return False
    except Exception as e:
        print(f"✗ Config test failed: {e}")
        return False


def test_chatbot_initialization():
    """Test chatbot initialization"""
    print("\nTesting chatbot initialization...")
    try:
        from chatbot import UnifiedAIChatbot
        
        chatbot = UnifiedAIChatbot()
        
        # Check available providers
        providers = chatbot.list_providers()
        print(f"  Available providers: {', '.join(providers) if providers else 'None'}")
        
        # Get status
        status = chatbot.get_status()
        print(f"  Current provider: {status['current_provider']}")
        print(f"  Image generators: {', '.join(status['available_image_generators'])}")
        print(f"  Video generators: {', '.join(status['available_video_generators'])}")
        
        if len(providers) == 0:
            print("  ⚠ Warning: No AI providers available. Please set API keys in .env file")
        else:
            print("✓ Chatbot initialized successfully")
        
        return True
    except Exception as e:
        print(f"✗ Chatbot initialization failed: {e}")
        return False


def test_file_structure():
    """Test that all required files exist"""
    print("\nTesting file structure...")
    required_files = [
        'config.py',
        'base_provider.py',
        'openai_provider.py',
        'gemini_provider.py',
        'video_provider.py',
        'chatbot.py',
        'cli.py',
        'web_app.py',
        'requirements.txt',
        '.env.example',
        '.gitignore',
        'README.md',
        'templates/index.html'
    ]
    
    base_path = Path(__file__).parent
    all_exist = True
    
    for file in required_files:
        file_path = base_path / file
        if file_path.exists():
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} not found")
            all_exist = False
    
    if all_exist:
        print("✓ All required files exist")
    else:
        print("✗ Some files are missing")
    
    return all_exist


def main():
    """Run all tests"""
    print("=" * 60)
    print("Multi-AI Chatbot Test Suite")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("File Structure", test_file_structure()))
    results.append(("Imports", test_imports()))
    results.append(("Configuration", test_config()))
    results.append(("Chatbot Initialization", test_chatbot_initialization()))
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print("\n⚠ Some tests failed. Please check the output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
