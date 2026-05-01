import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import os

def train():
    df = pd.read_csv('data/raw_data.csv')
    
    features = ['age', 'weight_kg', 'height_cm', 'gender', 'activity_level', 'bmi']
    target = 'calories_needed'
    
    X = df[features]
    y = df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=10,
        min_samples_split=5,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    
    # Evaluation
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print(f"MAE:  {mae:.2f} calories")
    print(f"RMSE: {rmse:.2f} calories")
    
    # Feature importance
    importances = pd.Series(model.feature_importances_, index=features)
    print("\nFeature Importances:")
    print(importances.sort_values(ascending=False))
    
    # Save model
    os.makedirs('model', exist_ok=True)
    joblib.dump(model, 'model/calorie_model.pkl')
    print("\nModel saved to model/calorie_model.pkl")
    
    return mae, rmse

if __name__ == '__main__':
    train()