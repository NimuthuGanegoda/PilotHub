# Contributing to Multi-AI Chatbot

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 🎯 Ways to Contribute

- **Report bugs**: Open an issue describing the bug
- **Suggest features**: Open an issue with your feature idea
- **Improve documentation**: Fix typos, add examples, clarify instructions
- **Add new AI providers**: Integrate additional AI services
- **Add new features**: Implement new functionality
- **Fix bugs**: Submit pull requests for known issues

## 🚀 Getting Started

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/AI-Setups.git
   cd AI-Setups
   ```
3. **Set up development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Code Guidelines

### Python Style
- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small

### Adding a New AI Provider

To add a new AI provider:

1. **Create a new provider file** (e.g., `anthropic_provider.py`):
   ```python
   from base_provider import AIProvider
   
   class AnthropicProvider(AIProvider):
       def __init__(self, api_key: str):
           super().__init__(api_key)
           # Initialize your provider
       
       def generate_text(self, prompt: str, **kwargs) -> str:
           # Implement text generation
           pass
       
       def chat(self, messages: list, **kwargs) -> str:
           # Implement chat functionality
           pass
   ```

2. **Update `config.py`**:
   - Add API key configuration
   - Add provider to defaults if needed

3. **Update `chatbot.py`**:
   - Import the new provider
   - Initialize it in `UnifiedAIChatbot.__init__()`

4. **Update documentation**:
   - Add provider to README.md
   - Update .env.example
   - Add usage examples

### Adding Media Generators

Follow similar patterns for image or video generators:

1. **Inherit from base classes**: `ImageGenerator` or `VideoGenerator`
2. **Implement required methods**: `generate_image()` or `generate_video()`
3. **Handle errors gracefully**: Return error messages, don't crash
4. **Save files properly**: Use the configured output directories

## 🧪 Testing

Before submitting:

1. **Run the test suite**:
   ```bash
   python test_chatbot.py
   ```

2. **Test manually**:
   ```bash
   python cli.py
   python web_app.py
   ```

3. **Check for import errors**: Ensure all modules import correctly

4. **Test with different providers**: Verify compatibility

## 📄 Documentation

- Update README.md for significant changes
- Add examples for new features
- Update QUICKSTART.md if setup process changes
- Comment complex code sections

## 🔍 Pull Request Process

1. **Update documentation**: Ensure docs reflect your changes
2. **Test thoroughly**: All functionality should work
3. **Follow code style**: Maintain consistency
4. **Describe changes**: Write clear PR description
5. **Link issues**: Reference related issues

## 🐛 Bug Reports

When reporting bugs, include:

- **Description**: Clear description of the bug
- **Steps to reproduce**: How to trigger the bug
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: Python version, OS, etc.
- **Error messages**: Full error traceback

Example:
```
**Bug**: Image generation fails with DALL-E

**Steps to reproduce**:
1. Set OPENAI_API_KEY in .env
2. Run: python cli.py
3. Enter: /image sunset over ocean
4. Error occurs

**Error message**:
```
Error generating image: ...
```

**Environment**:
- Python: 3.11.0
- OS: Ubuntu 22.04
- openai package: 1.0.0
```

## 💡 Feature Requests

When suggesting features, include:

- **Use case**: Why is this feature needed?
- **Description**: What should it do?
- **Examples**: How would it be used?
- **Alternatives**: Other solutions you've considered

## 📜 Code of Conduct

- Be respectful and inclusive
- Accept constructive criticism
- Focus on what's best for the project
- Show empathy towards others

## ❓ Questions?

- **Check existing issues**: Your question might be answered
- **Read the docs**: Check README.md and QUICKSTART.md
- **Ask in issues**: Open an issue with the "question" label

## 🙏 Thank You!

Your contributions make this project better for everyone. We appreciate your time and effort!
