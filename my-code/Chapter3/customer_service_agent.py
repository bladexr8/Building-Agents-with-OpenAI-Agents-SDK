import os
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool

# Load environment variables from the .env file
load_dotenv()

# Access the API Key
api_key = os.getenv("OPENAI_API_KEY")

# Check to confirm API Key is accessible
if not api_key:
    print("ERROR: OPENAI_API_KEY not found. Please set it in your .env file")
else:
    print("API Key loaded successfully")

# Create a tool
@function_tool
def get_order_status(orderID:int) -> str:
    """
    Returns the order status given an order ID
    """
    if orderID in (100, 101):
        return "Delivered"
    elif orderID in (200, 201):
        return "Delayed"
    elif orderID in (300, 301):
        return "Cancelled"
    else:
        return "Order Not Found"

# Define the customer retention agent
customer_retention_agent = Agent(
    name="Customer Retention Agent",
    instructions="You are an AI agent that responds to customers that want to close their accounts and retains their business. Be very courteous, relatable and kind. Offer discounts up to 10 percent if it helps",
    model="gpt-4.1"
)

# Create an Agent and run it
agent = Agent(name="Customer Service Agent", 
              instructions="You are an AI Agent that helps respond to customer queries for a local paper company", 
              model="gpt-4o",
              tools=[get_order_status],
              handoffs=[customer_retention_agent])

# Run the Control Logic Framework
# result = Runner.run_sync(agent, "What is the status of my order? My Order ID is 200")
result = Runner.run_sync(agent, "I want to cancel my order and account. You delayed my order for the 3rd time!")

# Print the result
print(result.final_output)