#!/usr/bin/env python3
"""
CLI Interface for the Unified AI Chatbot
"""
import sys
import argparse
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt, Confirm
from rich.table import Table

from chatbot import UnifiedAIChatbot
from config import Config


console = Console()


def display_welcome():
    """Display welcome message"""
    welcome_text = """
# 🤖 Multi-AI Chatbot

Welcome to the Unified AI Chatbot! This chatbot integrates multiple AI providers:
- **ChatGPT** (OpenAI)
- **Gemini** (Google)

**Features:**
- 💬 Text chat with multiple AI models
- 🎨 Image generation (DALL-E)
- 🎥 Video generation (Replicate)

**Commands:**
- `/help` - Show this help message
- `/providers` - List available AI providers
- `/switch <provider>` - Switch to a different AI provider
- `/image <prompt>` - Generate an image
- `/video <prompt>` - Generate a video
- `/reset` - Clear conversation history
- `/status` - Show current status
- `/exit` or `/quit` - Exit the chatbot
"""
    console.print(Panel(Markdown(welcome_text), title="Welcome", border_style="blue"))


def display_status(chatbot: UnifiedAIChatbot):
    """Display current chatbot status"""
    status = chatbot.get_status()
    
    table = Table(title="Chatbot Status", show_header=True, header_style="bold magenta")
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Current Provider", status['current_provider'])
    table.add_row("Text Providers", ", ".join(status['available_text_providers']))
    table.add_row("Image Generators", ", ".join(status['available_image_generators']))
    table.add_row("Video Generators", ", ".join(status['available_video_generators']))
    table.add_row("Conversation Messages", str(status['conversation_length']))
    
    console.print(table)


def main():
    """Main CLI application"""
    parser = argparse.ArgumentParser(description="Multi-AI Chatbot CLI")
    parser.add_argument('--provider', type=str, help='Default AI provider to use')
    parser.add_argument('--no-interactive', action='store_true', help='Non-interactive mode')
    args = parser.parse_args()
    
    # Validate configuration
    valid, errors = Config.validate()
    if not valid:
        console.print("[red]Configuration errors:[/red]")
        for error in errors:
            console.print(f"  [red]✗[/red] {error}")
        console.print("\n[yellow]Please set up your .env file based on .env.example[/yellow]")
        sys.exit(1)
    
    # Initialize chatbot
    try:
        chatbot = UnifiedAIChatbot()
    except Exception as e:
        console.print(f"[red]Error initializing chatbot: {e}[/red]")
        sys.exit(1)
    
    # Set provider if specified
    if args.provider:
        if chatbot.set_provider(args.provider):
            console.print(f"[green]✓[/green] Using {args.provider} provider")
        else:
            console.print(f"[red]✗[/red] Provider {args.provider} not available")
    
    # Display welcome message
    if not args.no_interactive:
        display_welcome()
        display_status(chatbot)
        console.print()
    
    # Main interaction loop
    while True:
        try:
            # Get user input
            user_input = Prompt.ask("\n[bold cyan]You[/bold cyan]").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.startswith('/'):
                command_parts = user_input.split(maxsplit=1)
                command = command_parts[0].lower()
                command_arg = command_parts[1] if len(command_parts) > 1 else ""
                
                if command in ['/exit', '/quit']:
                    console.print("[yellow]Goodbye![/yellow]")
                    break
                
                elif command == '/help':
                    display_welcome()
                
                elif command == '/providers':
                    providers = chatbot.list_providers()
                    console.print(f"[green]Available providers:[/green] {', '.join(providers)}")
                    console.print(f"[cyan]Current provider:[/cyan] {chatbot.current_provider}")
                
                elif command == '/switch':
                    if command_arg:
                        if chatbot.set_provider(command_arg):
                            console.print(f"[green]✓[/green] Switched to {command_arg}")
                        else:
                            console.print(f"[red]✗[/red] Provider {command_arg} not available")
                    else:
                        console.print("[red]Usage: /switch <provider>[/red]")
                
                elif command == '/reset':
                    chatbot.reset_conversation()
                    console.print("[green]✓[/green] Conversation history cleared")
                
                elif command == '/status':
                    display_status(chatbot)
                
                elif command == '/image':
                    if command_arg:
                        console.print(f"[yellow]Generating image...[/yellow]")
                        result = chatbot.generate_image(command_arg)
                        console.print(f"[green]Image saved to:[/green] {result}")
                    else:
                        console.print("[red]Usage: /image <description>[/red]")
                
                elif command == '/video':
                    if command_arg:
                        console.print(f"[yellow]Generating video... (this may take a while)[/yellow]")
                        result = chatbot.generate_video(command_arg)
                        console.print(f"[green]Video saved to:[/green] {result}")
                    else:
                        console.print("[red]Usage: /video <description>[/red]")
                
                else:
                    console.print(f"[red]Unknown command: {command}[/red]")
                    console.print("[yellow]Type /help for available commands[/yellow]")
                
                continue
            
            # Regular chat message
            console.print("[yellow]Thinking...[/yellow]")
            response = chatbot.chat(user_input)
            
            console.print(f"\n[bold green]{chatbot.current_provider.upper()}[/bold green]")
            console.print(Panel(Markdown(response), border_style="green"))
        
        except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted. Type /exit to quit.[/yellow]")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")


if __name__ == "__main__":
    main()
