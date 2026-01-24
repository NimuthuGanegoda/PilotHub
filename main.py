import argparse
import sys
from src.ai_manager import AIManager

def main():
    parser = argparse.ArgumentParser(description="AI Tool Integrator (ChatGPT, DeepSeek, Grok)")
    parser.add_argument('--provider', type=str, required=True, choices=['openai', 'deepseek', 'grok'], help='The AI provider to use.')
    parser.add_argument('--prompt', type=str, required=True, help='The prompt to send to the AI.')

    args = parser.parse_args()

    try:
        manager = AIManager(args.provider)
        response = manager.chat(args.prompt)
        print(f"Response from {args.provider}:\n{response}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
