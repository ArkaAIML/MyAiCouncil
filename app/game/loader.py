import json
import random
from pathlib import Path


# Path to the country profiles JSON
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "country_profiles.json"


def load_country_profiles() -> list[dict]:
    """
    Loads all country profiles from JSON file.
    """
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Country profiles file not found at {CONFIG_PATH}")

    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    if "profiles" not in data:
        raise ValueError("Invalid country_profiles.json format: missing 'profiles' key")

    return data["profiles"]


def select_random_country() -> dict:
    """
    Selects and returns one random country profile.
    """
    profiles = load_country_profiles()

    if not profiles:
        raise ValueError("No country profiles available")

    return random.choice(profiles)

if __name__ == "__main__":
    country = select_random_country()
    print(country["name"])