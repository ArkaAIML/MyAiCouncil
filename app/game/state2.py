from pydantic import BaseModel
from typing import Dict, Optional

class GameState(BaseModel):
    country: Dict
    current_crisis: Dict
    metrics: Dict[str, int]
    turn: int = 1

    last_agent_outputs: Optional[Dict[str, Dict]] = None
