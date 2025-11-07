import os
from dotenv import load_dotenv
from agents import Agent, Runner

# Load environment variables from the .env file
load_dotenv()

# Access the API Key
api_key = os.getenv("OPENAI_API_KEY")

# Check to confirm API Key is accessible
if not api_key:
    print("ERROR: OPENAI_API_KEY not found. Please set it in your .env file")
else:
    print("API Key loaded successfully")

# Create an Agent and run it
agent = Agent(name="Customer Service Agent", instructions="You are an AI Agent that helps respond to customer queries for a local paper company", model="gpt-4o")

# Run the Control Logic Framework
result = Runner.run_sync(agent, "How do I cancel my order?")

# Print the result
print(result.final_output)