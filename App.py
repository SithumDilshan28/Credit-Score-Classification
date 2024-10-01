import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Credit Score Prediction", layout="wide", page_icon="💳")

# Title of the web app
#st.title("💳 Credit Score Prediction App")

# Sidebar with additional options
with st.sidebar:
    st.title("💳 Credit Score Prediction")  # Adding a title to the sidebar
    #st.image("expert_banner.png", use_column_width=True)  # You can use a custom image here
    st.header("About")
    st.write(
        """
        This app uses sample data to predict credit scores based on features such as age, occupation, income, and more. 
        The sample data includes examples for 'Poor,' 'Standard,' and 'Good' credit scores.
        """
    )
    st.write("Developed by: U-Connect")

# CSS styling to improve the look of the app
st.markdown("""
    <style>
    /* Main container styling */
    /* Container for input fields */
    .input-container {
        background-color: #fff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        max-width: 600px;
        width: 100%;
        margin-top: 40px; /* Adjust this value for spacing from the top */
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
        text-align: center;
        margin-top: 40px; /* Adjust this value for top spacing */
    }
    </style>
    """, unsafe_allow_html=True)

# Sample data with results for 'Poor', 'Standard', and 'Good'
sample_data = pd.DataFrame({
    'Gender': ['Male', 'Female', 'Male'],
    'Age': [25, 45, 35],
    'Occupation': ['Engineer', 'Doctor', 'Teacher'],
    'Annual Income (LKR)': [3000000, 8500000, 5500000],
    'Monthly Base Salary (LKR)': [250000, 720000, 450000],
    'Outstanding Debt (LKR)': [1500000, 500000, 200000],
    'No of Bank Accounts': [2, 5, 3],
    'No of Loans': [3, 1, 0],
    'No of Credit Cards': [4, 2, 5],
    'Credit Score': ['Poor', 'Good', 'Standard']
})

# Display the sample data in the main container

# Center the input form using a container
with st.container():

    st.subheader("Input Your Details Below:")

    # Collect user input data
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    occupation = st.selectbox("Occupation", ["Engineer", "Doctor", "Teacher", "Other"])
    annual_income = st.number_input("Annual Income (in LKR)", min_value=0, max_value=10000000, value=5000000)
    monthly_base_salary = st.number_input("Monthly Base Salary (in LKR)", min_value=0, max_value=1000000, value=400000)
    outstanding_debt = st.number_input("Outstanding Debt (in LKR)", min_value=0, max_value=10000000, value=500000)
    no_of_bank_accounts = st.number_input("Number of Bank Accounts", min_value=0, max_value=50, value=2)
    no_of_loans = st.number_input("Number of Loans", min_value=0, max_value=50, value=1)
    no_of_credit_cards = st.number_input("Number of Credit Cards", min_value=0, max_value=50, value=3)

    # Display user input summary
    st.markdown("### Your Input Summary")
    user_input = {
        "Gender": gender,
        "Age": age,
        "Occupation": occupation,
        "Annual Income (LKR)": annual_income,
        "Monthly Base Salary (LKR)": monthly_base_salary,
        "Outstanding Debt (LKR)": outstanding_debt,
        "Number of Bank Accounts": no_of_bank_accounts,
        "Number of Loans": no_of_loans,
        "Number of Credit Cards": no_of_credit_cards,
    }

    st.json(user_input)

    # Display sample results when the Predict button is clicked
    if st.button("Predict Credit Score"):
        if gender == "Male" and age <= 25:
            st.success("Predicted Credit Score: **Poor**")
        elif gender == "Female" and annual_income > 8000000:
            st.success("Predicted Credit Score: **Good**")
        else:
            st.success("Predicted Credit Score: **Standard**")

    st.markdown('</div>', unsafe_allow_html=True)
