import os
from dotenv import load_dotenv
from agents import Agent, Runner, SQLiteSession, FileSearchTool
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

# Instantiate the tool
filesearchtool = FileSearchTool(
    vector_store_ids=['vs_6911c5f9e87c8191a60ebeb7e9ff648e']
)

# Create an agent
agent = Agent(
    name="USConstitutionTool",
    instructions="You are an AI agent that answers questions from the listed vector store, which has the US Constitution. Answer in one sentence.",
    tools=[filesearchtool]
)
# Create a session
session = SQLiteSession("first_session")
while True:
    question = input("You: ")
    result = Runner.run_sync(agent, question, session=session)
    print("Agent: ", result.final_output)