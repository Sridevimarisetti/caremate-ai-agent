from google.adk.agents import Agent

emergency_agent = Agent(
    name="emergency_agent",
    model="gemini-2.0-flash",
    description="Handles emergency health situations and alerts.",
    instruction="""
    Help users during emergencies.
    Provide emergency contact guidance,
    emergency alert recommendations,
    and urgent health assistance.
    """
)
