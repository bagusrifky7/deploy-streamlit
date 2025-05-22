# import libraries
import streamlit as st
import pandas as pd
import eda
import prediction

# Sidebar navigation
page = st.sidebar.selectbox(
    label='Select Page',
    options=['Introduction', 'Exploratory Data Analysis', 'Model Prediction']
)

if page == 'Introduction':
    # Introduction Page
    st.title('Milestone 2')
    st.write('**Name:** Bagus Rifky Riyanto')
    st.write('**Batch:** HCK-27')

    # Background
    with st.expander('Background'):
        st.caption(
            "There are many types of customers and various behaviors when it comes to managing money. "
            "Some customers frequently use credit cards to make purchases and repay the debt later. "
            "While this can present opportunities to offer products, some customers regularly miss their payment deadlines. "
            "This behavior can negatively impact business growth, especially in banking. "
            "To optimize loan approval decisions, we apply machine learning to identify low-risk customers. "
            "A higher percentage of low-risk approvals can significantly boost bank profits."
        )

    # Dataset Description
    with st.expander('Dataset Description'):
        st.caption(
            "The dataset contains information on loan applications from NIOOS Bank customers. "
            "It includes the following columns: person_age, person_gender, person_education, person_income, "
            "person_emp_exp, person_home_ownership, loan_amnt, loan_intent, loan_int_rate, "
            "loan_percent_income, cb_person_cred_hist_length, credit_score, "
            "previous_loan_defaults_on_file, and loan_status."
        )

    # Objective
    with st.expander('Objective'):
        st.caption(
            "The main objectives of this analysis are to predict the approval of loan applications for NIOOS Bank, "
            "support the credit risk team in decision-making, and assist the marketing team in targeting the right customers."
        )

    # Conclusion
    with st.expander('Conclusion'):
        st.caption(
            "The Random Forest Classifier, before hyperparameter tuning, performs best for predicting loan approvals. "
            "It achieves a precision score of 0.76, meaning that 76% of predicted approvals are correct. "
            "This makes it a reliable model for identifying approve-worthy applications."
        )

    # Recommendation
    with st.expander('Recommendation'):
        st.caption(
            "Although the current model performs well, it shows signs of overfitting. "
            "To enhance performance and generalization, Grid Search for hyperparameter tuning is recommended over Random Search. "
            "This could yield better model parameters, improving precision and increasing the accuracy of approved customer predictions."
        )

elif page == 'Exploratory Data Analysis':
    eda.run()

elif page == 'Model Prediction':
    prediction.run()
    