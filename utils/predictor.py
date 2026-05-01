import joblib
from utils.preprocessing import prepare_features

def predict_calories(age, weight_kg, height_cm, gender, activity):
    model = joblib.load('model/calorie_model.pkl')
    features = prepare_features(age, weight_kg, height_cm, gender, activity)
    return int(model.predict(features)[0])