from typing import Dict
from app.game.loader import select_random_country
from app.game.state import GameState
import random


class GameEngine:
    """
    Core game engine: initializes game, runs turns, applies agent suggestions.
    """

    def __init__(self):
        # Pick a random country
        country = select_random_country()
        self.state = GameState(
            country_id=country["id"],
            country_name=country["name"],
            metrics=country["initial_metrics"]
        )

        # Save initial country info for reference
        self.country_profile = country

    def run_turn(self, agent_suggestions: Dict[str, float]):
        """
        Apply agent metric changes, advance turn, and check for failure conditions.
        """
        # Apply metric changes safely
        self.state.apply_metric_changes(agent_suggestions)

        # Check if any hard failure occurs
        self.state.check_failure_conditions()

        # Record agent evaluation (optional)
        self.state.record_agent_evaluation(agent_suggestions)

        # Advance turn if game not over
        if not self.state.is_game_over:
            self.state.advance_turn()

    def get_state(self):
        """
        Return current game state as dict
        """
        return self.state.dict()

    def is_game_over(self):
        return self.state.is_game_over


# --------------------------
# TEST BLOCK
# --------------------------
if __name__ == "__main__":
    engine = GameEngine()
    print(f"Starting game with country: {engine.state.country_name}")
    print("Initial metrics:", engine.state.metrics)

    # Simulate 3 turns with random agent suggestions
    for i in range(3):
        if engine.is_game_over():
            print("Game over!")
            break

        # Example: agents suggest random changes
        suggestions = {
            "stability": random.randint(-10, 10),
            "public_trust": random.randint(-5, 5),
            "resources": random.randint(-7, 7),
            "ethics": random.randint(-5, 5)
        }

        print(f"\nTurn {engine.state.turn} agent suggestions:", suggestions)
        engine.run_turn(suggestions)
        print("Metrics after turn:", engine.state.metrics)

    if engine.is_game_over():
        print("\nFinal outcome:", engine.state.state.outcome)
    else:
        print("\nGame not finished after 3 turns")
