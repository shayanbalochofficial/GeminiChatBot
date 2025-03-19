import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables and configure the API
load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Start a loop to continuously get user queries
while True:
    # Get input from the user
    user_prompt = input("Enter your prompt (or 'exit' to quit): ")
    
    # Check if the user wants to exit
    if user_prompt.lower() == 'exit':
        break
    
    # Generate and print the response
    response = model.generate_content(user_prompt)
    print(response.text)