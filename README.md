# Analyzing Customer Churn Data

> People come and go, services stay!
> 

### What is Churn?

**Telecommunication churn** refers to the phenomenon where customers of a telecom service provider discontinue their service or switch to another provider. Churn can be voluntary (when customers actively choose to switch providers) or involuntary (when customers are disconnected by the provider due to non-payment or other reasons). 

![Untitled](Analyzing%20Customer%20Churn%20Data%209d9ea17ffff94dc39445f78f1b789f09/Untitled.png)

By understanding the factors driving churn and implementing effective retention strategies, telecom companies can improve customer satisfaction, enhance loyalty, and ensure sustained growth.

## Module 1: **Data Preprocessing, Exploratory Data Analysis (EDA), and Feature Engineering**

- The Telco Customer Churn Dataset focuses on customer churn for a telecommunications company, containing information on customer demographics, services, account information, and churn status.
- The overview lets us know that there are no missing values in the dataset, however, some features have multiple values referring to “No” with additional textual context, which are standardized for consistency.
- Customers with lower tenure show a higher likelihood of churn.
- Higher monthly charges are associated with a higher likelihood of churn.
- Total charges follow a right-skewed distribution, with most customers generating lower total charges.
- Monthly charges are widely distributed, peaking around the mid-range, indicating varied customer billing amounts.
- We balanced the abundant/under sampled data by using Synthetic Minority Oversampling Technique (SMOTE) — also known as Synthetic Data!

![Untitled](Analyzing%20Customer%20Churn%20Data%209d9ea17ffff94dc39445f78f1b789f09/Untitled%201.png)

- Churn has a relatively strong positive correlation with MonthlyCharges and Contract_Month-to-month, indicating customers with higher monthly charges and month-to-month contracts are more likely to churn.
- Churn has a negative correlation with tenure, Contract_One year, and Contract_Two year, suggesting customers with longer tenure and longer contracts are less likely to churn.

---

## Module 2: **AI Algorithms, Model Training, Tuning, and Results**

For this section, we’re going to be using a set of Machine Learning algorithms and evaluating their performance in order to give us better insight into predicting customer churn.

| Model Name | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| --- | --- | --- | --- | --- | --- |
| Logistic Regression | 0.860232 | 0.877397 | 0.834528 | 0.855426 | 0.935692 |
| Decision Trees | 0.804713 | 0.800000 | 0.807818 | 0.803890 | 0.805279 |
| Random Forest | 0.855713 | 0.871078 | 0.831922 | 0.851050 | 0.927770 |
| Gradient Boosting | 0.859587 | 0.862319 | 0.852769 | 0.857517 | 0.936491 |
| Support Vector Machines | 0.851517 | 0.880936 | 0.809722 | 0.843856 | 0.927816 |
| Decision Level Fusion | 0.861201 | 0.874069 | 0.841042 | 0.857238 | 0.933898 |

### Logistic Regression

- Logistic Regression performs the best in terms of accuracy (86%), precision, recall, and F1 score. The ROC-AUC score indicates it has a strong ability to distinguish between classes.
- Logistic Regression works well when the relationship between features and the target is roughly linear.

### Decision Trees

- Decision trees end up providing the lowest accuracy (80.4%) out of all the models which could be because Decision Trees are prone to overfitting, especially with noisy data or when the tree becomes too complex.
- The performance might be affected by the lack of sufficient depth or pruning.

### Random Forest

- Random Forest performs well, with high accuracy (85.5%) and balanced precision and recall. It handles overfitting better than Decision Trees by averaging multiple trees.
- The slightly lower performance compared to Gradient Boosting might be due to the way trees are combined (majority voting vs. boosting).

### Gradient Boosting

- Gradient Boosting shows the best performance among all models in terms of ROC-AUC (93.6%), indicating strong classification capabilities. It builds trees sequentially, focusing on correcting errors from previous trees, which often leads to better performance (and reduced overfitting).

### Support Vector Machines

- SVM performs well with high precision (88%) and a good balance of other metrics. The performance might slightly lag behind Gradient Boosting due to its sensitivity to the correct choice of kernel and regularization parameters.

### Ensemble (Decision-Level Fusion - Majority Voting)

- Decision-level fusion involves combining the outputs (decisions) of individual classifiers using methods such as majority voting, weighted voting, or stacking. Were going to be using Majority Voting.
- It provides us with a slightly higher accuracy of 86.12%

The optimized final models are used to generate predictions on the test dataset and exported as pickle files. The predicted probabilities of churn are obtained for each customer.

