<div align="center">

<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-1.32-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Model-Random%20Forest-8A2BE2?style=for-the-badge"/>
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>

<br/><br/>

# FitForge — AI-Powered Fitness Planner

📊 **Predicts daily calorie needs and generates personalized workout & diet plans using Machine Learning**

</div>

---

## 🔭 Overview

FitForge is a lightweight **machine learning-based fitness planning system** that helps users build **data-driven workout and diet plans**.

It predicts daily calorie requirements using a trained ML model and maps user goals (fat loss, muscle gain, maintenance) to structured fitness routines — all through a fast, interactive web interface.

---

## ✨ Features

- 🧍 Input body metrics (**age, height, weight, goal**)  
- 🔥 Predict **daily calorie requirements (ML-based)**  
- 🏋️ Generate **goal-specific workout routines**  
- 🥗 Get **personalized diet recommendations**  
- 📊 Clean **Streamlit dashboard UI**  
- ⚡ Real-time fitness plan generation  
- 📈 Goal-based insights  

---

## 🖥️ Sample Flow

Enter your profile → Select fitness goal → Click **Generate Plan** → Get your complete AI-powered fitness roadmap instantly

---

## ⚙️ Installation

```bash
git clone https://github.com/satwiktelang18/FitForge.git
cd FitForge
pip3 install -r requirements.txt
```

---

## ▶️ Usage

```bash
streamlit run app.py
```

Open browser at: http://localhost:8501

---

## 🧠 How It Works

1. User inputs body metrics (age, height, weight, goal)  
2. Data is preprocessed and normalized  
3. ML model predicts daily calorie requirements  
4. Workout engine maps goal → structured routines  
5. Diet engine generates calorie-aligned meal plans  
6. Results displayed via Streamlit UI  

---

## 📊 Model Insights

- **Algorithm:** Random Forest Regressor  
- **Target Variable:** Daily Calorie Requirement  
- **Input Features:** Age, Height, Weight, Fitness Goal  

---

## 📊 Model Performance

- **Model:** Random Forest Regressor  
- **R² Score:** 0.9738  
- **MAE:** 81.95 calories  
- **RMSE:** 101.78 calories  

---

### 🔍 Key Insights

- The model explains **~97% of the variance** in calorie requirements (high predictive power)
- Average prediction error is **~82 calories**, which is reasonably low for fitness estimation
- Most important factor: **Activity Level**, followed by **Weight**

> Note: Model trained on structured fitness-related dataset. Performance may vary for real-world users.

---

## 🏗️ Project Structure

```bash
FitForge/
│
├── app.py
├── requirements.txt
│
├── data/
├── model/
│   ├── calorie_model.pkl
│   ├── train_model.py
│   └── evaluate.py
│
├── tracking/
│   └── progress_tracker.py
│
├── utils/
│   ├── diet_recommender.py
│   ├── workout_recommender.py
│   ├── macro_calculator.py
│   ├── predictor.py
│   └── preprocessing.py
```

---

## 🛠️ Tech Stack

- Python 3.11  
- Streamlit  
- scikit-learn  
- Pandas  
- NumPy  

---

## 🚀 Future Improvements

- [ ] Progress tracking dashboard  
- [ ] User authentication system  
- [ ] Deployment on Streamlit Cloud  
- [ ] Mobile optimization  
- [ ] Advanced ML personalization  

---

## 👨‍💻 Author

**Satwik Telang**
