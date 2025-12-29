# MyAiCouncil
=================

## Overview
-----------
**MyAiCouncil** is a single-player, AI-driven policy simulation game where the user acts as a head of state during a national crisis.  
Multiple AI agents represent different advisory perspectives (stability, economy, ethics, public trust).  
The player must choose one policy action per round and survive by keeping national metrics above critical thresholds.

This project is designed as a **demo-ready AI systems showcase**, combining:
- Multi-agent reasoning
- Structured LLM outputs
- Game state management
- Backend–frontend separation


## Core Concept
-------------
Each turn:
1. A crisis is presented
2. AI advisors independently propose one policy
3. The player selects **one** action
4. National metrics update internally
5. The game progresses toward success or failure


## Game Metrics
--------------
| Metric        | Description |
|--------------|-------------|
| Stability     | Internal order and governance strength |
| Public Trust  | Citizen confidence in leadership |
| Resources     | Economic and material capacity |
| Ethics        | Moral and humanitarian standing |

All metrics are constrained between **0 and 100**.


## AI Advisors
--------------
Each advisor is an autonomous agent with a specific value system.

| Agent | Focus |
|------|-------|
| Stability Agent | Law, order, control |
| Economy Agent | Growth, capital, efficiency |
| Ethics Agent | Human rights, fairness |
| Public Trust Agent | Popular support and morale |

Each agent returns:
- A single recommended action
- Hidden metric deltas (applied only after selection)


## Architecture
--------------
User (Streamlit UI)
|
v
FastAPI Backend
|
|-- Game State Manager
|
|-- Stability Agent
|-- Economy Agent
|-- Ethics Agent
|-- Public Trust Agent
|
v
LLM Provider (via Agno)


- Frontend never sees raw agent JSON
- Backend stores full agent decisions internally
- Only human-readable actions are exposed


## API Endpoints
---------------
### Start Game


POST /start

Initializes country, crisis, and metrics.

### Get Agent Advice


GET /agents

Returns:


{
"actions": {
"stability": "Action text...",
"economy": "Action text...",
"ethics": "Action text...",
"public_trust": "Action text..."
}
}


### Choose Action


POST /choose/{agent_key}

Applies hidden metric changes and returns updated state.


## Frontend
----------
The Streamlit frontend:
- Displays country profile and crisis
- Shows current metrics visually
- Presents advisor actions as selectable policies
- Updates metrics immediately after selection

The frontend **never requires an API key**.


## Environment Setup
-------------------
### Backend
- Python 3.10+
- FastAPI
- Agno
- Uvicorn

Set environment variable:


OPENAI_API_KEY=your_key_here


### Frontend
- Streamlit
- Requests

No secrets required.


## Game Rules (Current Scope)
-----------------------------
- Single round demo
- One action may be chosen
- Metrics update once
- Designed for extension into multi-round survival mode


## Planned Extensions
---------------------
- Fixed multi-round gameplay (win if all metrics > 18)
- End-state evaluation
- Difficulty scaling
- Persistent session storage
- Agent personality drift


## Purpose
---------
This project demonstrates:
- Practical multi-agent orchestration
- Clean LLM output parsing
- Real-time decision impact simulation
- Production-style backend/frontend separation

It is suitable for:
- AI system demos
- Hackathons
- Portfolio projects
- Academic presentations



