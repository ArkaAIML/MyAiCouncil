from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from app.game.engine import GameEngine

app = FastAPI(title="Council of Minds Prototype")

# ----------------------
# In-memory single game instance
# ----------------------
engine: GameEngine = None  # Will be initialized when a game starts

# ----------------------
# Request Model for agent suggestions
# ----------------------
class AgentSuggestions(BaseModel):
    stability: int = 0
    public_trust: int = 0
    resources: int = 0
    ethics: int = 0


# ----------------------
# Endpoint: Start Game
# ----------------------
@app.post("/start_game")
def start_game():
    global engine
    engine = GameEngine()
    return {
        "message": "Game started",
        "country": engine.state.country_name,
        "metrics": engine.state.metrics,
        "turn": engine.state.turn,
        "max_turns": engine.state.max_turns
    }


# ----------------------
# Endpoint: Run Next Turn
# ----------------------
@app.post("/next_turn")
def next_turn(suggestions: AgentSuggestions):
    global engine
    if engine is None:
        raise HTTPException(status_code=400, detail="Game not started. Call /start_game first.")

    if engine.is_game_over():
        return {
            "message": "Game over",
            "outcome": engine.state.outcome,
            "metrics": engine.state.metrics
        }

    # Convert suggestions to dict
    agent_changes: Dict[str, int] = suggestions.dict()

    # Run one turn
    engine.run_turn(agent_changes)

    # Prepare response
    response = {
        "metrics": engine.state.metrics,
        "turn": engine.state.turn,
        "is_game_over": engine.state.is_game_over,
        "outcome": engine.state.outcome
    }

    return response


# ----------------------
# Optional: Get Current State
# ----------------------
@app.get("/get_state")
def get_state():
    global engine
    if engine is None:
        raise HTTPException(status_code=400, detail="Game not started. Call /start_game first.")

    return {
        "country": engine.state.country_name,
        "metrics": engine.state.metrics,
        "turn": engine.state.turn,
        "is_game_over": engine.state.is_game_over,
        "outcome": engine.state.outcome
    }