from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.game.loader import select_random_country, select_random_crisis
from app.game.state2 import GameState
from agno.agents import load_agent
from agno.schema import Message

app = FastAPI()

# Initialize agents
agents = {
    "stability_agent": load_agent("stability-advisor"),
    "economy_agent": load_agent("economy-advisor"),
    "ethics_agent": load_agent("ethics-&-human-rights-advisor"),
    "public_trust_agent": load_agent("public-sentiment-&-legitimacy-advisor")
}

# In-memory game state
game_state: GameState | None = None

@app.post("/start")
async def start_game():
    global game_state
    country = select_random_country()
    crisis = select_random_crisis()

    # Initialize metrics with the country's initial metrics
    metrics = country.get("initial_metrics", {
        "stability": 50,
        "public_trust": 50,
        "resources": 50,
        "ethics": 50
    })

    game_state = GameState(
        country=country["name"], 
        current_crisis=crisis,
        metrics=metrics
    )

    return JSONResponse(content={
        "country": country,
        "crisis": crisis,
        "metrics": metrics
    })


@app.get("/agents")
async def get_agent_suggestions():
    global game_state
    if not game_state:
        return JSONResponse(content={"error": "Game not started"}, status_code=400)

    suggestions = {}

    # Wrap metrics into a Message for each agent
    for name, agent in agents.items():
        user_msg = Message(
            role="user",
            content=f"Current metrics: {game_state.metrics}. Provide your advice."
        )

        try:
            run_output = agent.run([user_msg])
            # Extract content safely
            suggestions[name] = run_output.content if run_output and run_output.content else "No advice generated"
        except Exception as e:
            suggestions[name] = f"Error: {str(e)}"

    return JSONResponse(content=suggestions)
