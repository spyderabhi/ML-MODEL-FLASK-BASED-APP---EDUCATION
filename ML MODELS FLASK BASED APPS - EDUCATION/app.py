from flask import Flask, render_template, request
import numpy as np
from load_model import load_model
import xgboost as xgb

app = Flask(__name__)

try:
    model, scaler = load_model()
except Exception as e:
    print(f"Failed to load model or scaler: {e}")
    model = None
    scaler = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return render_template('index.html', error_message="Model or scaler not loaded. Check logs.")

    try:
        fields = ['SCHTOT', 'SCH1', 'SCH2', 'SCH3', 'TOTPOPULAT', 'P_SC_POP', 'P_ST_POP',
                  'SEXRATIO', 'OVERALL_LI', 'FEMALE_LIT', 'MALE_LIT', 'TCHTOT',
                  'TCHTOTG', 'TCHTOTM', 'AREA_SQKM']

        input_data = np.array([[float(request.form[field]) for field in fields]])

        # Scale input
        input_data_scaled = scaler.transform(input_data)

        # Convert to DMatrix for XGBoost Booster
        dmatrix = xgb.DMatrix(input_data_scaled)

        # Predict using Booster
        prediction = model.predict(dmatrix)

        prediction_text = f"The predicted enrollment total is: {prediction[0]:,.2f}"
        return render_template('result.html', prediction=prediction_text)

    except Exception as e:
        return render_template('index.html', error_message=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
