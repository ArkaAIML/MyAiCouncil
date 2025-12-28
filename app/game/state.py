from pydantic import BaseModel, Field
from typing import Dict, List, Optional


class GameState(BaseModel):
    # Identity
    country_id: str
    country_name: str

    # Core game tracking
    turn: int = 1
    max_turns: int = 10
    is_game_over: bool = False
    outcome: Optional[str] = None

    # Metrics (dynamic & extensible)
    metrics: Dict[str, float]

    # History
    decision_history: List[Dict] = Field(default_factory=list)
    agent_evaluations: List[Dict] = Field(default_factory=list)

    def apply_metric_changes(self, changes: Dict[str, float]):
        for key, delta in changes.items():
            current = self.metrics.get(key, 50)
            new_value = max(0, min(100, current + delta))
            self.metrics[key] = new_value

    def advance_turn(self):
        if self.turn >= self.max_turns:
            self.is_game_over = True
        else:
            self.turn += 1

    def check_failure_conditions(self):
        if self.metrics.get("stability", 100) <= 0:
            self.is_game_over = True
            self.outcome = "State collapse due to instability"
        elif self.metrics.get("public_trust", 100) <= 0:
            self.is_game_over = True
            self.outcome = "Government lost all public trust"

    def record_decision(self, decision: Dict):
        self.decision_history.append(decision)

    def record_agent_evaluation(self, evaluation: Dict):
        self.agent_evaluations.append(evaluation)


# --------------------------
# TEST BLOCK (OUTSIDE CLASS)
# --------------------------
if __name__ == "__main__":
    state = GameState(
        country_id="AURELIA",
        country_name="Republic of Aurelia",
        metrics={
            "stability": 50,
            "public_trust": 65,
            "resources": 55,
            "ethics": 70
        }
    )

    state.apply_metric_changes({"stability": -60})
    state.check_failure_conditions()
    print(state.is_game_over, state.outcome)
