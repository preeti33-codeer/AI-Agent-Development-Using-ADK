from google.adk import Agent


root_agent = Agent(
    name="agent1",
    model="gemini-2.0-flash",
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user.
    Ask for the user's name and greet them by name.
    """
)

__all__ = ["root_agent"]

