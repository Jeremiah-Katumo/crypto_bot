# crypto_bot

crypto_bot is an interactive, voice-enabled chatbot that helps users learn about trending, sustainable, and trusted cryptocurrencies. It uses text-to-speech to provide a conversational experience and shares fun facts about popular coins.

## Features

- Answers questions about trending, sustainable, and trusted cryptocurrencies
- Shares fun facts about Bitcoin, Ethereum, Cardano, and Solana
- Voice responses using text-to-speech (pyttsx3)
- Simple command-line interface

## Requirements

- Python 3.12 or newer
- [pyttsx3](https://pypi.org/project/pyttsx3/)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/crypto_bot.git
   cd crypto_bot
   ```
2. Install dependencies:
   ```bash
   pip install pyttsx3
   ```

## Usage

Run the chatbot from your terminal:
```bash
python main.py
```

Write your questions (e.g., "What coins are trending?", "Tell me a fact", "Which coin is sustainable?") and listen to the bot's responses. Type `exit` to quit.

## Project Structure

- `main.py` — Entry point for the chatbot
- `bot.py` — Chatbot logic and voice functions
- `data.py` — Cryptocurrency data and fun facts
- `Images/` — Screenshots and images

## Disclaimer

Crypto investments are risky. Always do your own research before investing!
