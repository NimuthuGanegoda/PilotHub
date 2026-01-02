# AI Integration Tool

This repository provides a unified interface to interact with multiple AI providers, including ChatGPT (OpenAI), DeepSeek, and Grok (xAI).

## Prerequisites

- Python 3.8+
- API Keys for the providers you wish to use.

## Installation

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Set up your environment variables:
    -   Copy `.env.example` to `.env`:
        ```bash
        cp .env.example .env
        ```
    -   Open `.env` and fill in your API keys.

## Usage

You can use the tool via the command line interface (CLI).

### Syntax

```bash
python main.py --provider <provider_name> --prompt "<your_message>"
```

### Available Providers

-   `openai` (ChatGPT)
-   `deepseek`
-   `grok`

### Examples

**Using ChatGPT:**
```bash
python main.py --provider openai --prompt "Hello, how are you?"
```

**Using DeepSeek:**
```bash
python main.py --provider deepseek --prompt "Explain quantum computing."
```

**Using Grok:**
```bash
python main.py --provider grok --prompt "What is the meaning of life?"
```

## Running Tests

To run the unit tests:

```bash
python -m unittest discover tests
```
