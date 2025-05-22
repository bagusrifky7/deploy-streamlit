# Prediction of Customers Loan Approval

## Repository Outline
1. P1M2_bagus_rifky.ipynb - Notebook filled preprocessing, model training, and model evaluation.
2. P1M2_bagus_rifky_inf - Notebook filled with model inference process.
3. P1M2_bagus_rifky_conceptual.txt - Txt filled with answer from conceptual questions.
4. loan_data.csv - Raw CSV file for this analysis
5. Deployment - Folder filled with file required for deployment

## Problem Background
Getting low-risk customers' has always be an objective of every business. To easier and faster prediction for customers' loan request, we will use machine learning model. We can compare 5 machine learning models that we will use on this analysis. The model that we will use are K-Nearest Neighbors, Decision Tree, Support Vector Machine, Random Forest, and Boosting. It is important for our's company to decrease the potential number of customers' that will make payments passed the due date.

## Project Output
The output for this project is customers' loan request can be approved or not.

## Data
Characteristics of my data have 14 column and 45000 rows, This dataset consist of:
- person_age column is filled with information of customers' age.
- person_gender column is filled with information of customers' gender.
- person_education column is filled with information of customers' level of education.
- person_income columnis filled with information of customers' annual income.
- person_emp_exp column is filled with infomation of customers' employments experience.
- person_home_ownership column is filled with information of customers' home ownership status.
- loan_amnt column is filled with information of customers' request amount of loan.
- loan_intent column is filled with information of customers' loan intention.
- loan_int_rate column is filled with information of customers' loan interest rate.
- loan_percent_income column is filled with information of customers' percentage of loan amount from annual income.
- cb_person_cred_hist_length column is filled with information of customers' length of credit history(in years).
- credit_score column is filled with information of customers' credit score.
- previous_loan_defaults_on_file is filled with informations of customers' previous loan defaults
- loan_status is filled with informations of customers' loan approval status.

## Method
We uses five supervised machine learning for this analysis. The five models is consist of K-Neares Neighbors, Support Vector Machine, Decision Tree, Random Forest Classifier, AdaBoost with Decision Tree as base model.

## Stacks
The packages I use on this project is Pandas, Numpy, Scikit-Learn, Scipy, and Matplotlib.

## Reference
Link to the dataset: https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data
---