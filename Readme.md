# 📱 Customer Churn Prediction System

## 📌 Project Overview

The Customer Churn Prediction System is a Machine Learning project that predicts whether a telecom customer is likely to leave (churn) or stay with the company.

This project follows a complete Machine Learning pipeline including:

- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Model Training
- Model Evaluation
- Feature Importance Analysis
- Model Saving
- Streamlit Deployment

---

## 🎯 Objective

The objective of this project is to help telecom companies identify customers who are likely to churn so they can take preventive actions such as offering discounts, improving customer support, or providing better service plans.

---

## 📂 Dataset

**Dataset Name:** Telco Customer Churn Dataset

The dataset contains information about telecom customers including:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract Type
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

**Target Variable**

- Churn (Yes / No)

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Streamlit

---

## 🤖 Machine Learning Models

The following models were trained and compared:

1. Logistic Regression
2. Random Forest Classifier
3. Gradient Boosting Classifier

### Model Comparison

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|---------:|----------:|--------:|---------:|
| Logistic Regression | 80% | 69% | 56% | 62% |
| Random Forest | 79% | 67% | 53% | 59% |
| Gradient Boosting | 81% | 71% | 58% | 64% |

### Best Model

Gradient Boosting Classifier

Accuracy: **81%**

---

## 📊 Model Evaluation

The selected model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix

---

## ⭐ Feature Importance

The top important features influencing churn include:

- Contract
- Tenure
- Monthly Charges
- Total Charges
- Internet Service
- Tech Support
- Online Security
- Payment Method
- Paperless Billing
- Dependents

---

## 💾 Saved Files

- churn_model.pkl
- scaler.pkl

---

## 📱 Streamlit Application

The project also includes a professional Streamlit application where users can:

- Enter customer information
- Predict customer churn
- View churn probability
- View customer risk level
- Get business recommendations

---

## 📁 Project Structure

```
Customer_Churn_Prediction/
│
├── Customer_Churn_Prediction.ipynb
├── streamlit_app.py
├── churn_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
├── screenshots/
└── dataset.csv
```

---

## ▶️ Installation

Clone the repository

```
git clone <repository_link>
```

Move to project folder

```
cd Customer_Churn_Prediction
```

Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run Streamlit App

```
streamlit run streamlit_app.py
```

---

## 📸 Screenshots

Project screenshots include:

- Dataset Preview
- Churn Distribution
- Monthly Charges Distribution
- Correlation Heatmap
- Model Comparison
- Confusion Matrix
- Feature Importance
- Streamlit Dashboard
- Prediction Result

---

## 👩‍💻 Developer

**Ayesha Imran**

BS Artificial Intelligence

Pakistan

---

## 📜 License

This project is developed for educational and internship purposes.