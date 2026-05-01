<div align="center">

<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-1.32-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Machine%20Learning-Calorie%20Prediction-6A5ACD?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Model-Random%20Forest-8A2BE2?style=for-the-badge"/>
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/Numerical-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
<img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>

<br/><br/>

# 💪 FitForge — AI-Powered Fitness Planner

**An intelligent AI fitness system that generates personalized workout routines, calorie targets, and diet strategies based on user body metrics and fitness goals — built with Python & Streamlit.**

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
- 📈 Goal-based insights (fat loss / bulking / maintenance)

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
4. Workout engine maps goal → structured training split  
5. Diet engine generates calorie-aligned meal plan  
6. Results displayed via Streamlit UI  

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

## 📊 Model Logic

- **Calorie Model** → Predicts daily energy requirements using ML  
- **Workout Engine** → Converts fitness goal → structured routine  
- **Diet Engine** → Generates calorie-matched meal plans  

---

## 🚀 Future Improvements

- [ ] Progress tracking dashboard  
- [ ] User authentication system  
- [ ] Cloud deployment (Streamlit Cloud)  
- [ ] Mobile optimization  
- [ ] Advanced ML personalization (Deep Learning)  

---

## 👨‍💻 Author

**Satwik Telang**
