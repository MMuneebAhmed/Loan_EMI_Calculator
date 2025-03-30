import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Function to calculate EMI
def calculate_emi(principal, rate, tenure):
    monthly_rate = rate / (12 * 100)
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure) / ((1 + monthly_rate) ** tenure - 1)
    return emi

# Function to generate amortization schedule
def generate_amortization_schedule(principal, rate, tenure, extra_payment=0, balloon_payment=0):
    monthly_rate = rate / (12 * 100)
    emi = calculate_emi(principal, rate, tenure)
    balance = principal
    schedule = []
    total_interest_paid = 0
    for month in range(1, tenure + 1):
        interest = balance * monthly_rate
        principal_paid = emi - interest + extra_payment
        balance -= principal_paid
        if month % 12 == 0:
            balance -= balloon_payment
        total_interest_paid += interest
        if balance < 0:
            balance = 0
        schedule.append([month, emi, principal_paid, interest, balance])
        if balance == 0:
            break
    return pd.DataFrame(schedule, columns=["Month", "EMI", "Principal Paid", "Interest Paid", "Balance"]), total_interest_paid

# Function to check loan eligibility
def check_loan_eligibility(employed, income, expenses, credit_score):
    if not employed:
        return False, "Applicant must be employed to be eligible for a loan."
    if income <= expenses:
        return False, "Income must be greater than expenses to qualify for a loan."
    if credit_score < 650:
        return False, "Credit score must be greater than 650 to qualify for a loan."
    return True, "Congratulations! You are eligible for the loan."

# Sidebar settings
dark_mode = st.sidebar.checkbox("Dark Mode 🌙")
currency = st.sidebar.selectbox("Select Currency", ["PKR", "₹", "$", "€", "£"], index=0)
language = st.sidebar.selectbox("Select Language", ["English", "Urdu"], index=0)
loan_type = st.sidebar.selectbox("Select Loan Type", ["Custom", "Home Loan", "Car Loan", "Personal Loan"], index=0)

if loan_type == "Home Loan":
    default_rate = 7.0
    default_tenure = 240
elif loan_type == "Car Loan":
    default_rate = 9.5
    default_tenure = 60
elif loan_type == "Personal Loan":
    default_rate = 12.0
    default_tenure = 36
else:
    default_rate = 7.5
    default_tenure = 120

st.title("Loan EMI Calculator 💳")

# Loan Eligibility Check
st.subheader("Loan Eligibility Check")
employed = st.checkbox("Are you employed?")
income = st.number_input("Enter your monthly income", min_value=0, step=1000)
expenses = st.number_input("Enter your monthly expenses", min_value=0, step=1000)
credit_score = st.number_input("Enter your credit score", min_value=300, max_value=900, step=1)

if "eligible" not in st.session_state:
    st.session_state.eligible = False

if st.button("Check Eligibility"):
    st.session_state.eligible, message = check_loan_eligibility(employed, income, expenses, credit_score)
    if st.session_state.eligible:
        st.success(message)
    else:
        st.error(message)

if st.session_state.eligible:
    principal = st.slider(f"Loan Amount ({currency})", min_value=10000, max_value=10000000, step=10000, value=500000)
    rate = st.slider("Annual Interest Rate (%)", min_value=1.0, max_value=20.0, step=0.1, value=default_rate)
    tenure = st.slider("Loan Tenure (months)", min_value=6, max_value=360, step=6, value=default_tenure)
    extra_payment = st.number_input(f"Extra Monthly Payment ({currency})", min_value=0, value=0, step=1000)
    balloon_payment = st.number_input(f"Balloon Payment ({currency})", min_value=0, value=0, step=10000)

    if st.button("Calculate EMI"):
        df, total_interest_paid = generate_amortization_schedule(principal, rate, tenure, extra_payment, balloon_payment)
        emi = calculate_emi(principal, rate, tenure)
        st.success(f"Your Monthly EMI: {currency}{emi:.2f}")
        st.write(f"Total Interest Paid: {currency}{total_interest_paid:.2f}")
        st.subheader("Amortization Schedule")
        st.dataframe(df)
        months = df["Month"]
        balances = df["Balance"]
        fig = go.Figure(data=[go.Scatter(x=months, y=balances, mode='lines+markers', name='Balance')])
        fig.update_layout(title="Amortization Schedule", xaxis_title="Month", yaxis_title=f"Balance ({currency})", hovermode="x")
        st.plotly_chart(fig)
        fig_pie = go.Figure(data=[go.Pie(labels=["Principal", "Interest"], values=[principal, emi * tenure - principal], hole=.3)])
        fig_pie.update_layout(title="Principal vs Interest Breakdown")
        st.plotly_chart(fig_pie)
