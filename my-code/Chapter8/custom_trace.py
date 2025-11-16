# Required imports
import os
from dotenv import load_dotenv
from agents import Agent, Runner, trace
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
    result = Runner.run_sync(agent, "Where is the Eiffel Tower?")
    print(result.final_output)

