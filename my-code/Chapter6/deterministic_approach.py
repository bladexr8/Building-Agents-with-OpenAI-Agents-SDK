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

# Create two agents
complaints_agent = Agent(
    name="Complaints Agent",
    instructions="Handle any customer complaints with empathy and clear next steps."
)
inquiry_agent = Agent(
    name="General Inquiry Agent",
    instructions="Answer general questions about our services promptly."
)

# Create orchestration
def orchestrate(user_message:str):
    # Deterministically delegates requests to the right customer service agent
    if ("complaint" in user_message.lower() or "problem" in user_message.lower()):
        print("Redirecting you to the Complaints agent")
        chosen_agent = complaints_agent
    else:
        print("Redirecting you to the inquiry agent")
        chosen_agent = inquiry_agent
    result = Runner.run_sync(chosen_agent, user_message)
    return result.final_output

while True:
    question = input("You: ")
    result = orchestrate(question)
    print("Agent: ", result)