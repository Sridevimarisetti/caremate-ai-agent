from google.adk.agents import Agent

wellness_agent = Agent(
    name="wellness_agent",
    model="gemini-2.0-flash",
    description="Handles wellness check-ins and health monitoring.",
    instruction="""
    Help users track wellness,
    daily health check-ins,
    exercise reminders,
    hydration and wellbeing.
    """
)
