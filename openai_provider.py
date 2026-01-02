"""
OpenAI Provider (ChatGPT and DALL-E)
"""
import os
import requests
from pathlib import Path
from datetime import datetime
from openai import OpenAI
from base_provider import AIProvider, ImageGenerator


class OpenAIProvider(AIProvider):
    """OpenAI ChatGPT provider"""
    
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4"
    
    def generate_text(self, prompt: str, **kwargs) -> str:
        """Generate text using ChatGPT"""
        try:
            response = self.client.chat.completions.create(
                model=kwargs.get('model', self.model),
                messages=[{"role": "user", "content": prompt}],
                max_tokens=kwargs.get('max_tokens', 1000),
                temperature=kwargs.get('temperature', 0.7)
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating text: {str(e)}"
    
    def chat(self, messages: list, **kwargs) -> str:
        """Chat with ChatGPT using conversation history"""
        try:
            response = self.client.chat.completions.create(
                model=kwargs.get('model', self.model),
                messages=messages,
                max_tokens=kwargs.get('max_tokens', 1000),
                temperature=kwargs.get('temperature', 0.7)
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error in chat: {str(e)}"


class DALLEGenerator(ImageGenerator):
    """DALL-E image generator"""
    
    def __init__(self, api_key: str, output_dir: Path):
        super().__init__(api_key)
        self.client = OpenAI(api_key=api_key)
        self.output_dir = output_dir
        self.output_dir.mkdir(exist_ok=True)
    
    def generate_image(self, prompt: str, **kwargs) -> str:
        """Generate an image using DALL-E"""
        try:
            response = self.client.images.generate(
                model=kwargs.get('model', 'dall-e-3'),
                prompt=prompt,
                size=kwargs.get('size', '1024x1024'),
                quality=kwargs.get('quality', 'standard'),
                n=1
            )
            
            # Get the image URL
            image_url = response.data[0].url
            
            # Download and save the image
            image_response = requests.get(image_url)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"dalle_{timestamp}.png"
            filepath = self.output_dir / filename
            
            with open(filepath, 'wb') as f:
                f.write(image_response.content)
            
            return str(filepath)
        except Exception as e:
            return f"Error generating image: {str(e)}"
