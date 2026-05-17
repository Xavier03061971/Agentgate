import streamlit as st

st.set_page_config(page_title="AgentGate", layout="wide")

st.title("AgentGate")
st.subheader("AI Agent Governance Layer")

st.markdown("### Decision Engine")

action = st.selectbox(
    "Select action",
    [
        "send_email",
        "delete_data",
        "read_data",
        "permission_change"
    ]
)

if st.button("Run Inspection"):

    if action == "read_data":
        decision = "ALLOW"
        risk = 0.03
        color = "green"

    elif action == "send_email":
        decision = "REVIEW"
        risk = 0.31
        color = "orange"

    else:
        decision = "BLOCK"
        risk = 0.82
        color = "red"

    st.markdown(f"## :{color}[{decision}]")
    st.metric("Risk Score", risk)

    st.success("Inspection completed.")