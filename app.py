import streamlit as st
import joblib
import pandas as pd
model = joblib.load('Bank churn prediction/model.pkl')

st.markdown(
    "<h1 style='text-align: center; color: #2E86AB;'>Bank Churn Predictor</h1>",
    unsafe_allow_html=True
)
st.markdown("""
    <p style='text-align: center; color: gray; font-size: 18px; margin: auto; display: block;'>
        Enter customer details below to predict if they will churn
    </p>
""", unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #2E86AB;'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    CreditScore = st.number_input('Credit Score', min_value=300, max_value=850)
    Geography = st.selectbox('Geography', ['France', 'Spain', "Germany"])
    Gender = st.selectbox('Gender', ['Male', 'Female'])
    Age = st.number_input('Age', min_value=18,  max_value=100)
    Tenure = st.number_input("Tenure", min_value=0, max_value=10)

with col2:
    Balance = st.number_input("Balance", min_value=0.0)
    NumOfProducts = st.number_input("Number Of Products", min_value=0, max_value=4)
    HasCrCard = st.selectbox("Has credit Card", ['No', 'Yes'])
    IsActiveMember = st.selectbox("Is Active Member", ['No', 'Yes'])
    EstimatedSalary = st.number_input('Estimated Salary', min_value=0.0)

if HasCrCard == "Yes":
    HasCrCard = 1
else:
    HasCrCard = 0

if IsActiveMember == "Yes":
    IsActiveMember = 1
else:
    IsActiveMember = 0

st.markdown("<br>", unsafe_allow_html=True)

if st.button('Predict'):
    input_data = pd.DataFrame([[CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]],
                               columns=['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary'])
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)
    churn_probability = round(probability[0][1] * 100, 2)
    
    if prediction[0] == 1:
        st.error(f"⚠️ This customer is likely to churn! ({churn_probability}% probability)")
    else:
        st.success(f"✅ This customer is not likely to churn. ({churn_probability}% probability)")

    # st.markdown("### Why this prediction?")
    # # Churn rate by Geography
    # geo_churn = df.groupby('Geography')['Exited'].mean() * 100
    # st.bar_chart(geo_churn)