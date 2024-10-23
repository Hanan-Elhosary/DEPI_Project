# Predictive Maintenance Project

"Unlocking the future of efficiency: Discover how predictive maintenance transforms operational challenges into proactive solutions, saving time, money, and resources."

## Team Members
- [Menna El Sayed](https://www.linkedin.com/in/menna-elsayed-859b7628a)
- [Hanan Elhosary](http://www.linkedin.com/in/hanan-elsaid-elhosary)
- [Nourhan Ebrahim](https://www.linkedin.com/in/norhan-ebrahim-87b32725a)
- [Mariam Ahmed](https://www.linkedin.com/in/norhan-ebrahim-87b32725a)

## Agenda
1. Problem
2. Exploratory Data Analysis (EDA)
3. Modeling
4. Key Insights
5. Deployment

## Project Overview
Predictive maintenance is a data-driven approach that helps industries predict equipment failures before they occur. This project aims to:

1. Classify machine status as either "No Failure" or "Failure".
2. Predict failures to enable preventive maintenance.
3. Leverage sensor data to understand operational conditions leading to failures, improving system reliability.

## Real-World Impact
- **Reduced Costs**: Lowers maintenance expenses.
- **Increased Equipment Lifespan**: Extends machine lifespan by 15-20%.
- **Minimized Downtime**: Reduces unplanned downtimes.
- **Efficient Resource Utilization**: Optimizes repairs and reduces waste.

## Steps in the Project

### Data Cleaning
- **Outliers**: Removed using Z-score to prevent bias from abnormal data points.
- **Irrelevant Columns**: "UDI" and "Product ID" were removed as they don't provide meaningful information for modeling.

### Data Transformation
- **Label Encoding**: Converted categorical features into numerical values.
- **Standardization**: Ensured all features contribute equally to the analysis.
- **PCA**: Applied to reduce dimensionality and enhance visualization.
- **SMOTE**: Used to handle class imbalance by generating synthetic samples.

### Exploratory Data Analysis (EDA)
- **Heatmaps**: Showed key feature correlations (e.g., air temperature and process temperature).
- **Pair Plots**: Helped identify patterns and trends.
- **Profile Report**: Generated a comprehensive summary, including data types, distributions, correlations, and outliers.

### Modeling
- **Support Vector Classifier**: Achieved 91.2% accuracy.
- **Decision Tree Classifier**: Achieved 92% accuracy.
- **Random Forest Classifier**: Achieved 91.89% accuracy before hyperparameter tuning.
- **Hyperparameter Tuning**: Bayesian optimization was applied, leading to an improved Random Forest accuracy of 97.02%.
- **Model Monitoring**: Used MLflow to track model performance, visualizing metrics like accuracy, AUC-ROC curves, and confusion matrices.

### GANs for Data Generation
- **CTGAN**: Used to generate synthetic tabular data, retaining statistical properties of the original dataset.
- **Random Forest Testing**: Tested the usability of the generated data with a Random Forest classifier.

## Azure Simulation Workflow
1. **Data Upload**: Imported the dataset into Azure.
2. **Data Preprocessing**: Cleaned and transformed the data.
3. **Model Training**: Used a two-class Decision Tree model.
4. **Model Scoring & Evaluation**: Assessed performance with evaluation metrics.
5. **Deployment**: Deployed the trained model using a REST API for real-time predictions.

## Predictive Log Analytics
- This project analyzed log data to classify and categorize events, improving system behaviors and identifying anomalies. It utilized advanced machine learning techniques to enhance operational efficiency.

### Dataset
- **BGL Dataset**: Logs collected from a BlueGene/L supercomputer system.
- **Rows**: 2000
- **Columns**: 13 (2 integer columns and 11 string columns)

### Data Cleaning & Transformation
- Converted object types to string for consistency.
- Filled missing values to improve data quality.

### Modeling
- Trained three transformer models (BERT, DistilBERT, and RoBERTa) on log data:
  - **BERT**: 94.00% accuracy
  - **DistilBERT**: 94.00% accuracy
  - **RoBERTa**: 96.00% accuracy
- **Conclusion**: RoBERTa outperformed both BERT and DistilBERT, making it the best model for log data classification.

## Conclusion
Predictive Maintenance and Predictive Log Analytics provide proactive solutions for reducing downtime, extending equipment lifespan, and optimizing resources. Leveraging machine learning models such as Random Forest and RoBERTa enhances prediction accuracy, making these approaches highly effective in industrial applications.

---

Thank you for exploring our project! Feel free to reach out for any further information.
accuracy.

---

## Contact
For further information, please feel free to reach out through the team members' LinkedIn profiles.
