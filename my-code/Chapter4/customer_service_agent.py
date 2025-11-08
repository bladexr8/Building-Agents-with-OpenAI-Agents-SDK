import os
from datetime import datetime
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, StopAtTools

# Load environment variables from the .env file
load_dotenv()

# Access the API Key
api_key = os.getenv("OPENAI_API_KEY")

# Check to confirm API Key is accessible
if not api_key:
    print("ERROR: OPENAI_API_KEY not found. Please set it in your .env file")
else:
    print("API Key loaded successfully")

# Create an order status tool
@function_tool(
        name_override="get_status_of_current_order",
        description_override="Returns the status of an order given the customer's Order ID",
        docstring_style="google"
)
def get_order_status(orderID:int) -> str:
    """
    Returns the order status given an order ID
    Args:
        orderID (int) - Customer's Order ID in integer format
    Returns:
        string - Status message of the customer's order
    """
    if orderID in (100, 101):
        return "Delivered"
    elif orderID in (200, 201):
        return "Delayed"
    elif orderID in (300, 301):
        return "Cancelled"
    else:
        return "Order Not Found"
    
# Create an Invoice Tool
@function_tool
def create_invoice(orderID:int) -> str:
    """
        Generates an Invoice for a given Order ID
        Args:
            orderID(int) - Order ID of the customer's order
        Returns:
            string - Invoice for the customer's order
    """
    current_date = datetime.now().date()
    return f"Invoice for Order {orderID}: $123.45 (Generated on {current_date})"

# Define the Invoice Generator Agent
invoice_generator_agent = Agent(
    name="Invoice generator agent",
    instructions="Generate and return an invoice when requested",
    model="gpt-4o",
    tools=[create_invoice],
    tool_use_behavior=StopAtTools(stop_at_tool_names=["create_invoice"])
)

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
              handoffs=[customer_retention_agent, invoice_generator_agent])

# Run the Control Logic Framework
# result = Runner.run_sync(agent, "What is the status of my order? My Order ID is 200")
# result = Runner.run_sync(agent, "I want to cancel my order and account. You delayed my order for the 3rd time!")

# result = Runner.run_sync(invoice_generator_agent, "Create an invoice for order 123")

result = Runner.run_sync(agent, "Create an invoice for order 123")

# Print the result
print(result.final_output)