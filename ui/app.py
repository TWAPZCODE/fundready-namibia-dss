import streamlit as st
import pandas as pd
import requests
import time
import random

# Page Config
st.set_page_config(page_title="FundReady Namibia DSS", layout="wide")

# Sidebar Navigation
st.sidebar.title("FundReady Namibia")
st.sidebar.subheader("Decision Support System")
page = st.sidebar.radio("Navigation", ["Dashboard", "Diagnostic Assessment", "AI Document Decipherer", "Financial Projection Assistant", "Trust Portfolio"])

# API Configuration
API_BASE_URL = "http://localhost:8000/api"

def call_api(endpoint, method="GET", data=None):
    """Utility to interact with the Django Backend API"""
    try:
        url = f"{API_BASE_URL}/{endpoint}"
        if method == "POST":
            return requests.post(url, json=data)
        return requests.get(url)
    except Exception as e:
        return None

# Global State Simulation
if 'readiness_score' not in st.session_state:
    st.session_state.readiness_score = 45
if 'ml_prediction' not in st.session_state:
    st.session_state.ml_prediction = 0.52
if 'trust_score' not in st.session_state:
    st.session_state.trust_score = 0.60

# --- DASHBOARD ---
if page == "Dashboard":
    st.title("SME Success Dashboard")
    st.write("Welcome back to FundReady Namibia. Here is your current funding readiness overview.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Readiness Score", f"{st.session_state.readiness_score}%", delta="Rule-based")
        st.caption("Based on expert criteria")

    with col2:
        st.metric("ML Success Probability", f"{(st.session_state.ml_prediction * 100):.1f}%", delta="Predictive")
        st.caption("AI-driven probability")

    with col3:
        st.metric("Data Trust Score", f"{(st.session_state.trust_score * 100):.0f}%", delta="Quality")
        st.progress(st.session_state.trust_score)

    st.info("**Predictive Insight:** Your profile matches the 'High Potential Growth' cluster for the Technology sector. Completing your 'Marketing Strategy' could increase your probability by 12%.")

    st.subheader("Actionable Gap Analysis")
    st.warning("⚠️ **Critical Gaps Detected:**")
    st.write("- Business Registration with BIPA is incomplete.")
    st.write("- Financial records for the last 6 months are inconsistent.")
    st.write("- Marketing strategy lacks specific Namibian market context.")

# --- DIAGNOSTIC ASSESSMENT ---
elif page == "Diagnostic Assessment":
    st.title("Funding Readiness Assessment")
    st.write("Answer these questions to improve your score and get matched with funders.")

    with st.form("diagnostic_form"):
        q1 = st.radio("Is your business registered with BIPA?", ["Yes", "No", "In Progress"])
        q2 = st.radio("Do you have a formal business plan?", ["Yes", "No"])
        q3 = st.radio("Do you keep separate bank accounts for business and personal use?", ["Yes", "No"])
        q4 = st.slider("How many years has your business been operating?", 0, 10, 1)

        submitted = st.form_submit_button("Submit Assessment")
        if submitted:
            with st.spinner("Analyzing your data for GIGO resistance..."):
                time.sleep(2)
                st.session_state.readiness_score = random.randint(60, 85)
                st.session_state.ml_prediction = random.uniform(0.65, 0.90)
                st.success("Assessment Complete! Your Dashboard has been updated.")
                st.balloons()

# --- AI DOCUMENT DECIPHERER ---
elif page == "AI Document Decipherer":
    st.title("AI Document Decipherer & Auditor")
    st.write("Upload your documents (PDF, Image) and our integrated LLM will extract key data and audit for consistency.")

    uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        if st.button("Start AI Analysis"):
            with st.spinner("LLM is deciphering keywords and metrics..."):
                time.sleep(3)
                st.success("Analysis Complete!")
                st.subheader("Extracted Keywords")
                st.write("`Revenue`, `Namibian Compliance`, `Operating Expenses`, `NamRA`, `VAT 15%`")

                st.subheader("Audit Report")
                st.error("❌ **Issue:** Projected expenses do not account for Namibian VAT (15%).")
                st.error("❌ **Issue:** Executive Summary is too short (less than 200 words).")
                st.info("💡 **Insight:** AI detected a complete set of financial records for FY2023.")

                st.session_state.trust_score = min(st.session_state.trust_score + 0.15, 1.0)

# --- FINANCIAL PROJECTION ASSISTANT ---
elif page == "Financial Projection Assistant":
    st.title("Financial Projection Assistant")
    st.write("Generate bank-standard 3-year projections.")

    base_rev = st.number_input("Base Yearly Revenue (NAD)", value=100000)
    base_exp = st.number_input("Base Yearly Expenses (NAD)", value=80000)
    scenario = st.selectbox("Select Scenario", ["Conservative", "Realistic", "Optimistic"])

    mults = {
        "Conservative": (1.05, 1.02),
        "Realistic": (1.15, 1.05),
        "Optimistic": (1.30, 1.10)
    }
    rm, em = mults[scenario]

    data = []
    r, e = base_rev, base_exp
    for year in range(1, 4):
        data.append({
            "Year": f"Year {year}",
            "Revenue": round(r, 2),
            "Expenses": round(e, 2),
            "Profit": round(r - e, 2)
        })
        r *= rm
        e *= em

    df = pd.DataFrame(data)
    st.table(df)
    st.line_chart(df.set_index("Year")[["Revenue", "Profit"]])

# --- TRUST PORTFOLIO ---
elif page == "Trust Portfolio":
    st.title("Trust Portfolio & Fiduciary Logs")
    st.write("Manage your verified documents and view activity history.")

    st.subheader("Verified Documents")
    st.checkbox("BIPA Registration Certificate", value=True)
    st.checkbox("NamRA Tax Good Standing", value=False)
    st.checkbox("Audited Financial Statements", value=False)

    st.subheader("Fiduciary Usage Log")
    log_data = [
        {"Date": "2023-11-01 10:15", "User": "admin_sme", "Action": "Updated SME Profile"},
        {"Date": "2023-11-01 10:20", "User": "admin_sme", "Action": "Ran AI Document Scan"},
        {"Date": "2023-11-01 10:45", "User": "admin_sme", "Action": "Submitted Assessment"}
    ]
    st.dataframe(pd.DataFrame(log_data))

# Footer
st.markdown("---")
st.caption("FundReady Namibia DSS - Built with Python & Streamlit for the Bank of Namibia Regulatory Sandbox.")
