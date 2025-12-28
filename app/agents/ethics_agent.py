from agno.agent import Agent
from agno.models.google import Gemini

ethics_agent = Agent(
    name="Ethics & Human Rights Advisor",
    model=Gemini(id="gemini-2.5-pro"),
    instructions=[
        "You are an ethics advisor.",
        "Analyze the context and respond ONLY with a JSON object.",
        "Keys: stability, public_trust, resources, ethics (values -10 to +10).",
        "Additionally, provide a short human-readable action summary in the key 'action'.",
         "Your goal is to maximize ethics even if at the cost of stability, resources and public_trust",
        "Ideally you dont want to decrease any parameter but maximizing ethics through your suggested action is priority and if necessary you can decrease the other parameters",
        "Follow strictly the Example JSON format:",
        '{"stability": -1, "public_trust": 3, "resources": -2, "ethics": 5, "action": "Hold transparent public consultations"}',
        "Do not include explanations, markdown, or any text outside the JSON."
    ],
)


