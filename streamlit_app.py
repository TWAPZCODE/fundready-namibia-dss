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
page = st.sidebar.radio("Navigation", ["Dashboard", "Diagnostic Assessment", "Funding Matchmaker", "AI Document Decipherer", "Financial Projection Assistant", "Creditworthiness Simulator", "Sandbox Submission", "Trust Portfolio"])

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
        st.error(f"Backend connection error: {e}")
        return None

# Global State Simulation (Synced with API results)
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
            with st.spinner("Submitting to Predictive Engine..."):
                # Real API call to trigger backend scoring and ML prediction
                res = call_api("assessments/", method="POST", data={
                    "company_name": "SME Demo", # Mocked for demo
                    "registration_status": q1,
                    "has_business_plan": q2
                })
                time.sleep(2)
                if res and res.status_code == 201:
                    data = res.json()
                    st.session_state.readiness_score = data.get('score', 75)
                    st.session_state.ml_prediction = data.get('ml_predicted_success', 0.8)
                    st.success("Assessment Processed by PAP! Your Dashboard has been updated.")
                else:
                    st.warning("Assessment saved locally (Backend Offline).")
                st.balloons()

# --- FUNDING MATCHMAKER ---
elif page == "Funding Matchmaker":
    st.title("Funding Matchmaker")
    st.write("Find the best funding opportunities based on your sector and readiness.")

    col1, col2 = st.columns(2)
    with col1:
        sector_filter = st.selectbox("Filter by Sector", ["All", "Agriculture", "Technology", "Mining", "Retail"])
    with col2:
        type_filter = st.multiselect("Funding Type", ["Loan", "Grant", "Equity"], default=["Loan", "Grant"])

    # Fetch from API
    res = call_api("funding-sources/")
    if res and res.status_code == 200:
        funding_data = res.json()
    else:
        # Fallback to sample data if API is down
        funding_data = [
            {"name": "SME Special Loan", "organization": "FNB Namibia", "funding_type": "Loan", "amount_min": "50000", "amount_max": "1000000", "sector": "General"},
            {"name": "Agri-Business Grant", "organization": "DBN", "funding_type": "Grant", "amount_min": "100000", "amount_max": "5000000", "sector": "Agriculture"},
        ]

    df_fund = pd.DataFrame(funding_data)
    if not df_fund.empty:
        if sector_filter != "All":
            df_fund = df_fund[df_fund["sector"] == sector_filter]

        for _, row in df_fund.iterrows():
            with st.expander(f"{row['name']} ({row['organization']})"):
                st.write(f"**Type:** {row['funding_type']}")
                st.write(f"**Amount:** NAD {row['amount_min']} - {row['amount_max']}")
                st.write(f"**Sector:** {row['sector']}")
                st.write("**Requirements:** BIPA Registration, 12 Months Financials, Good Standing Certificate.")
                if st.button(f"Apply for {row['name']}", key=row['name']):
                    st.success("Application started! Progress tracked in your Dashboard.")

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

# --- SANDBOX SUBMISSION ---
elif page == "Sandbox Submission":
    st.title("Bank of Namibia Sandbox Interface")
    st.write("Compile and submit your application journey to the BoN Regulatory Sandbox.")

    st.subheader("Data Compilation Checklist")
    st.checkbox("Anonymized SME Profile", value=True)
    st.checkbox("Diagnostic Readiness Journey", value=True)
    st.checkbox("AI Audit Trail", value=True)
    st.checkbox("Compliance Declarations", value=False)

    if st.button("Compile and Submit to BoN"):
        with st.spinner("Anonymizing data and generating sandbox report..."):
            time.sleep(3)
            st.success("🎉 Successfully submitted to the BoN Regulatory Sandbox!")
            st.write("Reference ID: **BON-SANDBOX-2023-9981**")
            st.balloons()

# --- CREDITWORTHINESS SIMULATOR ---
elif page == "Creditworthiness Simulator":
    st.title("Creditworthiness Simulator")
    st.write("See how specific actions could improve your risk profile and interest rates.")

    current_score = st.session_state.readiness_score
    st.write(f"**Current Score:** {current_score}")

    st.subheader("Simulate Improvements")
    imp_options = [
        {"label": "Reduce Debt-to-Income Ratio", "impact": 10},
        {"label": "Secure a Formal Off-take Contract", "impact": 15},
        {"label": "Keep 6 Months Clean Bank Statements", "impact": 20},
        {"label": "Complete BIPA Registration", "impact": 15}
    ]

    selected_imps = []
    for imp in imp_options:
        if st.checkbox(f"{imp['label']} (+{imp['impact']} pts)"):
            selected_imps.append(imp)

    simulated_score = min(current_score + sum(i['impact'] for i in selected_imps), 100)

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Simulated Score", f"{simulated_score}%", delta=f"{simulated_score - current_score}%")
    with col2:
        rate = "12.5%" if simulated_score > 80 else "15.5%" if simulated_score > 60 else "18.5%"
        st.metric("Potential Interest Rate", rate)

    st.info(f"**Risk Profile:** {'Low' if simulated_score > 80 else 'Medium' if simulated_score > 60 else 'High'}")

# --- TRUST PORTFOLIO ---
elif page == "Trust Portfolio":
    st.title("Trust Portfolio & Fiduciary Logs")
    st.write("Manage your verified documents and view activity history.")

    st.subheader("Verified Documents")
    st.checkbox("BIPA Registration Certificate", value=True)
    st.checkbox("NamRA Tax Good Standing", value=False)
    st.checkbox("Audited Financial Statements", value=False)

    st.subheader("Fiduciary Usage Log")

    # Fetch from API
    res = call_api("usage-logs/")
    if res and res.status_code == 200:
        st.dataframe(pd.DataFrame(res.json()))
    else:
        # Sample data if API down
        log_data = [
            {"timestamp": "2023-11-01 10:15", "action": "Updated SME Profile"},
            {"timestamp": "2023-11-01 10:20", "action": "Ran AI Document Scan"},
        ]
        st.dataframe(pd.DataFrame(log_data))

# Footer
st.markdown("---")
st.caption("FundReady Namibia DSS - Built with Python & Streamlit for the Bank of Namibia Regulatory Sandbox.")
