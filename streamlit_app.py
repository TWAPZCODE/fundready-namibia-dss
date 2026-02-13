import streamlit as st
import pandas as pd
import numpy as np
import time
import random
import datetime

# =========================================================
# 1. PAGE CONFIG & INITIALIZATION (MUST BE AT THE VERY TOP)
# =========================================================
st.set_page_config(page_title="FundReady Namibia DSS", layout="wide", page_icon="🇳🇦")

# Initialize Session State
if 'readiness_score' not in st.session_state:
    st.session_state['readiness_score'] = 45
if 'ml_prediction' not in st.session_state:
    st.session_state['ml_prediction'] = 0.52
if 'trust_score' not in st.session_state:
    st.session_state['trust_score'] = 0.60
if 'usage_logs' not in st.session_state:
    st.session_state['usage_logs'] = []

def add_log(action):
    """Fiduciary Compliance Logger"""
    log_entry = {
        "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Action": action,
        "User": "SME_Admin_001"
    }
    st.session_state['usage_logs'].append(log_entry)

# ==========================================
# 2. CORE LOGIC MODULES
# ==========================================

class DataAnomalyDetector:
    def detect_outlier(self, field_name, value, sector):
        benchmarks = {'Agriculture': {'revenue': 500000, 'std': 200000}, 'Mining': {'revenue': 5000000, 'std': 1000000}}
        if sector in benchmarks and field_name in benchmarks[sector]:
            stats = benchmarks[sector]
            z_score = abs((float(value) - stats['revenue']) / stats['std'])
            return z_score > 3
        return False

    def check_consistency(self, data):
        issues = []
        rev, exp = float(data.get('revenue', 0)), float(data.get('expenses', 0))
        if rev < 0: issues.append("Revenue cannot be negative.")
        if rev > 0 and exp > rev * 10: issues.append("Expenses are unusually high relative to revenue.")
        return issues

class PredictiveEngine:
    def predict_readiness_probability(self, profile_data):
        base_prob = 0.4
        years = profile_data.get('years_in_operation', 0)
        if years > 5: base_prob += 0.3
        elif years > 2: base_prob += 0.15
        if profile_data.get('is_registered'): base_prob += 0.2
        return min(max(base_prob + random.uniform(-0.05, 0.05), 0.0), 1.0)

class DocumentDecipherer:
    def decipher(self, file_name):
        return {
            'keywords': ['Revenue', 'Compliance', 'Namibia', 'BIPA'],
            'detected_type': 'Financial Document' if file_name.lower().endswith('.pdf') else 'Image Scan',
            'summary': 'AI processing complete.'
        }

def generate_projections(base_revenue, base_expenses, scenario='Realistic'):
    multipliers = {'Conservative': (1.05, 1.02), 'Realistic': (1.15, 1.05), 'Optimistic': (1.30, 1.10)}
    rev_mult, exp_mult = multipliers[scenario]
    data = []
    r, e = float(base_revenue), float(base_expenses)
    for year in range(1, 4):
        data.append({"Year": f"Year {year}", "Revenue": round(r, 2), "Expenses": round(e, 2), "Profit": round(r - e, 2)})
        r *= rev_mult
        e *= exp_mult
    return pd.DataFrame(data)

# ==========================================
# 3. STREAMLIT UI LAYOUT
# ==========================================

# Sidebar Navigation
st.sidebar.title("🇳🇦 FundReady")
st.sidebar.subheader("Decision Support System")
page = st.sidebar.radio("Navigate", [
    "Dashboard",
    "Diagnostic Assessment",
    "Funding Matchmaker",
    "AI Document Decipherer",
    "Financial Projections",
    "Creditworthiness Simulator",
    "Sandbox Submission",
    "Fiduciary Logs"
])

# Utility: Reset State
if st.sidebar.button("Reset Application"):
    st.session_state['readiness_score'] = 45
    st.session_state['ml_prediction'] = 0.52
    st.session_state['trust_score'] = 0.60
    st.session_state['usage_logs'] = []
    st.rerun()

engine = PredictiveEngine()
decipherer = DocumentDecipherer()

# --- DASHBOARD ---
if page == "Dashboard":
    st.title("🚀 SME Success Dashboard")
    st.write("Current funding readiness overview.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Readiness Score", f"{st.session_state['readiness_score']}%", "Rule-based")
    with col2:
        st.metric("ML Success Probability", f"{(st.session_state['ml_prediction'] * 100):.1f}%", "Predictive (PAP)")
    with col3:
        st.metric("Data Trust Score", f"{(st.session_state['trust_score'] * 100):.0f}%", "Quality")
        st.progress(st.session_state['trust_score'])

    st.info("**Predictive Insight:** Completing your 'Market Analysis' could boost your probability by 15%.")

    st.subheader("Gap Analysis")
    st.warning("⚠️ BIPA Registration is pending verification.")
    st.warning("⚠️ Financial history is limited.")

