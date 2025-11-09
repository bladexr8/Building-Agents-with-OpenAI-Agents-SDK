import os
# import requests
# from datetime import datetime
from dotenv import load_dotenv
from agents import Agent, Runner, FileSearchTool
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

# instantiate the tool
filesearchtool = FileSearchTool(
    vector_store_ids=['vs_6910637da0a88191bf6c5f545fa617f9']
)

# create an agent
agent = Agent(
    name="FileTool",
    instructions="You are an AI agent that answers questions from the listed vector stores. Answer in one sentence.",
    tools=[filesearchtool]
)

result = Runner.run_sync(agent, "What is the Product Code for a Cyan Cartridge?")
print(result.final_output)
