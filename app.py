# import libraries
import streamlit as st
import pandas as pd
import eda
import prediction

# side bar option
page = st.sidebar.selectbox(label = 'Select Page', options = ['Introduction', 'Exploratory Data Analysis', 'Model Prediction'])

if page == 'Introduction':
    # introduction page
    st.title('Milestone 2')
    st.write('Name: Bagus Rifky Riyanto')
    st.write('Batch: HCK-27')

    # background
    with st.expander('Background'):
        st.caption("There are many customers' types and their behaviour when using their money. " \
        "Many use their credit card as a shortcut to purchase anything they want, and then they pay it later. " \
        "We can benefit those behaviour to sell our products. The caveat is that there are many customer who always make their payment way passed the promised due date. " \
        "This isn't good for the growth of the business when our bank has a customers' with that kind of behaviour. " \
        "To optimize our decision when approving loan application, we use machine learning and data to improve our percentage of low risk customers'. " \
        "Increasing percentage of low risk customers' can drives our bank profit even higher.")

    # dataset description
    with st.expander('Dataset Description'):
        st.caption("This dataset is filled with information of NIOOS Bank customers' loan application. Column in this dataset is consist of, person_age, person_gender," \
        "person_education, person_income, person_emp_exp, person_home_ownership, loan_amnt, loan_intent, loan_int_rate , loan_percent_income , cb_person_cred_hist_length,"
        "credit_score, previous_loan_defaults_on_file, loan_status")
    
    # objective
    with st.expander('Objective'):
        st.caption("Objectives for this analysis is predicting customers' loan application approval for NIOOS Bank, helping credit risk approval team on loan approval decision," \
        "helping marketing team when doing promotion of our financial products.")

    # conclusion
    with st.expander('Conclusion'):
        st.caption("Random Forest Classifier model before hyperparameter tuning process is prefereable for doing prediction on customers' loan request approval. " \
        "We can get a prediction around 76 percent of our predicted approved customers' loan are actually approveable customers'. " \
        "That percentange comes from precision score when using that model at 0.76, which's a good result.")
    
    # recommendation
    with st.expander("Recommendation"):
        st.caption("Our model is performing good in model inference process, but because the model is overfit, mayybe the result is just come out by chance. " \
                   "To improve our prediction, using Grid Search method on hyperparameter tuning is preferable rather than using Random Search method. " \
                   "Grid Search can provide better parameter for a better result. Higher percentange of predicted customers' loan approval that actually is " \
                   "an approveable customers' can be achieved.")

elif page == 'Exploratory Data Analysis':
    eda.run()

elif page == 'Model Prediction':
    prediction.run()
