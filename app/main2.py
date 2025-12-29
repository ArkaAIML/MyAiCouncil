from fastapi import FastAPI
from app.game.state2 import GameState
from app.game.loader import select_random_country, select_random_crisis

from app.agents.stability_agent import stability_agent
from app.agents.economy_agent import economy_agent
from app.agents.ethics_agent import ethics_agent
from app.agents.public_trust_agent import public_trust_agent
import json
import re

app = FastAPI(title="MyAiCouncil")

# Global game state (single-player for now)
GAME_STATE: GameState | None = None


@app.get("/")
def root():
    return {"message": "MyAiCouncil is running"}


@app.post("/start")
def start_game():
    global GAME_STATE

    country = select_random_country()
    crisis = select_random_crisis()

    GAME_STATE = GameState(
        country=country,
        current_crisis=crisis,
        metrics=country["initial_metrics"].copy()
    )

    return {
        "country": country,
        "crisis": crisis,  # ✅ fixed
        "metrics": GAME_STATE.metrics
    }


def build_agent_prompt(state: GameState) -> str:
    """
    Converts game state into a natural language prompt for LLMs.
    """
    return f"""
You are an advisor to the government.

Country: {state.country['name']}
Crisis: {state.current_crisis['title']} - {state.current_crisis['description']}

Current Metrics:
- Stability: {state.metrics['stability']}
- Public Trust: {state.metrics['public_trust']}
- Resources: {state.metrics['resources']}
- Ethics: {state.metrics['ethics']}

Give ONE concrete policy action and briefly explain its impact.
"""

@app.get("/agents")
def get_agent_suggestions():
    if not GAME_STATE:
        return {"error": "Game not started"}

    prompt = build_agent_prompt(GAME_STATE)

    agent_map = {
        "stability": stability_agent,
        "economy": economy_agent,
        "ethics": ethics_agent,
        "public_trust": public_trust_agent,
    }

    GAME_STATE.last_agent_outputs = {}   # store internally
    visible_actions = {}                # send to player

    for key, agent in agent_map.items():
        run = agent.run(prompt)
        decision = extract_agent_decision(run.content)

        GAME_STATE.last_agent_outputs[key] = decision
        visible_actions[key] = decision["action"]

    return {
        "actions": visible_actions
    }


def extract_agent_decision(text: str) -> dict:


    if not text:
        raise ValueError("Empty agent response")

    # Remove markdown code fences
    cleaned = re.sub(r"```(?:json)?", "", text)
    cleaned = cleaned.replace("```", "").strip()

    # Extract JSON object
    match = re.search(r"\{[\s\S]*\}", cleaned)
    if not match:
        raise ValueError(f"No JSON found in agent output:\n{text}")

    json_str = match.group()

    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON from agent:\n{json_str}") from e


@app.post("/choose/{agent_key}")
def choose_action(agent_key: str):
    if not GAME_STATE:
        return {"error": "Game not started"}

    if agent_key not in GAME_STATE.last_agent_outputs:
        return {"error": "Invalid agent choice"}

    decision = GAME_STATE.last_agent_outputs[agent_key]

    for metric in ["stability", "public_trust", "resources", "ethics"]:
        GAME_STATE.metrics[metric] += decision.get(metric, 0)
        GAME_STATE.metrics[metric] = max(0, min(100, GAME_STATE.metrics[metric]))

    return {
        "chosen_action": decision["action"],
        "updated_metrics": GAME_STATE.metrics
    }
