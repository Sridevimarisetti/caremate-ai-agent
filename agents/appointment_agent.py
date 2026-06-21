from google.adk.agents import Agent

appointment_agent = Agent(
    name="appointment_agent",
    model="gemini-2.0-flash",
    description="Handles doctor appointments and scheduling.",
    instruction="""
    Help users schedule, track,
    and manage medical appointments.
    Provide appointment reminders.
    """
)
