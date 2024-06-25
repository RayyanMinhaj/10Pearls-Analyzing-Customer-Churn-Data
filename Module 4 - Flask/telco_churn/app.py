from flask import Flask, request, jsonify
import pickle
import logging

app = Flask(__name__)

model_paths = ['models/lr_model.pkl', 'models/dt_model.pkl', 'models/rf_model.pkl', 'models/gb_model.pkl', 'models/svm_model.pkl']
models = [pickle.load(open(path, 'rb')) for path in model_paths]

# Set up logging - idk what this is but i am afraid to change it
logging.basicConfig(level=logging.DEBUG)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    logging.debug(f'Received data: {data}')
    
    model_index = data['model_index']
    features = data['features']
    
    model = models[model_index] #returns index 0,1,2,3,4 corresponding to each model
    prediction = model.predict([features])

    logging.debug(f'Prediction: {prediction}')
    return jsonify({'prediction': int(prediction[0])})  #sending the prediction back in integer format




@app.route('/health', methods=['GET'])
def health_check():
    return "API is running"




if __name__ == '__main__':
    app.run(debug=True)
