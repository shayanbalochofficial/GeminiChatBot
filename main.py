import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Welcome to Shayan's ChatGPT !").send()

@cl.on_message
async def on_message(message: cl.Message):
    user_prompt = message.content
    response = model.generate_content(user_prompt)
    await cl.Message(content=response.text).send()