# --- DIAGNOSTIC ASSESSMENT ---
elif page == "Diagnostic Assessment":
    st.title("📝 Readiness Assessment")
    with st.form("diag_form"):
        q1 = st.checkbox("Is your business registered with BIPA?")
        q2 = st.checkbox("Do you have a formal 3-year business plan?")
        q3 = st.selectbox("Sector", ["Technology", "Agriculture", "Mining", "Retail"])
        years = st.slider("Years in Operation", 0, 20, 2)
        if st.form_submit_button("Submit"):
            add_log("Completed Diagnostic")
            with st.spinner("Analyzing..."):
                time.sleep(2)
                prob = engine.predict_readiness_probability({'years_in_operation': years, 'is_registered': q1})
                st.session_state['ml_prediction'] = prob
                st.session_state['readiness_score'] = int(prob * 100)
                st.success("Analysis Complete!")
                st.balloons()

# --- FUNDING MATCHMAKER ---
elif page == "Funding Matchmaker":
    st.title("🔍 Funding Matchmaker")
    funds = [{"Name": "SME Special Loan", "Org": "FNB Namibia", "Amount": "NAD 1M"}, {"Name": "Agri-Grant", "Org": "DBN", "Amount": "NAD 5M"}]
    for f in funds:
        with st.expander(f"{f['Name']} - {f['Org']}"):
            st.write(f"Maximum Amount: {f['Amount']}")
            if st.button(f"Apply for {f['Name']}", key=f['Name']):
                add_log(f"Applied: {f['Name']}")
                st.success("Application started!")

# --- AI DOCUMENT DECIPHERER ---
elif page == "AI Document Decipherer":
    st.title("🤖 AI Document Decipherer")
    up = st.file_uploader("Upload document", type=['pdf', 'png', 'jpg'])
    if up and st.button("Run AI Analysis"):
        add_log(f"AI Scan: {up.name}")
        with st.spinner("Processing..."):
            time.sleep(3)
            res = decipherer.decipher(up.name)
            st.success("Extraction Successful")
            st.write(f"**Keywords:** {', '.join(res['keywords'])}")
            st.session_state['trust_score'] = min(st.session_state['trust_score'] + 0.12, 1.0)

# --- FINANCIAL PROJECTIONS ---
elif page == "Financial Projections":
    st.title("📊 Financial Projection Assistant")
    rev = st.number_input("Base Revenue (NAD)", value=100000)
    exp = st.number_input("Base Expenses (NAD)", value=80000)
    scen = st.selectbox("Scenario", ["Conservative", "Realistic", "Optimistic"])
    df_p = generate_projections(rev, exp, scen)
    st.table(df_p)
    st.line_chart(df_p.set_index("Year")[["Revenue", "Profit"]])

# --- CREDITWORTHINESS SIMULATOR ---
elif page == "Creditworthiness Simulator":
    st.title("⚖️ Creditworthiness Simulator")
    curr = st.session_state['readiness_score']
    st.write(f"**Current Score:** {curr}%")
    opt1 = st.checkbox("Reduce Debt (+10 pts)")
    opt2 = st.checkbox("Clean Records (+15 pts)")
    sim = min(curr + (10 if opt1 else 0) + (15 if opt2 else 0), 100)
    st.metric("Simulated Score", f"{sim}%", delta=f"{sim - curr}%")
    st.write(f"**Interest Rate Bracket:** {'12.5%' if sim > 80 else '18.5%'}")

# --- SANDBOX SUBMISSION ---
elif page == "Sandbox Submission":
    st.title("🏦 BoN Sandbox Portal")
    if st.button("Submit to Sandbox"):
        add_log("Sandbox Submission")
        with st.spinner("Processing..."):
            time.sleep(4)
            st.success("Submitted! ID: BON-SAND-9981")

# --- FIDUCIARY LOGS ---
elif page == "Fiduciary Logs":
    st.title("📜 Fiduciary Logs")
    if st.session_state['usage_logs']:
        st.table(pd.DataFrame(st.session_state['usage_logs']))
    else:
        st.info("No activity recorded.")

st.markdown("---")
st.caption("FundReady Namibia - 100% Python/Streamlit")
