# FundReady Namibia: Streamlit Decision Support System

FundReady Namibia is a 100% Python-based Decision Support System (DSS) and Predictive Analytics Platform (PAP). It is designed to help Namibian SMEs become funding-ready through intelligent assessments, AI-driven document auditing, and predictive success modeling.

## 🚀 Quick Start (Streamlit)

The fastest way to experience FundReady Namibia is through the Streamlit interface:

1.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Launch the App:**
    ```bash
    streamlit run streamlit_app.py
    ```

## 🛠️ VS Code Integration

This project is optimized for VS Code.
- Open the **Run and Debug** tab (Ctrl+Shift+D).
- Select **"Launch Streamlit App"** to start the UI.
- Select **"Launch Full App (Backend + UI)"** if you want to run the Django API alongside the Streamlit interface.

## 🌟 Key Features
- **Predictive Success Dashboard:** Real-time ML-driven probability of funding success.
- **Diagnostic Assessment:** Comprehensive SME readiness check.
- **Funding Matchmaker:** Searchable database of Namibian lenders (FNB, DBN, etc.).
- **AI Document Decipherer:** Automated extraction of metrics from PDFs and images.
- **Creditworthiness Simulator:** Interactive "what-if" scenarios for interest rate optimization.
- **Sandbox Submission Portal:** Compliant interface for the Bank of Namibia Regulatory Sandbox.

## 🏗️ Architecture
- **Frontend:** Streamlit (Pure Python)
- **Backend:** Django & Django REST Framework (Data persistence & GIGO-resistant validation)
- **Analytics:** NumPy & Pandas (Predictive modeling)

## 📝 Fiduciary Compliance
The system includes a **Usage Log** to track all user activities and dates, ensuring transparency for fiduciary and regulatory requirements.
