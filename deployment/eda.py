# import libraries
import streamlit as st
import pandas as pd
from PIL import Image

def run():
    # title section
    st.title('Exploratory Data Analysis')

    # first eda
    st.subheader("A. Relationship Between Customers' Income, History of Credit Length, and Credit Score to Loan Approval")
    image_a1 = Image.open('A_1.jpg')
    image_a2 = Image.open('A_2.jpg')
    st.image(image_a1, caption = 'Skewness Value')
    with st.expander("Explanation"):
        st.caption("Based on the calculations above, person_income, cred_hist_length, and credit_score column have skewed distributions. " \
                   "We will check the relationship between those three columns to loan approval column with point-biserial correlation test. " \
                   "The reason we use this type of correlation test because we gonna check relationships between continuous variable and binary variable.")
    
    st.image(image_a2, caption = 'Correlation Test')
    with st.expander('Explanation'):
        st.caption("Based on the calculations above, person_income and cred_hist_length column have a significant correlation to loan_status column. " \
                   "Meanwhile, credit_score and loan_status don't have a significant correlation between them. Those analyses are determined by the p-value. " \
                   "If we take a look at correlation value, there's a weak correlation between person_income and cred_hist_length column to loan_status column. " \
                   "We can conclude that customers' loan approval are influenced by customers' income and their history of credit length. " \
                   "Meanwhile, customers' loan approval are not influenced by customers' credit score.")

    # second eda
    st.subheader("B.What Age Categories Have The Most Loan Applications?")
    image_b1 = Image.open('B_1.png')
    Image_b2 = Image.open('B_2.png')
    st.image(image_b1, caption = 'Age Comparions for Most Loan Application')
    st.image(Image_b2, caption = 'Age Distribution for Loan Application')
    with st.expander("Explanation"):
        st.caption("Based on the bar chart above, customers' in the adult category have the most loan applications to our bank, " \
                   "meanwhile customers' in the aged category have the lowest loan applications to our bank. If we take a look on the histogram above, " \
                   "customers' age from range 20 to 30 years old have the most loan applications to our bank. We can conclude that " \
                   "there's a lot of customers that interested to our financial products from range of 20 to 30 years old.")

    # third eda
    st.subheader("C. How's The Income Distribution of Our Approved Customers' Loan?")
    image_c1 = Image.open('C_1.png')
    st.image(image_c1, caption = "Income Distributions of Approved Customers' Loan")
    with st.expander("Explanation"):
        st.caption("Based on the income distribution above, most of our approved customers' loan income is in a range between 35000 dollar to 70000 dollar. " \
                   "We can conclude that income in a range between 35000 to 70000 can be considered as a factor for loan request approval.")

    # fourth  eda
    st.subheader("D. How's The Approved Customer Loan Credit Score Distribution?")
    Image_d1 = Image.open('D_1.png')
    st.image(Image_d1, caption = "Credit Score Distribution for Approved Customers Loan")
    with st.expander("Explanation"):
        st.caption("Based on credit score distribution for only approved loan customers', the majority of our customers' credit scores are in the range between 550 to 700. "
                   "    If we take a look at CIBIL score ranges, 550 to 650 is categorised as average scores and 651 to 750 is categorised as good scores. " \
                   "CIBIL score is used as an interpretation of customers' credit score; the higher the score, the better the quality of our customers. " \
                   "We can conclude that we need to keep improving the quality of our customers'.")
        
    # fifth eda
    st.subheader("E. Relationship Between Customers' Employment Experience and How Much Loan Has Been Requested")
    image_e1 = Image.open('E_1.jpg')
    image_e2 = Image.open('E_2.jpg')
    st.image(image_e1, caption = "Skewness Value")
    st.image(image_e2, caption = "Correlation Value")
    with st.expander("Explanation"):
        st.caption("We use spearman correlation test because both column have skewed distribution. " \
                   "Based on calculations, there's a weak correlation between those two columns," \
                   "so we can conclude that there's no significant influenced on requested loan amount " \
                   "based on the higher or lower of customers' employment experience.")
    
    # sixth eda
    st.subheader("F. Relationship Between Customers' Loan Intention and Loan Amount Requested")
    image_f1 = Image.open('F_1.jpg')
    st.image(image_f1, caption = 'Skewness Value')
    with st.expander("Explanation"):
        st.caption("We use the Kendall correlation test because we gonna calculating the correlation value between categorical and numerical columns. " \
                   "Based on the calculation, the P-value shows us that there's no correlation between the two columns, and the correlation value shows us " \
                   "that there's no significant customers' loan intention influenced on the requested loan amount. We can conclude that any customers' " \
                   "loan intention doesn't make the customers' make a specific amount of the requested loan.")
    
    # seventh eda
    st.subheader("G. How's The Distribution of Customers' Credit Scores When The Loan Intention Is for Debt Consolidation?")
    image_g1 = Image.open('G_1.png')
    st.image(image_g1, caption = 'Credit Scores Distribution With Loan Intention for Debt Consolidation')
    with st.expander("Explanation"):
        st.caption("Based on the visualisation above, customers' who requested a loan for debt consolidation mostly have a high score range, between 600 and 700. " \
                   "We can conclude that we can consider an approval of loan to this type of customers. " \
                   "The caveat is we need to pay attention to the loan maturity with this type of customers' since we doesn't have the data of " \
                   "how this type of customers' uses their money.")
    
    # eigth eda
    st.subheader("H. What's The Percentage of Male and Female With Approved Loan?")
    image_h1 = Image.open('H_1.png')
    st.image(image_h1, caption = "Customers' Percertange Based on Genders")
    with st.expander("Explanation"):
        st.caption("Based on the pie chart above, our customers' with approved loan are 55% male and 45% \Female. " \
                   "We have quite balanced customers' spreads, because the difference between male and female customer is under 10%.")
        