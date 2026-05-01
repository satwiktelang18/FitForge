import numpy as np

ACTIVITY_MAP = {
    'Sedentary (little/no exercise)': 1.2,
    'Light (1-3 days/week)': 1.375,
    'Moderate (3-5 days/week)': 1.55,
    'Active (6-7 days/week)': 1.725,
    'Very Active (athlete)': 1.9
}

def prepare_features(age, weight_kg, height_cm, gender_str, activity_str):
    gender = 1 if gender_str == 'Male' else 0
    activity = ACTIVITY_MAP[activity_str]
    bmi = weight_kg / ((height_cm / 100) ** 2)
    return [[age, weight_kg, height_cm, gender, activity, bmi]]