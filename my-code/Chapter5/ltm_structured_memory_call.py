import os
import json
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool
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

# Create the JSON file if it does not exist
FILENAME = 'memory.json'
memory_default = {
    "user_profile": [],
    "order_preferences": [],
    "other": []
}
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w') as f:
        json.dump(memory_default, f, indent=4)
        print(f"Created '{FILENAME}' with default data.")
else:
    print(f"'{FILENAME}' already exists. ")

@function_tool
def save_memory(memory_type:str, memory:str) -> str:
    """
    Saves a memory to a memory store
    Args:
        memory_type: the type of memory to store. Choose between user_profile, order_preferences, or other
        memory: the memory to save
    """
    with open(FILENAME, 'r') as f:
        data = json.load(f)
        data[memory_type].append(memory)

    with open(FILENAME, 'w') as f:
        json.dump(data, f, indent=4)
        print(f"Memory ({memory}) saved")
        return f"Memory ({memory}) saved"
    
@function_tool
def load_memory(memory_type:str) -> str:
    """
    Loads a set of memory from a memory store
    Args:
        memory_type: the type of memory to load. Choose between user_profile, order_preferences, or other
    """
    with open(FILENAME, 'r') as f:
        data = json.load(f)
        return "|".join(data[memory_type])
    
# Create the agent
agent = Agent(
    name="QuestionAnswer",
    instructions="You are an AI agent that answers questions. You have access to two tools that enable you to save memories and load memories. Save memories when you learn an important fact. Load memories when something is asked for about the user.",
    tools=[save_memory, load_memory]
)

while True:
    question = input("You: ")
    result = Runner.run_sync(agent, question)
    print("Agent: ", result.final_output)