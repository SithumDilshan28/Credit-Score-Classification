import streamlit as st
import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load('model.h5')
scalar = joblib.load('scalar.h5')

# Title of the web app
st.set_page_config(page_title="Credit Score Prediction", layout="wide", page_icon="💳")
st.title("💳 Credit Score Prediction App")

# Sidebar with additional options
st.sidebar.header("Input Features")

def user_input_features():
    age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=45)
    annual_income = st.sidebar.number_input("Annual Income (in $)", min_value=1000, max_value=1000000, value=85000)
    monthly_inhand_salary = st.sidebar.number_input("Monthly In-hand Salary (in $)", min_value=0, max_value=100000, value=7200)
    num_bank_accounts = st.sidebar.number_input("Number of Bank Accounts", min_value=0, max_value=100, value=3)
    num_credit_card = st.sidebar.number_input("Number of Credit Cards", min_value=0, max_value=50, value=5)
    interest_rate = st.sidebar.number_input("Interest Rate", min_value=0, max_value=100, value=10)
    num_of_loan = st.sidebar.number_input("Number of Loans", min_value=0, max_value=20, value=1)
    delay_from_due_date = st.sidebar.number_input("Delay from Due Date", min_value=0, max_value=365, value=5)
    num_of_delayed_payment = st.sidebar.number_input("Number of Delayed Payments", min_value=0, max_value=100, value=3)
    changed_credit_limit = st.sidebar.number_input("Changed Credit Limit", value=10000.0)
    num_credit_inquiries = st.sidebar.number_input("Number of Credit Inquiries", min_value=0, max_value=50, value=2)
    outstanding_debt = st.sidebar.number_input("Outstanding Debt", value=5000.0)
    credit_utilization_ratio = st.sidebar.number_input("Credit Utilization Ratio", min_value=0, max_value=100, value=25)
    credit_history_age = st.sidebar.number_input("Credit History Age (in months)", min_value=0, max_value=600, value=180)
    total_emi_per_month = st.sidebar.number_input("Total EMI per Month", value=300.0)
    amount_invested_monthly = st.sidebar.number_input("Amount Invested Monthly", value=1200.0)
    monthly_balance = st.sidebar.number_input("Monthly Balance", value=600.0)
    
    # Categorical inputs (replace 1/0 based on your original data encoding)
    month_August = st.sidebar.selectbox("Is it August?", ["No", "Yes"])
    occupation_engineer = st.sidebar.selectbox("Is Occupation Engineer?", ["No", "Yes"])
    payment_min_amount = st.sidebar.selectbox("Payment of Minimum Amount?", ["No", "Yes"])
    payment_behaviour_low_spent = st.sidebar.selectbox("Low Spent Medium Value Payments?", ["No", "Yes"])
    
    # Encode the categorical variables as in the original training data
    month_August = 1 if month_August == "Yes" else 0
    occupation_engineer = 1 if occupation_engineer == "Yes" else 0
    payment_min_amount = 1 if payment_min_amount == "Yes" else 0
    payment_behaviour_low_spent = 1 if payment_behaviour_low_spent == "Yes" else 0
    
    # Combine all features into a single array
    features = np.array([[age, annual_income, monthly_inhand_salary, num_bank_accounts, num_credit_card, 
                          interest_rate, num_of_loan, delay_from_due_date, num_of_delayed_payment, changed_credit_limit, 
                          num_credit_inquiries, 1, outstanding_debt, credit_utilization_ratio, credit_history_age, 
                          total_emi_per_month, amount_invested_monthly, monthly_balance, 
                          1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                          payment_min_amount, 0, 0, payment_behaviour_low_spent, 0, 0, 0, month_August, occupation_engineer, 1]])
    
    return features

# Display user inputs
input_data = user_input_features()

# Apply the scaler transformation to the input data
input_data_scaled = scalar.transform(input_data)

# Make predictions when the button is clicked
if st.button("Predict Credit Score"):
    prediction = model.predict(input_data_scaled)
    credit_score_mapping = {0: 'Poor', 1: 'Standard', 2: 'Good'}
    st.success(f"Predicted Credit Score: **{credit_score_mapping[prediction[0]]}**")

# CSS styling to improve the look of the app
st.markdown("""
    <style>
    /* Background and main content styling */
    body {
        background-color: #f0f2f6;
        color: #333;
    }
    /* Custom styling for buttons */
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    /* Hover effect for buttons */
    .stButton button:hover {
        background-color: #45a049;
    }
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 5px;
    }
    /* Sidebar header */
    .sidebar h2 {
        color: #4CAF50;
        margin-bottom: 15px;
    }
    /* Input field styling */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        border: 1px solid #ced4da;
        border-radius: 5px;
        padding: 5px;
        width: 100%;
    }
    /* Header styling */
    h1 {
        color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)
