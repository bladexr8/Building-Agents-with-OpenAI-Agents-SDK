import os
import requests
# from datetime import datetime
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool
from pydantic import BaseModel
from typing import List

# Pydantic class to validate input to tool
class Crypto(BaseModel):
    """
    coin_ids: full name string to represent cryptocurrency
    """
    coin_ids: List[str]

# Load environment variables from the .env file
load_dotenv()

# Access the API Key
api_key = os.getenv("OPENAI_API_KEY")

# Check to confirm API Key is accessible
if not api_key:
    print("FATAL ERROR: OPENAI_API_KEY not found. Please set it in your .env file")
    exit(-1)

# Create the tools
@function_tool
def get_price_of_bitcoin() -> str:
    """ Get the price of Bitcoin."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    price = response.json()["bitcoin"]["usd"]
    return f"${price:,.2f} USD."

@function_tool
def get_crypto_prices(crypto: Crypto) -> str:
    """
    Get the current prices of a list of cryptocurrencies
    Args:
        crypto: an object with a list of coin_ids (e.g. bitcoin, ethereum, litecoin, etc)
    """
    ids = ",".join(crypto.coin_ids)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data

# Create the agent
crypto_agent = Agent(
    name="CryptoTracker",
    instructions="You are a crypto assistant. Use tools to get real-time data. When getting cryptocurrecny prices, call the tool only once for all requests",
    tools=[get_price_of_bitcoin, get_crypto_prices]
)

# Run the agent with an example prompt
# result = Runner.run_sync(crypto_agent, "What's the price of Bitcoin?")
result = Runner.run_sync(crypto_agent, "What's the price of Bitcoin and Ethereum?")

print(result.final_output)

