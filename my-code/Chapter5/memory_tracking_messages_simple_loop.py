import os
from dotenv import load_dotenv
from agents import Agent, Runner
# from pydantic import BaseModel
# from typing import List

# Load environment variables from the .env file
load_dotenv()

# Access the API Key
api_key = os.getenv("OPENAI_API_KEY")

# Check to confirm API Key is accessible
if not api_key:
    print("FATAL ERROR: OPENAI_API_KEY not found. Please set it in your .env file")
    exit(-1)

# Create the Agent
agent = Agent(
    name="QuestionAnswer",
    instructions="You are an AI agent that answers questions."
)

messages = []

while True:
    question = input("You: ")
    messages.append({
        "role": "user",
        "content": question
    })
    result = Runner.run_sync(agent, messages)
    print("Agent: ", result.final_output)
    messages.append({
        "role": "assistant",
        "content": result.final_output
    })