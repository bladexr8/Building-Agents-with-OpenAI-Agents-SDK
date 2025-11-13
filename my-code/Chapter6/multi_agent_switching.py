import os
from dotenv import load_dotenv
from agents import Agent, Runner, SQLiteSession, trace
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
    instructions="Introduce yourself as the complaints agent. Handle any customer complaints with empathy and clear next steps."
)

sales_agent = Agent(
    name="Sales Agent",
    instructions="Introduce yourself as the sales agent. Answer general questions about our services promptly."
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="Answer general questions. Triage the user's request and call the appropriate agent"
)

# Handoff all agents with each other
complaints_agent.handoffs = [sales_agent, triage_agent]
sales_agent.handoffs = [complaints_agent, triage_agent]
triage_agent.handoffs = [complaints_agent, sales_agent]


# Create a session
session = SQLiteSession("first_session")
last_agent = triage_agent
with trace("Multi-agent system"):
    while True:
        question = input("You: ")
        result = Runner.run_sync(last_agent, question, session=session)
        print("Agent: ", result.final_output)
        last_agent = result.last_agent
    