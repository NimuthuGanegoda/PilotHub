# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### 1. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

Or use the setup script:
```bash
./setup.sh
```

### 2. Get Your API Keys

You need at least ONE of these:

**Option A: Google Gemini (Free tier available)**
- Visit: https://makersuite.google.com/app/apikey
- Sign in and create an API key
- Free tier: 60 requests per minute

**Option B: OpenAI (Paid)**
- Visit: https://platform.openai.com/api-keys
- Create an account and add billing
- Get your API key

### 3. Configure Environment

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your keys
nano .env  # or use your favorite editor
```

Minimum configuration (.env):
```
GEMINI_API_KEY=your_key_here
DEFAULT_AI_PROVIDER=gemini
```

### 4. Run the Chatbot

**CLI Mode:**
```bash
python cli.py
```

**Web Mode:**
```bash
python web_app.py
# Open http://127.0.0.1:5000 in your browser
```

## 📖 Example Usage

### Chat with AI

```
You: Hello! Tell me a joke about programming.

GEMINI: Why do programmers prefer dark mode?
Because light attracts bugs! 🐛
```

### Switch Providers

```
You: /switch openai
✓ Switched to openai

You: What's the capital of France?
OPENAI: The capital of France is Paris.
```

### Generate Images

```
You: /image a serene mountain landscape at sunset with a lake
Generating image...
Image saved to: generated_images/dalle_20240102_123456.png
```

### Generate Videos

```
You: /video ocean waves gently rolling onto a sandy beach
Generating video... (this may take a while)
Video saved to: generated_videos/video_20240102_123456.mp4
```

## 💡 Tips for Best Results

### Text Generation
- Be specific in your questions
- Provide context when needed
- Try different providers for different tasks:
  - **Gemini**: Fast, good for general questions
  - **ChatGPT**: More detailed, creative responses

### Image Generation
- Use descriptive language
- Specify style (e.g., "photorealistic", "cartoon", "oil painting")
- Mention colors, lighting, composition
- Example: "A photorealistic portrait of a golden retriever in a sunny garden, shallow depth of field"

### Video Generation
- Keep prompts simple and clear
- Describe motion and scene
- Example: "Sunrise over a calm ocean with gentle waves"

## 🔧 Troubleshooting

**"Configuration errors" on startup**
```bash
# Make sure .env exists
cp .env.example .env

# Edit and add at least one API key
nano .env
```

**Import errors**
```bash
# Install all dependencies
pip install -r requirements.txt
```

**"Provider not available"**
- Check that the API key is set in .env
- Verify the key is valid (test on the provider's website)

## 🌟 Next Steps

1. **Explore the web interface** - More visual and user-friendly
2. **Try different AI providers** - Compare responses
3. **Generate images** - Create unique artwork
4. **Experiment with prompts** - Learn what works best

## 📚 Full Documentation

See [README.md](README.md) for complete documentation.

## ❓ Need Help?

- Check the [README.md](README.md) for detailed information
- Review the [.env.example](.env.example) for all configuration options
- Run `python test_chatbot.py` to verify your setup
