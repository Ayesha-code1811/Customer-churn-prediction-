
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📱",
    layout="wide"
)

# ==========================
# Load Model & Scaler
# ==========================

model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")

# ==========================
# Custom CSS
# ==========================

st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

h1{
    color:#0E4D92;
    text-align:center;
}

h3{
    color:#0E4D92;
}

.stButton>button{
background:#0E4D92;
color:white;
border-radius:10px;
height:55px;
width:100%;
font-size:20px;
font-weight:bold;
}

.stButton>button:hover{
background:#1976D2;
color:white;
}

div[data-testid="stMetric"]{
background:white;
padding:15px;
border-radius:12px;
box-shadow:0px 0px 8px rgba(0,0,0,0.1);
}

.block{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 0px 10px rgba(0,0,0,0.08);
margin-bottom:20px;
}

.footer{
text-align:center;
font-size:15px;
color:gray;
margin-top:40px;
}

</style>
""",unsafe_allow_html=True)

# ==========================
# Sidebar
# ==========================

st.sidebar.image(
    "https://img.icons8.com/color/96/artificial-intelligence.png",
    width=80
)

st.sidebar.title("Customer Churn")

st.sidebar.markdown("---")

st.sidebar.success("Model Loaded Successfully")

st.sidebar.markdown("### 👩 Developer")
st.sidebar.info("Ayesha Imran")

st.sidebar.markdown("### 🤖 Machine Learning Model")
st.sidebar.info("Gradient Boosting Classifier")

st.sidebar.markdown("### 🎯 Accuracy")
st.sidebar.success("81%")

st.sidebar.markdown("### 📂 Dataset")
st.sidebar.info("Telco Customer Churn")

st.sidebar.markdown("---")

st.sidebar.write("Built using")
st.sidebar.write("✔ Python")
st.sidebar.write("✔ Streamlit")
st.sidebar.write("✔ Scikit-Learn")
st.sidebar.write("✔ Joblib")

# ==========================
# Header
# ==========================

st.markdown("""
<h1>📱 Customer Churn Prediction System</h1>
""",unsafe_allow_html=True)

st.markdown("""
<center>

Predict whether a telecom customer is likely to leave the company using Machine Learning.

