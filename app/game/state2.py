from pydantic import BaseModel
from typing import Dict

class GameState(BaseModel):
    country: Dict               # full country profile dict
    current_crisis: Dict        # current crisis dict
    metrics: Dict               # {"stability": 50, "public_trust": 50, "resources": 50, "ethics": 50}
    turn: int = 1
