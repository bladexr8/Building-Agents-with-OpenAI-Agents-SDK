import os
# import requests
# from datetime import datetime
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

# Create empty list (this will contain messages)
messages = []

# Initial message
messages.append({
    "role": "user",
    "content": "How hot is the sun?"
})

# Call agent
result = Runner.run_sync(agent, messages)
print(result.final_output)

# Add response to message
messages.append({
    "role": "assistant",
    "content": result.final_output
})

# Add second question to message
messages.append({
    "role": "user",
    "content": "How big is it?"
})

# Call agent
result = Runner.run_sync(agent, messages)
print(result.final_output)
