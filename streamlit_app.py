import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="MyAiCouncil",
    layout="centered"
)

st.title("🧠 MyAiCouncil")


if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "agents" not in st.session_state:
    st.session_state.agents = {}

if "metrics" not in st.session_state:
    st.session_state.metrics = {}


if not st.session_state.game_started:
    if st.button("🎮 Start Game"):
        res = requests.post(f"{API_BASE}/start")
        data = res.json()

        st.session_state.country = data["country"]
        st.session_state.crisis = data["crisis"]
        st.session_state.metrics = data["metrics"]
        st.session_state.game_started = True

        agents_res = requests.get(f"{API_BASE}/agents")
        st.session_state.agents = agents_res.json()["actions"]  # ✅ FIX

        st.rerun()


if st.session_state.game_started:

    country = st.session_state.country
    crisis = st.session_state.crisis
    metrics = st.session_state.metrics
    agents = st.session_state.agents

    st.subheader(country["name"])
    st.write(country["description"])

    st.divider()

    st.subheader("🚨 Crisis")
    st.write(f"**{crisis['title']}**")
    st.write(crisis["description"])

    st.divider()

    st.subheader("📊 Current Metrics")
    cols = st.columns(4)
    cols[0].metric("Stability", metrics["stability"])
    cols[1].metric("Public Trust", metrics["public_trust"])
    cols[2].metric("Resources", metrics["resources"])
    cols[3].metric("Ethics", metrics["ethics"])

    st.divider()

    st.subheader("🏛️ Council Advice")
    st.caption("Choose ONE policy to implement")

    for agent_key, action_text in agents.items():
        with st.container(border=True):
            st.write(action_text)

            if st.button("Choose this action", key=agent_key):
                choose_res = requests.post(
                    f"{API_BASE}/choose/{agent_key}"
                )

                result = choose_res.json()
                st.session_state.metrics = result["updated_metrics"]  # ✅ FIX

                st.success("Policy implemented")
                st.rerun()
