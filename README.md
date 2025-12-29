MyAiCouncil
===========

A single-player, policy-decision simulation game powered by multiple AI advisors.  
The player governs a fictional country through crises by choosing between competing policy recommendations, each affecting national metrics such as stability, public trust, resources, and ethics.

---

Core Concept
------------

**MyAiCouncil** simulates decision-making under uncertainty.

- The player represents the head of government.
- A country and an initial crisis are generated at the start.
- Multiple AI advisor agents independently propose one concrete policy action.
- Each action affects national metrics positively and negatively.
- The player selects exactly one action per round.
- Metrics update internally and determine success or failure.

The system emphasizes trade-offs, ethical dilemmas, and long-term consequences rather than optimal play.

---

Gameplay Overview
-----------------

1. Start a new game
2. Receive:
   - Country profile
   - Initial crisis
   - Starting metrics
3. Consult the AI council
4. Choose exactly one policy action
5. Metrics update
6. (Future) Proceed to next round or end condition

---

Game Metrics
------------

Each decision affects four core metrics:

| Metric        | Description |
|--------------|-------------|
| Stability    | Internal order, unrest, and political control |
| Public Trust | Citizen confidence in government legitimacy |
| Resources    | Economic strength and material capacity |
| Ethics       | Human rights, fairness, and moral governance |

All metrics are bounded between **0 and 100**.

---

AI Advisor Agents
-----------------

Each advisor represents a distinct governing priority and operates independently.

| Agent | Focus Area | Typical Bias |
|------|------------|--------------|
| Stability Advisor | Law, order, control | Authoritarian tendencies |
| Economy Advisor | Growth, efficiency | Resource-heavy trade-offs |
| Ethics Advisor | Human rights, fairness | High moral cost tolerance |
| Public Trust Advisor | Legitimacy, perception | Popular but risky decisions |

Agents receive the same game state but produce different recommendations.

---

System Architecture
-------------------

The system follows a clean separation between frontend, backend, and AI logic.

┌──────────────────────┐
│ Streamlit UI │
│ (Player Interface) │
└──────────┬───────────┘
│ HTTP Requests
▼
┌──────────────────────┐
│ FastAPI Backend │
│ │
│ - Game State │
│ - API Endpoints │
│ - Decision Logic │
└──────────┬───────────┘
│ Prompts
▼
┌──────────────────────┐
│ AI Advisor Agents │
│ │
│ - Stability Agent │
│ - Economy Agent │
│ - Ethics Agent │
│ - Trust Agent │
└──────────────────────┘



---

Project Structure
-----------------

MyAiCouncil/
│
├── app/
│ ├── agents/
│ │ ├── stability_agent.py
│ │ ├── economy_agent.py
│ │ ├── ethics_agent.py
│ │ └── public_trust_agent.py
│ │
│ ├── game/
│ │ ├── loader.py
│ │ ├── state2.py
│ │ └── engine2.py
│ │
│ └── main2.py
│
├── streamlit_app.py
├── README.md
└── requirements.txt



---

API Endpoints
-------------

### Start Game
POST /start



Initializes a new game session.

Response:
```json
{
  "country": {},
  "crisis": {},
  "metrics": {}
}
Get Advisor Actions

GET /agents
Returns player-friendly policy actions only.

Response:



{
  "actions": {
    "stability": "Action text...",
    "economy": "Action text...",
    "ethics": "Action text...",
    "public_trust": "Action text..."
  }
}
Choose Action

POST /choose/{agent_key}
Applies the selected advisor’s decision.

Response:


{
  "chosen_action": "...",
  "updated_metrics": {}
}
Frontend
The frontend is implemented using Streamlit.

Displays country, crisis, and metrics

Shows only human-readable actions

Allows selection of one policy per round

Updates metrics after decision

The frontend does not expose:

Raw agent JSON

Internal metric deltas

Prompt engineering logic

Environment Variables
The backend requires an API key for the LLM provider.

Example:


export GOOGLE_API_KEY=your_api_key_here
The frontend does not require an API key.

Future Roadmap
Multi-round gameplay with fixed turn limit

Win / loss conditions based on metric thresholds

Persistent session storage

Difficulty presets

Visual analytics for metric trends

Multiplayer or observer mode

Design Philosophy
Decisions should never be strictly optimal

Every action has hidden costs

Ethical choices may weaken power

Powerful choices may erode legitimacy

The game is designed to force uncomfortable trade-offs, not reward min-maxing.

License
For educational and experimental purposes.





