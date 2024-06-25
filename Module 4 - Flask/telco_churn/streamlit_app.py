import streamlit as st
import requests

#All the features and their options in a as key values pair
categorical_features = {
    'gender': ['Female', 'Male'],
    'SeniorCitizen': ['0', '1'],
    'Partner': ['No', 'Yes'],
    'Dependents': ['No', 'Yes'],
    'PhoneService': ['No', 'Yes'],
    'MultipleLines': ['No', 'Yes'],
    'InternetService': ['DSL', 'Fiber optic', 'No'],
    'OnlineSecurity': ['No', 'Yes'],
    'OnlineBackup': ['No', 'Yes'],
    'DeviceProtection': ['No', 'Yes'],
    'TechSupport': ['No', 'Yes'],
    'StreamingTV': ['No', 'Yes'],
    'StreamingMovies': ['No', 'Yes'],
    'Contract': ['Month-to-month', 'One year', 'Two year'],
    'PaperlessBilling': ['No', 'Yes'],
    'PaymentMethod': ['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check']
}

#We have only 3 numerical features
numerical_features = ['tenure', 'MonthlyCharges', 'TotalCharges']

#Titles and stuff
st.title('10Pearls - Telco Customer Churn Prediction')
st.write('Analysing Customer Churn Data - Predicting Behavior to Retain Customers')
st.write('Rayyan Minhaj - Data Science Intern')
st.markdown("""---""")
st.write('')
st.title('Create a Customer')
st.write('')




#DROP DOWN FOR MODELS
model_option = st.selectbox(
    'Select Model',
    ('Linear Regression', 'Decision Trees', 'Random Forest', 'Gradient Boosting', 'SVM')
)

model_mapping = {
    'Linear Regression': 0,
    'Decision Trees': 1,
    'Random Forest': 2,
    'Gradient Boosting': 3,
    'SVM': 4
}

#DROP DOWN FOR CATEGORICAL FEATURES - not going to lie, this was done by chatgpt :)
input_data = {} #these are going to be the values i send to my models pickle file for prediction

for feature, options in categorical_features.items(): #for all my features in categorical_feature dict, create:
    selected_option = st.selectbox(f'Select {feature}', options) #first create the boxes
    for option in options: #then create as many drop down options as there are in my values of that feature
        input_data[f'{feature}_{option}'] = 1 if option == selected_option else 0 #since we have 2 of every option, make the selected option as 1 rest 0

#NUMERICAL INPUT FOR NUMERIC FEATURES
for feature in numerical_features:
    input_data[feature] = st.number_input(f'Enter {feature}', min_value=0.0)


#PREDICT BUTTON
if st.button('Predict'):
    model_index = model_mapping[model_option]
    features_values = list(input_data.values())

    #payload which we will send by api consists of model name and features
    #model name so that it can open that specific model in /predict
    payload = {
        'model_index': model_index,
        'features': features_values
    }

    response = requests.post('http://127.0.0.1:5000/predict', json=payload)
    #st.write(f'Status code: {response.status_code}')
    #st.write(f'Response: {response.text}')
    
    prediction = response.json()['prediction'] #getting the response here
    if prediction:
        st.error('Customer is likely to Churn!')
    else:
        st.success('Customer is not likely to Churn')
    
    
    #if response.status_code == 200:
    #    prediction = response.json()['prediction']
    #    st.write(f'Prediction: {"Churn" if prediction else "No Churn"}')
    #else:
    #    st.write('Error in prediction request')
