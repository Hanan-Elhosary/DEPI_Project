
# Predictive Maintenance Project

## Project Overview
This project focuses on **Predictive Maintenance**, using machine learning to predict equipment failures before they occur, allowing for proactive interventions. Our goal is to classify machine status (No Failure or Failure) and predict potential failures to enhance preventive maintenance strategies.

---

## Team Members
- **Menna El Sayed** - [LinkedIn](https://www.linkedin.com/in/menna-elsayed-859b7628a)
- **Nourhan Ebrahim**
- **Hanan Elhosary** - [LinkedIn](http://www.linkedin.com/in/hanan-elsaid-elhosary)
- **Mariam Ahmed**

---

## Agenda
1. Problem Definition
2. Exploratory Data Analysis (EDA)
3. Modeling
4. Key Insights
5. Deployment

---

## Problem Description
- **Predictive Maintenance** is a data-driven approach to forecast machinery failures based on sensor readings, improving operational reliability.
- Key Objectives:
  1. Classify machine status (Failure/No Failure).
  2. Predict failures before they happen.
  3. Analyze sensor data to optimize operations.

---

## Real-World Impact
- **Reduced Costs:** Maintenance costs lowered by up to 20%.
- **Increased Equipment Lifespan:** Extended by 15-20%.
- **Minimized Downtime:** Unplanned downtimes are reduced.
- **Efficient Resource Use:** Repairs optimized, waste reduced.

---

## Data Preprocessing
1. **Outliers Removal:** Used Z-score method to handle extreme values.
2. **Column Handling:** Removed unnecessary columns like `UDI` and `Product ID`.
3. **Label Encoding:** Categorical features like `Type` were transformed into numerical values.
4. **PCA & SMOTE:** Applied PCA to reduce dimensionality and SMOTE to balance class distribution.

---

## Data Exploration
- Histograms, box plots, and heatmaps were used to understand data distribution and relationships.
- Correlations were observed between key variables like **Air Temperature**, **Process Temperature**, **Torque**, and **Rotational Speed**.

---

## Modeling
- Models applied:
  - **Support Vector Classifier (SVM)**: 91.2%
  - **Decision Tree Classifier**: 92%
  - **Random Forest Classifier**: 91.89% (tuned to 97.02% with Bayesian optimization)

---

## Deployment on Azure
- Data uploaded, processed, and transformed in **Azure Machine Learning Studio**.
- The trained model was deployed, creating a REST API endpoint for real-time predictions.
- The API was integrated into an HTML/CSS interface for seamless interaction with the deployed model.

---

## Predictive Log Analytics Project
A complementary project analyzing **log data** for system behaviors and anomalies using advanced ML models like **BERT**, **DistilBERT**, and **RoBERTa**. The highest performing model was **RoBERTa** with 96% accuracy.

---

## Contact
For further information, please feel free to reach out through the team members' LinkedIn profiles.
