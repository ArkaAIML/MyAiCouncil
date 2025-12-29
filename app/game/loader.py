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



CRISES = [
    {
        "title": "Economic Collapse",
        "description": "Inflation is rising rapidly, unemployment is high, and public anger is growing."
    },
    {
        "title": "Border Conflict",
        "description": "A neighboring nation has mobilized troops near the border, raising fears of war."
    },
    {
        "title": "Energy Shortage",
        "description": "Fuel reserves are critically low, causing power outages nationwide."
    },
    {
        "title": "Civil Unrest",
        "description": "Mass protests have erupted after allegations of government corruption."
    },
    {
        "title": "Pandemic Outbreak",
        "description": "A fast-spreading disease threatens public health and economic stability."
    }
]


def select_random_crisis():
    return random.choice(CRISES)


if __name__ == "__main__":
    country = select_random_country()
    print(country["name"])

    crisis = select_random_crisis()
    print(crisis["title"])
