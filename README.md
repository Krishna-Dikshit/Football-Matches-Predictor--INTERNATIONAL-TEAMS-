# ⚽ Football Matches Predictor (International Teams)

A Machine Learning project that predicts football match outcomes using historical international match data.

This project demonstrates the full Data Science workflow including data cleaning, exploratory data analysis, feature engineering, and building a predictive model.

---

## 📊 Project Overview

The goal of this project is to predict the result of a football match (Home Win / Draw / Away Win) based on historical FIFA World Cup match data.

---

## 📁 Dataset

- Source: FIFA World Cup historical matches dataset
- Contains:
  - Match details (teams, goals, stadium, year)
  - Match outcomes
  - Tournament information

After cleaning:
- ~852 valid matches used for analysis

---

## 🧠 Machine Learning Approach

This project uses a supervised classification approach.

### Steps:
1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Label Encoding (Teams & Results)
5. Model Training (Random Forest Classifier)
6. Model Evaluation

---

## 📌 Features Used

- Home Team Name (encoded)
- Away Team Name (encoded)

---

## 🎯 Target Variable

- Match Result:
  - Home Win
  - Draw
  - Away Win

---

## 🤖 Model Used

- Random Forest Classifier
- Scikit-learn implementation
- Ensemble-based decision trees

---

## 📈 Results

- Model trained on historical FIFA World Cup matches
- Achieves reasonable accuracy for baseline prediction
- Evaluated using accuracy score and confusion matrix

---

## ⚠️ Limitations

- Does not include player-level data
- Does not include team form or FIFA rankings
- Only uses historical team identity as features
- Not suitable for betting or real-world prediction

---

## 🚀 Future Improvements

- Add FIFA rankings / Elo ratings
- Include player statistics
- Predict exact scorelines
- Build full World Cup tournament simulator
- Create web app using Streamlit

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## 📷 Sample Visualizations

(Add your plots here)

```markdown
![Match Results](images/match_results.png)
