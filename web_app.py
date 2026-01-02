#!/usr/bin/env python3
"""
Web Interface for the Unified AI Chatbot
"""
from flask import Flask, render_template, request, jsonify, send_from_directory
from pathlib import Path
import os

from chatbot import UnifiedAIChatbot
from config import Config

app = Flask(__name__)
chatbot = None


@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')


@app.route('/api/status', methods=['GET'])
def get_status():
    """Get chatbot status"""
    return jsonify(chatbot.get_status())


@app.route('/api/providers', methods=['GET'])
def get_providers():
    """Get available providers"""
    return jsonify({
        'providers': chatbot.list_providers(),
        'current': chatbot.current_provider
    })


@app.route('/api/switch-provider', methods=['POST'])
def switch_provider():
    """Switch AI provider"""
    data = request.json
    provider = data.get('provider')
    
    if chatbot.set_provider(provider):
        return jsonify({'success': True, 'provider': provider})
    else:
        return jsonify({'success': False, 'error': 'Provider not available'}), 400


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    data = request.json
    message = data.get('message', '')
    provider = data.get('provider')
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    try:
        response = chatbot.chat(message, provider=provider)
        return jsonify({
            'response': response,
            'provider': provider or chatbot.current_provider
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/generate-image', methods=['POST'])
def generate_image():
    """Generate an image"""
    data = request.json
    prompt = data.get('prompt', '')
    
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    
    try:
        filepath = chatbot.generate_image(prompt)
        filename = Path(filepath).name
        return jsonify({
            'success': True,
            'filepath': filepath,
            'url': f'/images/{filename}'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/generate-video', methods=['POST'])
def generate_video():
    """Generate a video"""
    data = request.json
    prompt = data.get('prompt', '')
    
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    
    try:
        filepath = chatbot.generate_video(prompt)
        filename = Path(filepath).name
        return jsonify({
            'success': True,
            'filepath': filepath,
            'url': f'/videos/{filename}'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/reset', methods=['POST'])
def reset_conversation():
    """Reset conversation history"""
    chatbot.reset_conversation()
    return jsonify({'success': True})


@app.route('/images/<path:filename>')
def serve_image(filename):
    """Serve generated images"""
    return send_from_directory(Config.IMAGE_OUTPUT_DIR, filename)


@app.route('/videos/<path:filename>')
def serve_video(filename):
    """Serve generated videos"""
    return send_from_directory(Config.VIDEO_OUTPUT_DIR, filename)


def main():
    """Run the web server"""
    global chatbot
    
    # Validate configuration
    valid, errors = Config.validate()
    if not valid:
        print("Configuration errors:")
        for error in errors:
            print(f"  ✗ {error}")
        print("\nPlease set up your .env file based on .env.example")
        return
    
    # Initialize chatbot
    Config.ensure_output_dirs()
    chatbot = UnifiedAIChatbot()
    
    # Create templates directory if it doesn't exist
    templates_dir = Path(__file__).parent / 'templates'
    templates_dir.mkdir(exist_ok=True)
    
    print("=" * 60)
    print("🤖 Multi-AI Chatbot Web Interface")
    print("=" * 60)
    print(f"Available providers: {', '.join(chatbot.list_providers())}")
    print(f"Current provider: {chatbot.current_provider}")
    print("\nStarting server at http://127.0.0.1:5000")
    print("Press Ctrl+C to stop")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
