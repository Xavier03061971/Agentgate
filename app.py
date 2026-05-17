import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(
    page_title="AgentGate Enterprise",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# STYLING
# -----------------------------

st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}

.allow-box {
    background-color: rgba(0,255,140,0.08);
    border: 1px solid #00ff99;
    padding: 18px;
    border-radius: 12px;
}

.review-box {
    background-color: rgba(255,180,0,0.08);
    border: 1px solid #ffb000;
    padding: 18px;
    border-radius: 12px;
}

.block-box {
    background-color: rgba(255,0,80,0.08);
    border: 1px solid #ff0055;
    padding: 18px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("🛡️ AgentGate")
st.sidebar.caption("AI Agent Governance Infrastructure")

st.sidebar.divider()

st.sidebar.subheader("Governance Center")

st.sidebar.markdown("- Live Agents")
st.sidebar.markdown("- Policies")
st.sidebar.markdown("- Audit Center")
st.sidebar.markdown("- Escalations")
st.sidebar.markdown("- Incident Queue")
st.sidebar.markdown("- Semantic Monitor")

st.sidebar.divider()

environment = st.sidebar.selectbox(
    "Environment",
    ["production", "enterprise", "internal", "sandbox"]
)

# -----------------------------
# TOP METRICS
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Agents Protected", "14")

with col2:
    st.metric("Inspections", "8,421")

with col3:
    st.metric("Blocked Actions", "1,284")

with col4:
    st.metric("Risk Accuracy", "98%")

st.divider()

# -----------------------------
# ACTION SELECTOR
# -----------------------------

action = st.selectbox(
    "Select Action",
    [
        "send_email",
        "read_data",
        "delete_data",
        "permission_change"
    ]
)

# -----------------------------
# GOVERNANCE ENGINE
# -----------------------------

risk_map = {
    "send_email": {
        "decision": "REVIEW",
        "risk": 0.31,
        "class": "review-box",
        "explanation": "External communication detected in sensitive environment.",
        "policies": [
            "CUSTOMER_DATA_PROTECTION",
            "HIGH_SENSITIVITY_ENVIRONMENT"
        ]
    },

    "read_data": {
        "decision": "ALLOW",
        "risk": 0.03,
        "class": "allow-box",
        "explanation": "Read-only low-risk action.",
        "policies": []
    },

    "delete_data": {
        "decision": "BLOCK",
        "risk": 0.69,
        "class": "block-box",
        "explanation": "Irreversible destructive action detected.",
        "policies": [
            "SENSITIVE_ACTION_TYPE",
            "CUSTOMER_DATA_PROTECTION"
        ]
    },

    "permission_change": {
        "decision": "BLOCK",
        "risk": 0.82,
        "class": "block-box",
        "explanation": "Privileged identity-security operation detected.",
        "policies": [
            "IDENTITY_SECURITY_CONTROL",
            "HIGH_SENSITIVITY_ENVIRONMENT"
        ]
    }
}

# -----------------------------
# EXECUTION
# -----------------------------

if st.button("Run Governance Inspection"):

    result = risk_map[action]

    st.markdown(
        f"""
        <div class="{result['class']}">
            <h1>{result['decision']}</h1>
            <h3>Risk Score: {result['risk']}</h3>
            <p>{result['explanation']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # Explainability Engine

    st.subheader("Explainability Engine")

    st.write("### Triggered Policies")

    if result["policies"]:
        for policy in result["policies"]:
            st.warning(policy)
    else:
        st.success("No critical policies triggered")

    # Semantic Analysis

    st.write("### Semantic Analysis")

    semantic_items = [
        "External exposure risk detected",
        "Identity privilege escalation signals detected",
        "Irreversible operation identified",
        "Customer data interaction detected",
        "Low-risk read-only behavior"
    ]

    st.info(random.choice(semantic_items))

    # Timeline

    st.subheader("Agent Trace Timeline")

    timeline = pd.DataFrame({
        "Timestamp": [
            "12:41",
            "12:42",
            "12:43",
            "12:44"
        ],
        "Event": [
            "Agent initiated operation",
            "Semantic analyzer evaluated intent",
            "Policy engine triggered escalation",
            f"Decision issued: {result['decision']}"
        ]
    })

    st.dataframe(timeline, use_container_width=True)

    # Multi-Agent Monitoring

    st.subheader("Multi-Agent Monitoring")

    agents = pd.DataFrame({
        "Agent": [
            "agent_admin",
            "agent_reader",
            "agent_mailer"
        ],

        "State": [
            "Escalated",
            "Stable",
            "Review"
        ],

        "Risk": [
            0.82,
            0.03,
            0.31
        ],

        "Decision": [
            "BLOCK",
            "ALLOW",
            "REVIEW"
        ]
    })

    st.dataframe(agents, use_container_width=True)

    # Live Simulation

    st.subheader("Live Agent Simulation")

    simulation_steps = [
        "Agent analyzing environment...",
        "Inspecting tool permissions...",
        "Evaluating semantic intent...",
        "Running governance policies...",
        f"Final decision: {result['decision']}"
    ]

    sim_box = st.empty()

    for step in simulation_steps:
        sim_box.info(step)
        time.sleep(0.7)

st.divider()

st.caption("AgentGate Enterprise Governance System")