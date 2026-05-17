# 🏠 MagicBricks House Price Predictor

> A Multiple Linear Regression model to predict residential property prices in Delhi using real-world MagicBricks data.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![R² Score](https://img.shields.io/badge/R²%20Score-~0.66-brightgreen)

---

## 📌 Overview

This project builds a **Multiple Linear Regression** model to estimate residential property prices in **Delhi** based on attributes like area, BHK, bathrooms, locality, furnishing status, and more — sourced from MagicBricks listings.

**Goal:** Help buyers, sellers, and analysts estimate realistic house prices using key property features.

---
## 🖥️ Demo

### Screenshots
<img width="640" height="319" alt="App Screenshot 1" src="https://github.com/user-attachments/assets/73dfe663-f0e9-49b2-8482-7a473262b723" />
<img width="637" height="299" alt="App Screenshot 2" src="https://github.com/user-attachments/assets/1b9e405e-4dae-4ed8-80ee-c2d1a8bfe807" />

### Video Walkthrough

https://github.com/user-attachments/assets/89d3a6e7-c19a-4c19-a8cb-dcfe8b8b81af

https://github.com/user-attachments/assets/276f364a-d9d1-4d18-b3fd-e265eb9d43ff

https://github.com/user-attachments/assets/ac484f15-166e-494c-9a94-15a6904c511c

---
## ✨ Features

- 📊 **Exploratory Data Analysis (EDA)** — distributions, correlations, and outlier investigation
- 🧹 **Data Preprocessing** — null handling, type correction, outlier removal
- 🔧 **Feature Engineering** — `Total_Rooms`, `Area_per_Room` derived features
- 🔢 **One-Hot Encoding** — categorical variables like locality and furnishing status
- 🤖 **Multiple Linear Regression** — trained with scikit-learn
- 📈 **Model Evaluation** — MAE, RMSE, and R² metrics
- 🌐 **Streamlit Web App** — interactive price prediction interface
- 🐳 **Docker Support** — fully containerized for easy deployment

---
## 📊 Model Performance

| Metric | Value |
|---|---|
| R² Score | ~0.66 |
| Mean Absolute Error | ₹X.XX Lakh |
| RMSE | ₹X.XX Lakh |

> Performance can be further improved using gradient boosting methods like XGBoost — see [Future Improvements](#-future-improvements).

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.11 |
| Data | Pandas, NumPy |
| ML | Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Web App | Streamlit |
| Deployment | Docker |

---

## 📁 Project Structure

```
house-price-app/
├── app.py                     # Streamlit web application
├── Dockerfile                 # Docker configuration
├── requirements.txt           # Python dependencies
├── .dockerignore              # Docker build optimisation
├── .gitignore
├── MagicBricks.csv            # Dataset
├── models/
│   ├── house_price_model.pkl  # Trained regression model
│   └── feature_columns.pkl    # Encoded feature columns
├── notebooks/
│   └── notebook.ipynb         # EDA, preprocessing & model training
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Docker (optional, for containerized run)

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd house-price-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

### 4. Run with Docker

```bash
docker build -t house-price-app .
docker run -p 8501:8501 house-price-app
```

Then open your browser at → `http://localhost:8501`

---

## 📈 Key Insights

- **Area** is the strongest predictor of price
- **Locality** introduces significant price variation across Delhi neighborhoods
- **Bathrooms** and **BHK count** positively correlate with price
- **Furnishing status** and **property type** add measurable valuation differences

---

## 🔮 Future Improvements

- [ ] Upgrade to **XGBoost / Gradient Boosting** for better accuracy
- [ ] Hyperparameter tuning with GridSearchCV / Optuna
- [ ] Add floor number and property age as features
- [ ] Enrich locality data with proximity to metro/schools/hospitals
- [ ] Deploy on **Render / Railway / Streamlit Cloud**

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

Built as a learning project for understanding real estate price prediction using Machine Learning.

Made with ❤️ using Python & Streamlit
