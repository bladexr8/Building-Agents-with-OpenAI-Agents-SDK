import os
# import requests
# from datetime import datetime
from dotenv import load_dotenv
from agents import Agent, Runner, WebSearchTool
from pydantic import BaseModel
from typing import List

# Load environment variables from the .env file
load_dotenv()

# Access the API Key
api_key = os.getenv("OPENAI_API_KEY")

# Check to confirm API Key is accessible
if not api_key:
    print("FATAL ERROR: OPENAI_API_KEY not found. Please set it in your .env file")
    exit(-1)

# Instantiate the tool
websearchtool = WebSearchTool()
# Create an agent
agent = Agent(
    name="WebTool",
    instructions="You are an AI agent that answers web questions. Answer in one sentence.",
    tools=[websearchtool]
)
result = Runner.run_sync(agent, "Who won the 2025 Stanley Cup?")
print(result.final_output)