</center>
""",unsafe_allow_html=True)

st.write("")

# ==========================
# Dashboard Cards
# ==========================

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric("Model","Gradient Boosting")

with c2:
    st.metric("Accuracy","81%")

with c3:
    st.metric("Dataset","7043 Rows")

with c4:
    st.metric("Features","19")

st.write("")
st.write("")

# ==========================
# Personal Information
# ==========================

st.markdown("<div class='block'>",unsafe_allow_html=True)

st.subheader("👤 Personal Information")

col1,col2=st.columns(2)

with col1:

    gender=st.selectbox(
        "Gender",
        ["Female","Male"]
    )

    senior=st.selectbox(
        "Senior Citizen",
        [0,1]
    )

    partner=st.selectbox(
        "Partner",
        ["No","Yes"]
    )

    dependents=st.selectbox(
        "Dependents",
        ["No","Yes"]
    )

    tenure=st.slider(
        "Tenure (Months)",
        0,72,12
    )

with col2:

    monthly=st.number_input(
        "Monthly Charges",
        0.0,
        150.0,
        70.0
    )

    total=st.number_input(
        "Total Charges",
        0.0,
        10000.0,
        1000.0
    )

st.markdown("</div>",unsafe_allow_html=True)

# ===================================================
# Service Information
# ===================================================

st.markdown("<div class='block'>",unsafe_allow_html=True)

st.subheader("🌐 Service Information")

c1,c2=st.columns(2)

with c1:

    phone=st.selectbox(
        "Phone Service",
        ["No","Yes"]
    )

    multiple=st.selectbox(
        "Multiple Lines",
        ["No","No phone service","Yes"]
    )

    internet=st.selectbox(
        "Internet Service",
        ["DSL","Fiber optic","No"]
    )

    security=st.selectbox(
        "Online Security",
        ["No","No internet service","Yes"]
    )

    backup=st.selectbox(
        "Online Backup",
        ["No","No internet service","Yes"]
    )

with c2:

    protection=st.selectbox(
        "Device Protection",
        ["No","No internet service","Yes"]
    )

    support=st.selectbox(
        "Tech Support",
        ["No","No internet service","Yes"]
    )

    tv=st.selectbox(
        "Streaming TV",
        ["No","No internet service","Yes"]
    )

    movies=st.selectbox(
        "Streaming Movies",
        ["No","No internet service","Yes"]
    )

st.markdown("</div>",unsafe_allow_html=True)

# ===================================================
# Billing Information
# ===================================================

st.markdown("<div class='block'>",unsafe_allow_html=True)

st.subheader("💳 Billing Information")

col1,col2=st.columns(2)

with col1:

    contract=st.selectbox(
        "Contract",
        ["Month-to-month","One year","Two year"]
    )

    paperless=st.selectbox(
        "Paperless Billing",
        ["No","Yes"]
    )

with col2:

    payment=st.selectbox(
        "Payment Method",
        [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ]
    )

st.markdown("</div>",unsafe_allow_html=True)

# ===================================================
# Label Encoding
# ===================================================

gender=1 if gender=="Male" else 0

partner=1 if partner=="Yes" else 0

dependents=1 if dependents=="Yes" else 0

phone=1 if phone=="Yes" else 0

paperless=1 if paperless=="Yes" else 0

multiple={
"No":0,
"No phone service":1,
"Yes":2
}[multiple]

internet={
"DSL":0,
"Fiber optic":1,
"No":2
}[internet]

security={
"No":0,
"No internet service":1,
"Yes":2
}[security]

backup={
"No":0,
"No internet service":1,
"Yes":2
}[backup]

protection={
"No":0,
"No internet service":1,
"Yes":2
}[protection]

support={
"No":0,
"No internet service":1,
"Yes":2
}[support]

tv={
"No":0,
"No internet service":1,
"Yes":2
}[tv]

movies={
"No":0,
"No internet service":1,
"Yes":2
}[movies]

contract={
"Month-to-month":0,
"One year":1,
"Two year":2
}[contract]

payment={
"Bank transfer (automatic)":0,
"Credit card (automatic)":1,
"Electronic check":2,
"Mailed check":3
}[payment]

# ===================================================
# Prediction Button
# ===================================================

st.write("")

if st.button("🔍 Predict Customer Churn"):

    # Input DataFrame (IMPORTANT: Same order as training)
    input_df = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple,
        "InternetService": internet,
        "OnlineSecurity": security,
        "OnlineBackup": backup,
        "DeviceProtection": protection,
        "TechSupport": support,
        "StreamingTV": tv,
        "StreamingMovies": movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }])

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.write("")
    st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.error("❌ Customer is likely to Churn")
    else:
        st.success("✅ Customer is NOT likely to Churn")

    # Probability
    st.write(f"### 📈 Churn Probability: **{probability*100:.2f}%**")
    st.progress(float(probability))

    # Risk Level
    st.write("### 🚦 Risk Level")

    if probability < 0.30:
        st.success("🟢 Low Risk")
    elif probability < 0.70:
        st.warning("🟡 Medium Risk")
    else:
        st.error("🔴 High Risk")

    # Recommendations
    st.write("### 💡 Business Recommendation")

    if prediction == 1:
        st.warning("""
- 🎁 Offer a special discount
- 📞 Contact the customer personally
- 📦 Recommend a long-term contract
- ⭐ Improve customer support
""")
    else:
        st.success("""
- 😊 Customer is likely to stay
- 💙 Maintain good service quality
- 🎉 Offer loyalty rewards
""")

# ===================================================
# Footer
# ===================================================

st.markdown("---")

st.markdown(
    """
    <div class="footer">
        <h4>📱 Customer Churn Prediction System</h4>
        <p>Developed by <b>Ayesha Imran</b></p>
        <p>Built with ❤️ using Python, Scikit-Learn & Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)
