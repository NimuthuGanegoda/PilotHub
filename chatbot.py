"""
Unified AI Chatbot Interface
This module provides a single interface to interact with multiple AI providers
and media generation capabilities.
"""
from typing import Optional, List, Dict
from pathlib import Path

from config import Config
from openai_provider import OpenAIProvider, DALLEGenerator
from gemini_provider import GeminiProvider
from video_provider import ReplicateVideoGenerator, SimpleVideoGenerator


class UnifiedAIChatbot:
    """Unified chatbot that can use multiple AI providers"""
    
    def __init__(self):
        """Initialize the unified chatbot with all available providers"""
        Config.ensure_output_dirs()
        
        self.providers = {}
        self.image_generators = {}
        self.video_generators = {}
        self.conversation_history = []
        
        # Initialize text AI providers
        if Config.OPENAI_API_KEY:
            self.providers['openai'] = OpenAIProvider(Config.OPENAI_API_KEY)
        
        if Config.GEMINI_API_KEY:
            self.providers['gemini'] = GeminiProvider(Config.GEMINI_API_KEY)
        
        # Initialize image generators
        if Config.OPENAI_API_KEY:
            self.image_generators['dalle'] = DALLEGenerator(
                Config.OPENAI_API_KEY, 
                Config.IMAGE_OUTPUT_DIR
            )
        
        # Initialize video generators
        if Config.REPLICATE_API_TOKEN:
            try:
                self.video_generators['replicate'] = ReplicateVideoGenerator(
                    Config.REPLICATE_API_TOKEN,
                    Config.VIDEO_OUTPUT_DIR
                )
            except ImportError:
                # Fallback to simple generator if replicate not available
                self.video_generators['simple'] = SimpleVideoGenerator(
                    '',
                    Config.VIDEO_OUTPUT_DIR
                )
        else:
            self.video_generators['simple'] = SimpleVideoGenerator(
                '',
                Config.VIDEO_OUTPUT_DIR
            )
        
        self.current_provider = Config.DEFAULT_AI_PROVIDER
    
    def set_provider(self, provider_name: str) -> bool:
        """Switch to a different AI provider"""
        if provider_name in self.providers:
            self.current_provider = provider_name
            return True
        return False
    
    def list_providers(self) -> List[str]:
        """List all available AI providers"""
        return list(self.providers.keys())
    
    def chat(self, message: str, provider: Optional[str] = None, **kwargs) -> str:
        """
        Send a message to the AI and get a response
        
        Args:
            message: The user's message
            provider: Optional provider name to use (defaults to current provider)
            **kwargs: Additional parameters to pass to the provider
        
        Returns:
            The AI's response
        """
        provider_name = provider or self.current_provider
        
        if provider_name not in self.providers:
            return f"Error: Provider '{provider_name}' not available. Available providers: {', '.join(self.list_providers())}"
        
        # Add message to conversation history
        self.conversation_history.append({
            'role': 'user',
            'content': message
        })
        
        # Get response from provider
        provider_obj = self.providers[provider_name]
        response = provider_obj.chat(self.conversation_history, **kwargs)
        
        # Add response to conversation history
        self.conversation_history.append({
            'role': 'assistant',
            'content': response
        })
        
        return response
    
    def generate_text(self, prompt: str, provider: Optional[str] = None, **kwargs) -> str:
        """
        Generate text without conversation history
        
        Args:
            prompt: The prompt to generate text from
            provider: Optional provider name to use
            **kwargs: Additional parameters
        
        Returns:
            The generated text
        """
        provider_name = provider or self.current_provider
        
        if provider_name not in self.providers:
            return f"Error: Provider '{provider_name}' not available"
        
        provider_obj = self.providers[provider_name]
        return provider_obj.generate_text(prompt, **kwargs)
    
    def generate_image(self, prompt: str, generator: Optional[str] = None, **kwargs) -> str:
        """
        Generate an image from a text prompt
        
        Args:
            prompt: Description of the image to generate
            generator: Optional generator name (defaults to dalle)
            **kwargs: Additional parameters
        
        Returns:
            Path to the generated image file
        """
        generator_name = generator or Config.DEFAULT_IMAGE_GENERATOR
        
        if generator_name not in self.image_generators:
            return f"Error: Image generator '{generator_name}' not available. Available: {', '.join(self.image_generators.keys())}"
        
        generator_obj = self.image_generators[generator_name]
        return generator_obj.generate_image(prompt, **kwargs)
    
    def generate_video(self, prompt: str, generator: Optional[str] = None, **kwargs) -> str:
        """
        Generate a video from a text prompt
        
        Args:
            prompt: Description of the video to generate
            generator: Optional generator name
            **kwargs: Additional parameters
        
        Returns:
            Path to the generated video file
        """
        # Use replicate if available, otherwise simple
        if 'replicate' in self.video_generators:
            generator_name = 'replicate'
        else:
            generator_name = 'simple'
        
        generator_obj = self.video_generators[generator_name]
        return generator_obj.generate_video(prompt, **kwargs)
    
    def reset_conversation(self):
        """Clear the conversation history"""
        self.conversation_history = []
        
        # Reset chat sessions for providers that maintain state
        if 'gemini' in self.providers:
            self.providers['gemini'].reset_chat()
    
    def get_conversation_history(self) -> List[Dict]:
        """Get the current conversation history"""
        return self.conversation_history
    
    def get_status(self) -> Dict:
        """Get the status of all providers and generators"""
        return {
            'current_provider': self.current_provider,
            'available_text_providers': self.list_providers(),
            'available_image_generators': list(self.image_generators.keys()),
            'available_video_generators': list(self.video_generators.keys()),
            'conversation_length': len(self.conversation_history)
        }
