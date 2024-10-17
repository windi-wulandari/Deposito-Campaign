<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1k13Bw7WwHaIotaWjNy1wuA1qp1VFVOAt" alt="My Image" width="900" height="200">
</p>

---

# Repository Overview

1. **[Dataset](https://colab.research.google.com/drive/1pufeP0nLc76_4ZSM7x-F8rd5BF0ZYcAO?usp=sharing)**
   This repository contains 3 CSV files used for various purposes in analysis and deployment:

   - **`bank-additional-full.csv`**: The initial dataset from UCI containing full information about the data that will be used for modeling.
   - **`df2_processed.csv`**: A dataset that has undergone cleansing and feature engineering, ready for further processing and analysis to gain business insights.
   - **`sample_input.csv`**: A dataset used as test data for predictions in the local web app that has been created.

2. **[Notebook](https://github.com/windi-wulandari/Deposito-Campaign/tree/main/Notebook)**
   There are 3 main notebooks used for various purposes such as analysis, business insights, and modeling:

   - **`EDA_&_Pre_processing.ipynb`**: A notebook containing Exploratory Data Analysis (EDA) focused on data cleansing and feature engineering.
   - **`EDA_Business_Insights.ipynb`**: A notebook dedicated to extracting and exploring business insights from cleaned data.
   - **`Modelling.ipynb`**: A notebook containing advanced preprocessing specifically for modeling, business simulations, and preparation for deployment.

3. **[Deployment](https://github.com/windi-wulandari/Deposito-Campaign/tree/main/Deployment)**
   File and folder structure for deploying the web application built with Flask:

   - **`app.py`**: The main file containing Flask code to run the web app, allowing users to make predictions.
   - **`model_deposito_all_in_one.pkl`**: A pickle file containing the model, target encoder, and encoding sequence. This file enables the app to make predictions based on user input.
   - **`templates/`**: A folder containing HTML files for the user interface.
     - **`index.html`**: The main page displaying the input form to users.
     - **`predict.html`**: A page that displays prediction results.
   - **`static/`**: A folder storing static files like CSS for styling the interface.
     - **`style.css`**: The CSS file used for styling the user interface.

4. **[Assets](https://github.com/windi-wulandari/Deposito-Campaign/tree/main/Assets)**
   There is an **`assets/`** folder containing images used in the README file, illustrating the app interface and analysis processes.

---

# **Background of the Problem**

In the context of the global economic crisis that began in 2008, a bank in Portugal launched a promotional campaign for term deposit products. Out of a total of 41,188 target customers, 11.3% were successfully converted into clients for the product. This achievement is considered standard given the challenging economic situation, but the fact that 88.7% of target customers did not respond positively indicates significant room for improvement.

Applying machine learning for predictive modeling is recommended as a promising solution to significantly improve the conversion rate. Compared to traditional methods such as statistical analysis, manual segmentation, or rule-based systems, machine learning offers advantages in analyzing complex data, higher predictive accuracy, more effective campaign personalization, and adaptability to market changes. This recommendation is backed by projections that show a potential 30% increase in conversion rates. With a large customer base, this percentage increase can have a substantial impact.

---

# **Goal**

**Optimize the term deposit campaign through predictive modeling to increase conversion and cost efficiency amid economic challenges.**

---

# **Objectives**

- Optimize campaign cost-efficiency by minimizing unnecessary expenses while still achieving desired results. The focus is on reducing cost per customer without sacrificing campaign quality.
- Increase the conversion rate through more effective and targeted marketing strategies, with the goal of converting more prospects into customers in each campaign.
- Lower customer acquisition costs by implementing efficient marketing strategies, using fewer resources to acquire each new customer, thus increasing profit per customer.
- Improve Return on Investment (ROI) for marketing campaigns by maximizing the revenue generated from each expense. The focus is on getting more value from each investment through optimized processes and strategies, leading to higher profits in every campaign.

---

# **Metrics**

**Business Metrics**

1. **Saving Cost**: Optimizing campaign spending by reducing inefficient costs. The target is to achieve a 60% cost savings compared to the baseline, while maintaining campaign efficiency.
2. **Conversion Rate (Percent)**: Increasing the percentage of conversions from prospects to customers. The target is to improve the conversion rate by 20% compared to the baseline for more optimal prospect-to-customer conversions.
3. **Customer Acquisition Cost (CAC)**: Lowering the cost per customer acquired. The target is to reduce CAC by 60% compared to the baseline, to improve customer acquisition cost-efficiency.
4. **Return on Investment (ROI)**: Measuring campaign effectiveness based on the profit generated compared to the cost incurred. The target is to increase ROI by 50% compared to the baseline, ensuring expenditures result in stable and significant profits.

**Model Metrics**
- **Recall**: Important for avoiding lost business opportunities. With high recall, the bank can identify most potential customers. If recall is high, the model successfully identifies the majority of customers who will open a deposit, ensuring the bank does not miss out on potential customers.
- **ROC-AUC**: Suitable for imbalanced data and provides a comprehensive view of model performance. ROC-AUC measures the model's ability to distinguish between customers who will and will not open a deposit, balancing the resulting confusion matrix.

---

# **About the Dataset**

This dataset is based on the **["Bank Marketing" UCI dataset](http://archive.ics.uci.edu/ml/datasets/Bank+Marketing)**. The data has been enriched with the addition of five new social and economic features/attributes (national indicators from a country with a population of around ~10 million), published by **[Banco de Portugal](https://www.bportugal.pt/estatisticasweb)**. The dataset contains **41,188 rows**, with columns as follows:

Table 1. Data Dictionary

| **Column Name**      | **Description**                                                                                            | **Data Type** |
|----------------------|------------------------------------------------------------------------------------------------------------|---------------|
| `age`                | Age of the bank client                                                                                      | Numeric       |
| `job`                | Type of job the client has                                                                                  | Categorical   |
| `marital`            | Marital status of the client                                                                                | Categorical   |
| `education`          | Education level of the client                                                                               | Categorical   |
| `default`            | Does the client have any defaulted credit?                                                                  | Categorical   |
| `housing`            | Does the client have a housing loan?                                                                        | Categorical   |
| `loan`               | Does the client have a personal loan?                                                                       | Categorical   |
| `contact`            | Type of communication used in the last contact                                                              | Categorical   |
| `month`              | Last contact month                                                                                          | Categorical   |
| `day_of_week`        | Last contact day of the week                                                                                | Categorical   |
| `duration`           | Last contact duration in seconds                                                                            | Numeric       |
| `campaign`           | Number of contacts performed during this campaign for the client                                             | Numeric       |
| `pdays`              | Number of days since the client was last contacted in a previous campaign (999 if never contacted)           | Numeric       |
| `previous`           | Number of contacts before this campaign                                                                     | Numeric       |
| `poutcome`           | Outcome of the previous marketing campaign                                                                  | Categorical   |
| `emp.var.rate`       | Employment variation rate - quarterly indicator                                                             | Numeric       |
| `cons.price.idx`     | Consumer price index - monthly indicator                                                                    | Numeric       |
| `cons.conf.idx`      | Consumer confidence index - monthly indicator                                                               | Numeric       |
| `euribor3m`          | 3-month Euribor rate - daily indicator                                                                      | Numeric       |
| `nr.employed`        | Number of employees - quarterly indicator                                                                   | Numeric       |
| `y`                  | Has the client subscribed to a term deposit?                                                                | Binary        |

---

# **EDA & Pre-Processing**

Table 2. EDA & Pre-Processing

| **EDA & Pre-Processing Steps**       | **Description**                                                                 |
|--------------------------------------|---------------------------------------------------------------------------------|
| Remove missing values                | Remove rows/columns containing 'unknown' values considered as missing values.   |
| Handle duplicates                    | Identify and remove duplicate rows throughout the dataset.                      |
| Feature Engineering                  | Add 16 new columns resulting from additional analysis and relevant feature combinations. |
| Business Insight                     | Analyze to extract business insights from the data.                             |
| Remove biased features               | Remove theoretically or business-biased features, such as `durations`, `emp.var.rate`, and `nr.employed`. |
| Remove features with many categories | Remove features with too many categories, as they can increase complexity without adding value. |
| One-hot encoding                     | Apply one-hot encoding to nominal categorical features to convert them into numeric form. |
| Label encoding                       | Apply label encoding to ordinal categorical features to maintain category order. |
| Split data                           | Split data into 70% for training and 30% for testing.                           |
| Handle class imbalance               | Address class imbalance in training data using SMOTE (Synthetic Minority Over-sampling Technique). |

---

# **Business Insights**

Several business insights have been discovered, accessible in the **[EDA: Business Insights Notebook](https://github.com/windi-wulandari/Deposito-Campaign/blob/main/Notebook/EDA_Business_Insights.ipynb)**. However, this discussion will focus on the **3-Month Euribor Rate**, which significantly influenced deposit decisions during the crisis.

**Figure 1.**

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1x-Pk7nGKcKg6NZC9JsAEPp4lVJE2qMch" alt="Description Image"
</p>


Before 2008, higher interest rates tended to encourage people to save more money. However, after the 2008 financial crisis, this pattern changed drastically. Low interest rates have now become the primary driver for individuals to save more in response to the economic uncertainty that has arisen, as can be seen in Figure 1.

From 2008 to 2010, Portugal experienced significant economic turmoil due to the global financial crisis and the European debt crisis. During this period, there was an interesting phenomenon where lower interest rates (Euribor 3M) correlated with an increase in term deposits. This shows that in times of economic instability, low interest rates can encourage people to prefer saving their money in deposits, which are considered safer compared to other riskier investments.

**Possible Causes:**
- **Economic Uncertainty:** When people feel uncertain about the future of the economy, they tend to save more as a precautionary measure.
- **Limited Investment Alternatives:** During a crisis, safe investment options become more limited, pushing people to choose deposits as a more stable option.
- **Perceived Risk:** Low interest rates provide a sense of security, making people feel more comfortable saving money in deposits, even though the returns are lower.

With this understanding, we can see how the **Euribor 3 Month** played a role in influencing people's saving behavior during the crisis, as well as the reasons behind the increase in deposits despite low interest rates.

---

# **Modeling**

Table 3. Model Evaluation

| Model                           | Data              | Recall | ROC-AUC |
|---------------------------------|-------------------|--------|---------|
| **Logistic Regression**         | Cross-Val Train   | 0.87   | 0.95    |
|                                 | Cross-Val Test    | 0.84   | 0.94    |
| **Decision Tree**               | Cross-Val Train   | 1.00   | 1.00    |
|                                 | Cross-Val Test    | 0.89   | 0.89    |
| **Decision Tree Tuning 1**      | Cross-Val Train   | 0.93   | 0.99    |
|                                 | Cross-Val Test    | 0.86   | 0.91    |
| **Decision Tree Tuning 2**      | Cross-Val Train   | 0.61   | 0.80    |
|                                 | Cross-Val Test    | 0.60   | 0.80    |
| **XGBoost**                     | Cross-Val Train   | 0.93   | 0.99    |
|                                 | Cross-Val Test    | 0.87   | 0.97    |
| **XGBoost Tuning 1**            | Cross-Val Train   | 0.97   | 0.99    |
|                                 | Cross-Val Test    | 0.88   | 0.97    |
| **XGBoost Tuning 2**            | Cross-Val Train   | 0.93   | 0.97    |
|                                 | Cross-Val Test    | 0.89   | 0.96    |
| **🟩 XGBoost Tuning 3**          | Cross-Val Train   | 0.94   | 0.97    |
|                                 | Cross-Val Test    | 0.90   | 0.96    |


The best model generated from this analysis is XGBoost Tuning 3. This model shows the best performance with the highest recall on the test set, at 0.90. Additionally, it exhibits high stability in ROC AUC, with a value of 0.96. This indicates that XGBoost Tuning 3 is not only good at identifying positives but also has strong capability in distinguishing between positive and negative classes, making it the most effective choice for this application.

---

# **Business Simulation**

**Figure 2. Business Simulation**

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1Z4POFLq_GT46UUpprPfrmc_pDL24fP_r" alt="Deskripsi Gambar">
</p>

### **Conclusion**

This conclusion shows that the use of machine learning (ML) models not only meets the established targets but also exceeds expectations. With 100% optimization in cost savings compared to the baseline scenario, it is clear that ML models can significantly enhance operational efficiency. Moreover, the 28.66% increase in conversion rate indicates that ML usage can attract more customers at a lower cost.

A 78.34% reduction in customer acquisition costs compared to the baseline method further strengthens the evidence that ML-based strategies are far more effective in acquiring new customers. While the baseline scenario shows losses, ML implementation managed to achieve a 112% improvement. This highlights the great potential of ML technology in improving business performance and achieving better-than-expected results.

For detailed and clearer calculations, access the **[SpreedSheet](https://docs.google.com/spreadsheets/d/1ZVc7tCzEfSmsqYxFG-VR-BgNx5eoxaik3ZmFWb-uXJQ/edit?usp=sharing)** on the sheet **"Final Result (English Version)"**.

---

# **Deployment**

For deploying the machine learning model, the trained model is stored in binary object form. This method is highly suitable because it allows direct model usage for predictions without the need for retraining, saving time and resources. Storing it in a binary object format also ensures that all critical components, such as the target encoder and encoding sequence, are kept in one file. This makes model management easier and more structured.

**Latency and Batch Processing**

Using periodic batch processing can help manage latency. This approach is suitable for situations where predictions do not need to be made in real-time but can be done at certain intervals. This way, a batch of data can be processed at once, reducing server load and maximizing efficiency.

However, to provide direct prediction access via the web, Flask can be implemented. Flask allows the development of a web interface that enables users to interactively make predictions.

Before deploying, the first step to take is to save the model with the following code:

```python
# Combine all elements into a single dictionary
saved_objects = {
    'model': best_xgb2,
    'target_encoder': target_encoder,
    'encoding_order': encoding_order
}

# Save everything into a single pickle file
with open("model_deposito_all_in_one.pkl", "wb") as f:
    pickle.dump(saved_objects, f)

print("The model, target encoder, and encoding order have been saved in a single file 'model_deposito_all_in_one.pkl'")
```

*It's important to also save the label encoding so that during future predictions, the model can automatically convert the input data into the correct format. By including the target encoder and encoding order, all the steps necessary for processing the data can be done without manual intervention, increasing efficiency and consistency.*

After saving the model, the model, encoder, and encoding order can be reloaded using the following code:

```python
# Load the model, encoder, and encoding order from the saved file
with open("model_deposito_all_in_one.pkl", "rb") as file:
    loaded_objects = pickle.load(file)

# Extract the model, target encoder, and encoding order
model = loaded_objects['model']
target_encoder = loaded_objects['target_encoder']
encoding_order = loaded_objects['encoding_order']
```

**Project Deployment Structure**

After preparing the model, the project structure for deployment using Flask can be organized in the VSCode app as follows:

```
Your project name/
│
├── Deployment
│   ├── .venv
│   ├── app.py
│   ├── model_deposito_all_in_one.pkl
│   ├── templates/
│   │   ├── index.html
│   │   └── predict.html
│   └── static/
│       └── style.css
```

- **app.py**: The main file that contains Flask code to run the web application.
- **model_deposito_all_in_one.pkl**: A pickle file that stores the model, target encoder, and encoding sequence, allowing the app to make predictions based on user input.
- **templates/**: A folder containing HTML files for the user interface.
  - **index.html**: The main page for users.
  - **predict.html**: The page that displays prediction results.
- **static/**: A folder containing static files like CSS for styling.
  - **style.css**: A CSS file to manage the appearance of the user interface.

This is an overview of the created web app. Although it cannot be shown through a link because it hasn’t been hosted yet, you can try all the available code to run it in your local environment.

**Figure 3. Web Interface**

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1jah-UkzulTLss4gnhCrwH925Coq6zBr7" alt="Image Description">
</p>

<br>

**Figure 4. Web Interface for Prediction Results**

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1W5mukAVkk164SC-0yvxyOnf4zruYXKwW" alt="Image Description" >
</p>

This web app allows users to make predictions by manually filling in variables. Once the variables are filled in, the data is automatically encoded because the model and encoding settings have been pre-saved. For convenience, there is also an option to upload a CSV file. After the prediction process is complete, the result will be displayed with a "Yes" or "No" label. If the user uploads a CSV file, the prediction results will be shown in a table containing the input variables along with the predicted outcomes.

---

# **Limitation**

Although all steps have been completed and the application runs locally, hosting on a server remains a challenge that needs to be addressed in order for the app to be accessible to users on a wider scale. Additionally, to support batch processing latency, using Airflow as an orchestrator also presents a limitation that should be addressed in the next project.

---

References

Scientific papers supporting the arguments presented can be accessed **[here](https://drive.google.com/drive/folders/1WTW2cw4IhWioQx2NVF49ariBLobvS-4-?usp=sharing)**.
