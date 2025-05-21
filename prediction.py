# import libraries
import pandas as pd
import streamlit as st
import joblib

def run():

    # import model
    with open('model_test.joblib', 'rb') as file:
        model = joblib.load(file)

    # variable for customer information
    age = st.number_input(label = 'Input customers\' age:', min_value = 0.0)
    gender = st.selectbox(label = 'Choose customers\' gender', options = ['male', 'female'])
    education = st.selectbox(label = 'Choose customers\' education', 
                             options = ['Bachelor', 'Master', 'High School', 'Doctorate', 'Associate'])
    income = st.number_input(label = 'Input customers\' income', min_value = 0.0)
    emp_exp = st.number_input(label = 'Input customers\' employment experience', min_value = 0)
    home_ownership = st.selectbox(label = 'Input customers\' home ownership', 
                                  options = ['MORTGAGE', 'OWN', 'RENT', 'OTHER'])
    amount = st.number_input(label = 'Input customers loan amount', min_value = 0)
    cust_intent = st.selectbox(label = 'Choose customers loan intent',
                                options = ['HOMEIMPROVEMENT', 'EDUCATION', 'VENTURE', 'PERSONAL', 'MEDICAL', 'DEBTCONSOLIDATION'])
    int_rate = st.number_input(label = 'Input customers interest rate', min_value = 0.00)
    percent_income = st.number_input(label = 'Input customers\' loan percentage from income', min_value = 0.00)
    cred_history = st.number_input(label = 'Input customers\' credit history length(in years)', min_value = 0.00)
    cred_score = st.number_input(label = 'Input customers\' credit score', min_value = 0)
    loan_defaults = st.selectbox(label = 'Choose previous loan defaults status', options = ['Yes', 'No'])

    st.write('Customer data from input:')
    # create variable for dataframe
    data = pd.DataFrame({'person_age': age,
                         'person_gender': gender,
                         'person_education': education,
                         'person_income': income,
                         'person_emp_exp': emp_exp,
                         'person_home_ownership': home_ownership,
                         'loan_amount': amount,
                         'loan_intent': cust_intent,
                         'loan_int_rate': int_rate,
                         'loan_percent_income': percent_income,
                         'cred_hist_length': cred_history,
                         'credit_score': cred_score,
                         'prev_loan_defaults':loan_defaults}, index = [0])
    
    df = data.copy()
    df = df[['person_income', 'loan_int_rate', 'loan_percent_income',
                     'person_home_ownership', 'prev_loan_defaults']]
    # display dataframe
    st.dataframe(data)
    
    if st.button(label = 'predict'):
        y_pred_inf = model.predict(data)
        if y_pred_inf[0] == 1:
            st.write('Customer loan request is approved')
        elif y_pred_inf[0] == 0:
            st.write('Customer loan request is not approved ')
