# 🏠 MagicBricks House Price Predictor

A Multiple Linear Regression model to predict house prices in Delhi using the MagicBricks dataset.

---

## 📋 Project Overview

This project builds a **Multiple Linear Regression** model to predict residential property prices in Delhi based on various features like Area, BHK, Bathrooms, Locality, etc.

**Goal**: Help users estimate realistic house prices using key property attributes.

---

## ✨ Features

- Comprehensive EDA (Exploratory Data Analysis)
- Robust Data Preprocessing & Cleaning
- Outlier Detection and Removal
- Feature Engineering (`Total_Rooms`, `Area_per_Room`)
- One-Hot Encoding of Categorical Variables
- Multiple Linear Regression Model
- Model Evaluation Metrics (MAE, RMSE, R²)
- Streamlit Web Application for easy predictions
- Docker Support for containerized deployment

---

## 📊 Model Performance

| Metric              | Value          |
|---------------------|----------------|
| R² Score            | ~0.66          |
| Mean Absolute Error | ₹X.XX Lakh     |
| RMSE                | ₹X.XX Lakh     |

> *Note: Performance can be further improved using XGBoost and better feature engineering.*
>
> ## demo
>## pictures
> <img width="640" height="319" alt="Screenshot 2026-05-17 162617" src="https://github.com/user-attachments/assets/73dfe663-f0e9-49b2-8482-7a473262b723" />

<img width="637" height="299" alt="Screenshot 2026-05-17 162659" src="https://github.com/user-attachments/assets/1b9e405e-4dae-4ed8-80ee-c2d1a8bfe807" />

## videos




https://github.com/user-attachments/assets/89d3a6e7-c19a-4c19-a8cb-dcfe8b8b81af





https://github.com/user-attachments/assets/276f364a-d9d1-4d18-b3fd-e265eb9d43ff



https://github.com/user-attachments/assets/ac484f15-166e-494c-9a94-15a6904c511c












---

## 🛠 Tech Stack

- **Python 3.11**
- **Pandas, NumPy** – Data Manipulation
- **Scikit-learn** – Machine Learning
- **Matplotlib & Seaborn** – Visualization
- **Streamlit** – Web Application
- **Docker** – Containerization

---

## 📁 Project Structure
house-price-app/
├── app.py                    # Streamlit Web Application
├── Dockerfile                # Docker configuration
├── requirements.txt          # Python dependencies
├── .dockerignore             # Docker build optimization
├── .gitignore                # Git ignore (recommended to add)
│
├── MagicBricks.csv                   # ← Grouped data files
│  
│
├── models/                   # ← Grouped model files
│   ├── house_price_model.pkl
│   └── feature_columns.pkl
│
├── notebooks/                # ← Grouped notebooks
│   └── notebook.ipynb
│
└── README.md


---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd house-price-app


2. Install Dependencies

pip install -r requirements.txt


3. Run Streamlit App

streamlit run app.py

4. Using Docker (Recommended)
docker build -t house-price-app .
docker run -p 8501:8501 house-price-app

Open browser → http://localhost:8501


📈 Key Insights

Area is the most important feature
Locality significantly impacts price
Number of Bathrooms and BHK also play important roles
Furnishing status and Property type affect valuation

🔮 Future Improvements

Switch to XGBoost / Gradient Boosting
Advanced hyperparameter tuning
Add more locality features
Include floor number and property age
Deploy on cloud (Render / Railway)


👤 Author
Built as a learning project for understanding real estate price prediction using Machine Learning.

Made with ❤️ using Python & Streamlit
