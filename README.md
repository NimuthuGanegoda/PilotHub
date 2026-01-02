# 🤖 Multi-AI Chatbot

A unified AI chatbot that integrates multiple AI providers (Gemini, ChatGPT, Claude) and includes AI-powered image and video generation capabilities.

## ✨ Features

- **Multiple AI Providers**: Chat with different AI models
  - 🤖 Google Gemini
  - 🤖 OpenAI ChatGPT (GPT-4)
  - 🤖 Anthropic Claude (optional)

- **Media Generation**:
  - 🎨 Image generation using DALL-E and Stable Diffusion
  - 🎥 Video generation using Replicate API

- **Two Interfaces**:
  - 💻 Command Line Interface (CLI)
  - 🌐 Web Interface

- **Conversation Management**:
  - Maintain conversation history
  - Switch between AI providers mid-conversation
  - Reset conversation at any time

## 📋 Requirements

- Python 3.8 or higher
- API keys for the services you want to use:
  - OpenAI API key (for ChatGPT and DALL-E)
  - Google Gemini API key
  - Replicate API token (optional, for video generation)
  - Stability AI API key (optional, for Stable Diffusion)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NimuthuGanegoda/AI-Setups.git
   cd AI-Setups
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   REPLICATE_API_TOKEN=your_replicate_token_here  # Optional
   ```

## 🎯 Usage

### Command Line Interface

Run the CLI chatbot:

```bash
python cli.py
```

**Available Commands**:
- `/help` - Show help message
- `/providers` - List available AI providers
- `/switch <provider>` - Switch to a different provider (e.g., `/switch openai`)
- `/image <description>` - Generate an image (e.g., `/image sunset over mountains`)
- `/video <description>` - Generate a video (e.g., `/video waves crashing on beach`)
- `/reset` - Clear conversation history
- `/status` - Show current status
- `/exit` or `/quit` - Exit the chatbot

**Example Session**:
```
You: Hello, how are you?
GEMINI: Hello! I'm doing well, thank you for asking...

You: /switch openai
✓ Switched to openai

You: What's the weather like today?
OPENAI: I don't have access to real-time weather data...

You: /image a beautiful sunset over the ocean
Generating image...
Image saved to: generated_images/dalle_20240102_123456.png
```

### Web Interface

Run the web server:

```bash
python web_app.py
```

Then open your browser and navigate to:
```
http://127.0.0.1:5000
```

**Web Interface Features**:
- Interactive chat interface
- Switch AI providers using the dropdown menu
- Generate images and videos with dedicated buttons
- View generated media directly in the browser
- Reset conversation history

## 📁 Project Structure

```
AI-Setups/
├── cli.py                  # Command-line interface
├── web_app.py             # Web interface (Flask)
├── chatbot.py             # Unified chatbot logic
├── config.py              # Configuration management
├── base_provider.py       # Abstract base classes
├── openai_provider.py     # OpenAI/ChatGPT integration
├── gemini_provider.py     # Google Gemini integration
├── video_provider.py      # Video generation
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── templates/
│   └── index.html        # Web UI template
├── generated_images/     # Generated images (created automatically)
└── generated_videos/     # Generated videos (created automatically)
```

## 🔑 Getting API Keys

### OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key

### Google Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key

### Replicate API Token (Optional)
1. Go to [Replicate](https://replicate.com/)
2. Sign up or log in
3. Go to your account settings
4. Copy your API token

## 🎨 Image Generation

The chatbot supports image generation using DALL-E:

**CLI**:
```
You: /image a futuristic city at night with neon lights
```

**Web Interface**: Click the "🎨 Generate Image" button

Generated images are saved in the `generated_images/` directory.

## 🎥 Video Generation

Video generation is supported through Replicate's text-to-video models:

**CLI**:
```
You: /video ocean waves crashing on a beach at sunset
```

**Web Interface**: Click the "🎥 Generate Video" button

Generated videos are saved in the `generated_videos/` directory.

**Note**: Video generation requires a Replicate API token and may take several minutes to complete.

## 💡 Tips

- Start with Gemini (it's fast and free with generous limits)
- Use ChatGPT for more detailed or creative responses
- Image generation works best with detailed, descriptive prompts
- Video generation can take 2-5 minutes depending on the model
- The conversation history is maintained across provider switches

## 🛠️ Customization

### Change Default Provider
Edit `.env`:
```
DEFAULT_AI_PROVIDER=openai  # or gemini
```

### Change Default Image Generator
Edit `.env`:
```
DEFAULT_IMAGE_GENERATOR=dalle
```

### Configure Output Directories
Edit `.env`:
```
IMAGE_OUTPUT_DIR=my_images
VIDEO_OUTPUT_DIR=my_videos
```

## 🐛 Troubleshooting

**"Configuration errors" on startup**:
- Make sure you've created a `.env` file with your API keys
- Verify that at least one AI provider's API key is set

**"Provider not available" error**:
- Check that the API key for that provider is set in `.env`
- Verify the API key is valid

**Image generation fails**:
- Ensure OPENAI_API_KEY is set
- Check that you have credits in your OpenAI account

**Video generation creates only a placeholder**:
- Set REPLICATE_API_TOKEN in `.env`
- Install replicate library: `pip install replicate`

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 👨‍💻 Author

Created by NimuthuGanegoda

## 🙏 Acknowledgments

- OpenAI for GPT-4 and DALL-E
- Google for Gemini
- Replicate for video generation models
- All the amazing open-source libraries used in this project