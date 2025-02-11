import streamlit as st
import pickle
import pandas as pd

# Title
st.title('Car Price Prediction App')

st.write('This web app predicts the **Car Purchase Amount** based on customer features.')

#to read the model from the pickle file
model=pickle.load(open('car_model.pkl','rb'))

# get input from the user, features: gender, age, annual salary, credit card debt, net worth

Gender=st.number_input('Gender 0: male 1: Female')
Age=st.number_input('Age min:20 max: 70')
annual_salary=st.number_input('Annual Salary ($) min:20,000 max: 100,000')
credit_card_debt=st.number_input('Credit Card Debt ($) min:100 max: 20,000')
net_worth=st.number_input('Net Worth ($) min:20,000 max: 100,000')

# convert the user information in DataFrame

user_data=pd.DataFrame({
    'gender':Gender,
    'age':Age,
    'annual Salary':annual_salary,
    'credit card debt':credit_card_debt,
    'net worth':net_worth}, index=[0])

# predict the house proce
prediction=model.predict(user_data)

if st.button('Predict'):
        st.write(f'Predict Sales {prediction[0]:,.2f}')