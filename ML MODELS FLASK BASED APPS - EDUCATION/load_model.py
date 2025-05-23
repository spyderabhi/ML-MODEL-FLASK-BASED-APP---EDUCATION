import os
import pickle
import xgboost as xgb

def load_model():
    model_path = 'best_model.json'  # updated to .json
    scaler_path = 'data_scaler.pkl'

    if not os.path.exists(model_path) or os.path.getsize(model_path) == 0:
        raise FileNotFoundError(f"Model file '{model_path}' is missing or empty.")
    if not os.path.exists(scaler_path) or os.path.getsize(scaler_path) == 0:
        raise FileNotFoundError(f"Scaler file '{scaler_path}' is missing or empty.")

    # Load model using XGBoost Booster.load_model()
    model = xgb.Booster()
    model.load_model(model_path)

    # Load scaler with pickle
    with open(scaler_path, 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)

    return model, scaler
