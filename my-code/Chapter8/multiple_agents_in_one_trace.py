# Required imports
import os
from dotenv import load_dotenv
from agents import Agent, Runner, trace, custom_span
import time
# from pydantic import BaseModel
# Load environment variables from the .env file
load_dotenv()
# Access the API key
# api_key = os.getenv("OPENAI_API_KEY")

# Create an agent
agent = Agent(
    name="QuestionAnswerAgent",
    instructions="You are an AI agent that answers questions in as few words as possible"
)

with trace("Henry's Workflow"):
    with custom_span("Task 1"):
        result = Runner.run_sync(agent, "Where is the Statue of Liberty?")
    with custom_span("Task 2"):
        result = Runner.run_sync(agent, "Where is the Eiffel Tower?")
    with custom_span("Task 3"):
        result = Runner.run_sync(agent, "Where is the Notre Dame?")
    with custom_span("Task 4"):
        result = Runner.run_sync(agent, "Where is the Burj Khalifa?")