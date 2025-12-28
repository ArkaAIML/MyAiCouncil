# app/game/engine.py

from typing import Dict, List
from app.game.state2 import GameState
from app.agents.stability_agent import stability_agent
from app.agents.economy_agent import economy_agent
from app.agents.ethics_agent import ethics_agent
from app.agents.public_trust_agent import public_trust_agent


AGENTS = {
    "stability": stability_agent,
    "economy": economy_agent,
    "ethics": ethics_agent,
    "security": public_trust_agent,
}


class GameEngine:
    def __init__(self, state: GameState):
        self.state = state

    def build_context(self) -> str:
        """Create shared context for all agents"""
        return f"""
Country: {self.state.country}
Crisis: {self.state.crisis}

Current metrics:
- Stability: {self.state.stability}
- Economy: {self.state.economy}
- Public Trust: {self.state.public_trust}
- Ethics: {self.state.ethics}

Turn: {self.state.turn}
"""

    def get_agent_actions(self) -> List[Dict]:
        """
        Ask each agent for an action.
        Returns a list of action objects (safe for UI).
        """
        context = self.build_context()
        actions = []

        for role, agent in AGENTS.items():
            response = agent.run(context)

            if not hasattr(response, "content"):
                continue

            action = response.content
            action["agent"] = role
            actions.append(action)

        return actions

    def apply_action(self, action: Dict):
        """
        Apply metric changes from the chosen action.
        """
        self.state.stability += action.get("stability", 0)
        self.state.economy += action.get("economy", 0)
        self.state.public_trust += action.get("public_trust", 0)
        self.state.ethics += action.get("ethics", 0)

        # clamp values between 0 and 100
        self.state.stability = max(0, min(100, self.state.stability))
        self.state.economy = max(0, min(100, self.state.economy))
        self.state.public_trust = max(0, min(100, self.state.public_trust))
        self.state.ethics = max(0, min(100, self.state.ethics))

        self.state.turn += 1
