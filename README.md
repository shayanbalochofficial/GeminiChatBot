
# Simple Gemini-Powered AI ChatBot

This `Simple Gemini-Powered AI ChatBot` is a sleek, terminal-based conversational tool built with Python, Chainlit, and Google’s Gemini API. Ask it anything, and it’ll respond with smart, AI-generated answers—all in real-time! Whether you’re exploring AI, testing prompts, or just chatting, this bot brings the power of Gemini to your fingertips.

## Features

- **Real-Time Chat**: Engage in a live conversation with the bot via a web-based interface.
- **Gemini AI**: Powered by Google’s `gemini-2.0-flash` model for fast, intelligent responses.
- **Simple Setup**: Uses Chainlit for an easy-to-use chat UI and `.env` for secure API key management.
- **Custom Welcome**: Greets you with a friendly “Welcome to Shayan’s ChatGPT!” message on start.
- **Lightweight**: Minimal code, maximum impact—perfect for learning or quick AI experiments.

## How to Use

1. **Prerequisites**:
   - Ensure you have Python installed (version 3.9 or higher recommended).
   - Obtain a Google Gemini API key from [Google’s AI Studio](https://makersuite.google.com/app/apikey).
   - Install required packages using `pip` or `uv` (a faster package manager):
     ```bash
     pip install chainlit google-generativeai python-dotenv
     # OR with uv
     uv pip install chainlit google-generativeai python-dotenv
     ```

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/shayanbalochofficial/GeminiChatBot.git
   cd GeminiChatBot
   ```

3. **Set Up Environment**:
   - Create a `.env` file in the project directory and add your Gemini API key:
     ```bash
     echo "GEMINI_API_KEY=your_api_key_here" > .env
     ```
   - Replace `your_api_key_here` with your actual API key.

4. **Run the App**:
   - Execute the following command in your terminal:
     ```bash
     chainlit run chatbot.py
     ```
   - Your browser will open to `http://localhost:8000`, where you can start chatting with the bot.

5. **Usage**:
   - Type a message or question in the chat interface.
   - Hit send, and the bot will respond with an AI-generated answer powered by Gemini.

## Requirements
- Python 3.9+
- Chainlit (`pip install chainlit`)
- Google Generative AI SDK (`pip install google-generativeai`)
- Python Dotenv (`pip install python-dotenv`)
- A Google Gemini API key (free tier available at time of writing)

## File Structure
- `main.py`: The main script containing the bot logic.
- `.env`: Stores your API key securely (not tracked by Git—add to `.gitignore`).

## Contributors
- **[Shayan Baloch](https://github.com/shayanbalochofficial)** - Creator and developer of this Gemini-Powered AI ChatBot.

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments
- Built as part of my journey into AI and Python—exploring how simple code can unlock powerful conversations!
- Thanks to Chainlit for an awesome chat framework and Google for the Gemini API.

---

Happy chatting! 🚀
