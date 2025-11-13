import os
from dotenv import load_dotenv
from dataclasses import dataclass
from agents import Agent, Runner, RunContextWrapper, function_tool
# from pydantic import BaseModel
# from typing import List

# Load environment variables from the .env file
load_dotenv()

# Access the API Key
api_key = os.getenv("OPENAI_API_KEY")



