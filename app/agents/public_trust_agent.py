
from agno.agent import Agent
from agno.models.google import Gemini
public_trust_agent = Agent(
    name="Public Sentiment & Legitimacy Advisor",
    model=Gemini(id="gemini-2.5-pro"),
    instructions=[
        "You are a public relations advisor.",
        "Analyze the context and respond ONLY with a JSON object.",
        "Your goal is to maximize public_trust even if at the cost of stability, resources and ethics",
        "Ideally you dont want to decrease any parameter but maximizing public trust through your suggested action is priority and if necessary you can decrease the other parameters",
        "Keys: stability, public_trust, resources, ethics (values -10 to +10).",
        "Additionally, provide a short human-readable action summary in the key 'action'.",
        "Follow strictly the Example JSON format:",
        '{"stability": 1, "public_trust": 5, "resources": -1, "ethics": 2, "action": "Make a public apology and promise policy changes"}',
        "Do not include explanations, markdown, or any text outside the JSON."
    ],
)

