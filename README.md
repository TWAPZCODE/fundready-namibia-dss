# FundReady Namibia DSS & PAP

FundReady Namibia is a comprehensive Decision Support System (DSS) and Predictive Analytics Platform (PAP) designed to empower Namibian Small and Medium Enterprises (SMEs) to become funding-ready and secure loans/grants.

## Project Vision
- **Increase Funding Success:** Improve SME chances of securing financial support.
- **Optimize Loan Terms:** Present SMEs as lower-risk borrowers for better interest rates.
- **Regulatory Sandbox:** Built for submission to the Bank of Namibia's Regulatory Sandbox.

## Tech Stack (100% Python)
- **Backend:** Django & Django REST Framework (DRF)
- **Frontend:** Streamlit
- **Analytics:** Integrated Predictive Engine (NumPy, Pandas)
- **Security:** Environment-based configuration

## Core Features
1.  **SME Success Dashboard:** View Readiness Scores, ML-predicted success probabilities, and Data Trust Scores.
2.  **Diagnostic Assessment:** Interactive questionnaire with real-time scoring.
3.  **AI Document Decipherer:** LLM-powered keyword and metric extraction from PDF/Images.
4.  **Financial Projection Assistant:** 3-year bank-standard financial forecasting (Income Statement, Cash Flow, Balance Sheet).
5.  **GIGO Resistance:** Multi-layered validation and anomaly detection to ensure high-quality data.
6.  **Fiduciary Logging:** Comprehensive audit trails of all user activities.

## How to Launch in VS Code

This project is pre-configured for VS Code. Follow these steps to launch:

1.  **Install Dependencies:**
    Open your terminal and run:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Initialize Database (First time only):**
    ```bash
    cd backend
    python manage.py makemigrations core
    python manage.py migrate
    python manage.py seed_db
    ```

3.  **Launch via VS Code:**
    - Go to the **Run and Debug** view in the VS Code Sidebar (Ctrl+Shift+D).
    - Select **"Launch Full App"** from the dropdown menu.
    - Click the **Green Play Button**.
    - This will start both the **Django Backend** (on port 8000) and the **Streamlit UI** (on port 8501).

4.  **Access the App:**
    - The Streamlit UI will automatically open in your browser at `http://localhost:8501`.
    - The Django API is available at `http://localhost:8000/api`.

## Troubleshooting
- **NameError: name 'null' is not defined:** This usually happens if you try to run an `.ipynb` (Jupyter Notebook) file directly with the Python interpreter. Notebooks are JSON files and cannot be run as scripts. Please use the VS Code "Run and Debug" configurations provided.
- **Missing Module:** Ensure you have activated your virtual environment and run `pip install -r requirements.txt`.
