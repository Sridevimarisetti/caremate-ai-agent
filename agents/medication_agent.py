from google.adk.agents import Agent

medication_agent = Agent(
    name="medication_agent",
    model="gemini-2.0-flash",
    description="Handles medication reminders and schedules.",
    instruction="""
    Help users manage medications,
    dosage schedules,
    refill reminders,
    and medication tracking.
    """
)
