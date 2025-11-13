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

# Create Agents
complaints_agent = Agent(
    name="Complaints Agent",
    instructions="Handle any customer complaints with empathy and clear next steps."
)

inquiry_agent = Agent(
    name="General Inquiry Agent",
    instructions="Answer general questions about our services promptly."
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="Triage the user's request and call the appropriate agent",
    handoffs=[
        complaints_agent,
        inquiry_agent
    ]
)

while True:
    question = input("You: ")
    result = Runner.run_sync(triage_agent, question)
    print("Agent: ", result.final_output)
    