import pandas as pd
import numpy as np

np.random.seed(42)
n = 2000

ages = np.random.randint(18, 65, n)
weights = np.random.uniform(50, 120, n)
heights = np.random.uniform(155, 195, n)
genders = np.random.choice([0, 1], n)
activity = np.random.choice([1.2, 1.375, 1.55, 1.725, 1.9], n)

bmr = np.where(
    genders == 1,
    88.362 + (13.397 * weights) + (4.799 * heights) - (5.677 * ages),
    447.593 + (9.247 * weights) + (3.098 * heights) - (4.330 * ages)
)
tdee = bmr * activity
noise = np.random.normal(0, 80, n)
calories = tdee + noise

df = pd.DataFrame({
    'age': ages,
    'weight_kg': weights,
    'height_cm': heights,
    'gender': genders,
    'activity_level': activity,
    'bmi': weights / ((heights / 100) ** 2),
    'calories_needed': calories.astype(int)
})

df.to_csv('data/raw_data.csv', index=False)
print(f"Dataset created: {len(df)} rows")
print(df.head())