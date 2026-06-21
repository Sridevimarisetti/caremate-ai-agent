from google.adk.agents import Agent

orchestrator = Agent(
    name="caremate_orchestrator",
    model="gemini-2.0-flash",
    description="Routes family health requests to specialized agents.",
    instruction="""
    You are the CareMate AI orchestrator.
    Route requests related to:
    - Medications
    - Appointments
    - Wellness check-ins
    - Emergency alerts
    """
)
