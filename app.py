import pandas as pd
from flask import Flask, jsonify, request
import joblib
import os

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():

    req = request.get_json()
    
    input_data = req['data']
    input_data_df = pd.DataFrame.from_dict(input_data)

    model = joblib.load('model.pkl')

    
    # scale_obj = joblib.load('scale.pkl')

    # input_data_scaled = scale_obj.transform(input_data_df)

    # print(input_data_scaled)

    prediction = model.predict(input_data_df)

    if prediction[0] == 1.0:
        cancer_type = 'Malignant Cancer'
    else:
        cancer_type = 'Benign Cancer'
        
    return jsonify({'output':{'cancer_type':cancer_type}})
        

@app.route('/')
def home():
    return "Welcome to Breast cancer diagnostic center"


if __name__=='__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '3000'))