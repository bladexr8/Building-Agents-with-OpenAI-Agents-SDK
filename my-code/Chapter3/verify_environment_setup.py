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
agent = Agent(name="Echo Agent", instructions="Return the words 'Setup Successful'")
result = Runner.run_sync(agent, "Run setup")
print(result.final_output)