![Untitled](Analyzing%20Customer%20Churn%20Data%209d9ea17ffff94dc39445f78f1b789f09/Untitled%202.png)

---

## Module 3: **Databases, SQL, and Queries**

A PostgreSQL database schema is created to store the processed data and predictions. Tables are designed to efficiently store customer information, features, and churn predictions. 

Using pgAdmin4 we are able to run queries and visualize results to make more informed correlations between churn and customer features.

![Untitled](Analyzing%20Customer%20Churn%20Data%209d9ea17ffff94dc39445f78f1b789f09/Untitled%203.png)

### **Data Ingestion**

Processed data is ingested into the PostgreSQL database using SQL scripts. Indexing and optimization techniques are applied to ensure fast query performance.

### Insights we are able to drive using Queries

- There are 2058 customers with less than a tenure of one year
- There are 3105 customers with less than a tenure of two years
- There are 3833 customers with a tenure of more than two years
- Maximum tenure is of 72 months and there are 362 customers with this tenure
- Minimum tenure is of 1 months and there are 613 customers with this tenure
- The lowest monthly charge is $18.25
- The maximum monthly charge is $118.75
- The average monthly charge is $64.7
- There are 3130 customers with monthly charges less than $65 (Average)
- There are 3897 customers with monthly charges greater than $65 (Average)
- There are 3875 customers who opted for a Month-to-Month contract type
- There are 1472 customers who opted for a One Year contract type
- There are 1685 customers who opted for a Two Year contract type
- Total Number of Customers: 7032
- The Average Tenure is approx. 32 months
- Total Revenue generated is $16,055,091.45
- Number of predicted customers who have churned is 470
- All of the predicted churned customers had a Month-to-Month contract type
- Predicted customers who Churn have a average monthly charge of $81.37
- 428 of the predicted churn customers had Fiber Optic
- 42 of the predicted churn customers had DSL
- 344 of the predicted Churned customers used Electronic Checks as their payment method
- 47 of the predicted Churned customers used Mailed Checks as their payment method
- 34 of the predicted Churned customers used Credit Card as their payment method
- 45 of the predicted Churned customers used Bank transfer as their payment method

### Running Total

A running total (also known as a cumulative sum) is the sum of a sequence of numbers that is updated each time a new number is added to the sequence. It gives the total at each point in the sequence.

![Untitled](Analyzing%20Customer%20Churn%20Data%209d9ea17ffff94dc39445f78f1b789f09/Untitled%204.png)

### Moving Average

A moving average (also known as a rolling average) smooths out data by creating an average of different subsets of the full data set. It’s useful for identifying trends over time by filtering out short-term fluctuations.

![Untitled](Analyzing%20Customer%20Churn%20Data%209d9ea17ffff94dc39445f78f1b789f09/Untitled%205.png)

---

## Module 4: **Model Deployment, APIs, and Testing**

- The models we have trained can now be deployed using Flask to create a REST API for predicting whether a customer profile is likely to Churn or not based on the services they opt for.
- Multiple trained models are integrated into the deployment to allow for comparison and selection.
- Endpoints are created for predicting churn based on user inputs.
- A simple frontend interface is developed to allow users to select services and models.

![Untitled](Analyzing%20Customer%20Churn%20Data%209d9ea17ffff94dc39445f78f1b789f09/Untitled%206.png)

### **Documenting API Endpoint Usage**

This API allows users to predict whether a customer will churn based on various features related to the customer’s account and service usage. The prediction is made using one of several machine learning models.

### **Health Check Endpoint**

- This endpoint is used to check if the API is running
- **Request**: GET /health
- **Response**: 200 OK (status code) ; “API is running” (body)

### **Predict Churn Endpoint**

- This endpoint is used to predict whether a customer will churn based on the input features and selected model.
- **Request**: POST /predict
- **Headers**: Content-Type: application/json
- **Body:** model_index, features

---

## Conclusion

Predicting customer churn is crucial for telecommunications companies to retain customers and reduce revenue loss. By employing data preprocessing, exploratory data analysis, feature engineering, and model training techniques, we can build robust models to predict churn. Addressing class imbalance through techniques like SMOTE improves model performance. Storing and managing data in a PostgreSQL database allows for efficient querying and insight generation. Finally, deploying the model using Flask and integrating it with a user-friendly interface makes the solution accessible and practical. This comprehensive approach helps identify at-risk customers and take proactive measures to improve customer retention.