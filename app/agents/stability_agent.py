# app/agents/stability_agent.py
from agno.agent import Agent
from agno.models.google import Gemini

print("Loading stability_agent module...")
gemini_model = Gemini(id="gemini-1.5-flash")


stability_agent = Agent(
    name="Stability Advisor",
    model=gemini_model,
    instructions=[
        "You are a national security advisor.",
        "Analyze the context and respond ONLY with a JSON object.",
        "Keys: stability, public_trust, resources, ethics (values -10 to +10).",
        "Do not include any prose or markdown backticks."
    ],
    markdown=True,
    
)

print("stability_agent variable created successfully")
