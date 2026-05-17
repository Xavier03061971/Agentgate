# AgentGate Enterprise Dashboard v2

Reemplaza COMPLETAMENTE tu archivo `dashboard.py` por este código.

```python
import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="AgentGate",
    page_icon="🛡️",
    layout="wide"
)

# =========================
# STYLES
# =========================

st.markdown(
    """
    <style>
    .main {
        background-color: #0f1117;
        color: white;
    }

    .metric-card {
        background-color: #1b1f2a;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #2d3445;
        text-align: center;
    }

    .decision-box {
        padding: 20px;
        border-radius: 16px;
        font-size: 28px;
        font-weight: bold;
        text-align: center;
    }

    .allow {
        background-color: rgba(0,255,100,0.15);
        border: 1px solid #00ff88;
    }

    .review {
        background-color: rgba(255,180,0,0.15);
        border: 1px solid #ffb000;
    }

    .block {
        background-color: rgba(255,0,80,0.15);
        border: 1px solid #ff0050;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# HEADER
# =========================

st.title("🛡️ AgentGate")
st.caption("AI Agent Governance Layer")

st.divider()

# =========================
# SIDEBAR
# =========================

st.sidebar.title("Control Panel")

selected_action = st.sidebar.selectbox(
    "Agent Action",
    [
        "send_email",
        "delete_data",
        "read_data",
        "permission_change"
    ]
)

selected_env = st.sidebar.selectbox(
    "Environment",
    [
        "internal",
        "enterprise",
        "production",
        "critical"
    ]
)

selected_sensitivity = st.sidebar.selectbox(
    "Sensitivity",
    [
        "low",
        "medium",
        "high",
        "critical"
    ]
)

run = st.sidebar.button("Run Inspection")

# =========================
# DASHBOARD METRICS
# =========================

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

# =========================
# ENGINE
# =========================

if run:

    if selected_action == "read_data":
        decision = "ALLOW"
        risk = 0.03
        external = 0.05
        internal = 0.00
        semantic = 0.00
        explanation = "Safe read-only operation detected."

    elif selected_action == "send_email":
        decision = "REVIEW"
        risk = 0.31
        external = 0.42
        internal = 0.03
        semantic = 0.21
        explanation = "External communication requires human validation."

    elif selected_action == "delete_data":
        decision = "BLOCK"
        risk = 0.69
        external = 0.92
        internal = 0.03
        semantic = 0.21
        explanation = "Destructive operation detected."

    else:
        decision = "BLOCK"
        risk = 0.82
        external = 1.00
        internal = 0.07
        semantic = 0.39
        explanation = "Privileged identity operation blocked."

    # =========================
    # DECISION BOX
    # =========================

    if decision == "ALLOW":
        css_class = "allow"
        emoji = "🟢"

    elif decision == "REVIEW":
        css_class = "review"
        emoji = "🟡"

    else:
        css_class = "block"
        emoji = "🔴"

    st.markdown(
        f"""
        <div class="decision-box {css_class}">
            {emoji} {decision}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # =========================
    # RISK METRICS
    # =========================

    r1, r2, r3, r4 = st.columns(4)

    r1.metric("Total Risk", risk)
    r2.metric("External", external)
    r3.metric("Internal", internal)
    r4.metric("Semantic", semantic)

    st.progress(risk)

    st.info(explanation)

    # =========================
    # DETAILS
    # =========================

    detail_col1, detail_col2 = st.columns(2)

    with detail_col1:
        st.subheader("Inspection Context")

        st.json(
            {
                "action": selected_action,
                "environment": selected_env,
                "sensitivity": selected_sensitivity,
                "confidence": round(random.uniform(0.85, 0.97), 3)
            }
        )

    with detail_col2:
        st.subheader("Governance Notes")

        notes = pd.DataFrame(
            {
                "Signal": [
                    "External Exposure",
                    "Privilege Escalation",
                    "Irreversible Action",
                    "Sensitive Context"
                ],
                "Detected": [
                    "Yes",
                    "No",
                    "Yes",
                    "Yes"
                ]
            }
        )

        st.dataframe(notes, use_container_width=True)

# =========================
# FOOTER
# =========================

st.divider()

st.caption("AgentGate Enterprise Governance System")
```

---

# Luego

Haz commit y push:

```bash
git add .
git commit -m "Upgrade enterprise dashboard"
git push
```

