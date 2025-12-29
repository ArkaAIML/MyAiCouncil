#MyAiCouncil

MyAiCouncil is an interactive, AI-driven governance simulation where multiple specialized AI advisors propose policy actions during national crises — and the player must choose wisely to keep the nation stable.
Instead of a single AI making decisions, MyAiCouncil models a council of competing advisors, each optimizing for a different priority such as stability, economy, ethics, or public trust.

##🎯 Core Idea

Real-world governance is not about one “correct” decision — it’s about trade-offs.

In MyAiCouncil:

Each AI agent represents a policy lens

Every suggested action helps some metrics and harms others

The player must balance competing advice to survive the crisis

##🧠 Advisor Agents

Each round, four independent AI agents analyze the same situation:

Agent	Focus
🛡️ Stability Advisor	Law, order, internal security
💰 Economy Advisor	Resources, industry, financial survival
⚖️ Ethics & Human Rights Advisor	Civil liberties, fairness, moral governance
🗳️ Public Trust Advisor	Legitimacy, popularity, social cohesion

Each agent proposes one concrete policy action along with its impact on national metrics.

##📊 Game Metrics

The nation is governed through four core metrics:

Stability

Public Trust

Resources

Ethics

Each decision modifies these values positively or negatively.
Metrics are internally clamped between 0–100.

##🕹️ Current Gameplay Flow (Demo Version)

Start a new game

A country profile is randomly selected

A national crisis is triggered

AI advisors propose policy actions

The player chooses one action

National metrics update accordingly

(Multi-round survival gameplay is planned but not yet implemented)

##🏗️ Project Architecture
MyAiCouncil/
│
├── app/
│   ├── agents/               # Individual AI advisors
│   │   ├── stability_agent.py
│   │   ├── economy_agent.py
│   │   ├── ethics_agent.py
│   │   └── public_trust_agent.py
│   │
│   ├── game/
│   │   ├── loader.py          # Loads countries & crises
│   │   ├── state2.py          # Game state model
│   │   └── engine2.py         # Game logic (current version)
│   │
│   └── main2.py               # FastAPI backend
│
├── frontend/
│   └── streamlit_app.py       # Streamlit UI (WIP)
│
├── config/
│   └── country_profiles.json
│
└── README.md

##🔌 Backend API (FastAPI)
Endpoint	Method	Description
/start	POST	Start a new game
/agents	GET	Get advisor policy suggestions
/choose/{agent_key}	POST	Choose an advisor’s action

Swagger UI is available at:

http://127.0.0.1:8000/docs

##🖥️ Frontend (Streamlit)

A simple Streamlit frontend is included to:

display the country and crisis

show advisor-recommended actions

allow the player to choose a policy

⚠️ The frontend is functional but still under refinement.

##🚀 How to Run Locally
1️⃣ Backend
uvicorn app.main2:app --reload

2️⃣ Frontend
streamlit run frontend/streamlit_app.py

##🔐 Environment Variables

The AI agents require an API key for the underlying LLM provider.

Create a .env file:

GOOGLE_API_KEY=your_api_key_here


The backend reads the API key — the frontend does not need direct access.

##🧭 Roadmap

Planned improvements:

Multi-round gameplay (fixed number of turns)

Win/Loss conditions based on metrics

Better UI feedback and animations

Agent disagreement visualization

Persistent game sessions

##🧑‍💻 Author

Built by Arka Banerjee
Computer Science & Engineering (AI/ML)

##📜 License

This project is for educational and demonstration purposes.
