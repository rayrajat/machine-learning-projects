import streamlit as st # type: ignore
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="MagicBricks House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 MagicBricks House Price Predictor")
st.markdown("### Predict house prices in Delhi using Multiple Linear Regression")

# ====================== LOAD MODEL & DATA ======================
@st.cache_resource
def load_model():
    # Train model here (or load saved model)
    df = pd.read_csv('MagicBricks.csv')
    data = df.copy()
    
    # Preprocessing
    data = data.drop(columns=['Per_Sqft'])
    data['Bathroom'] = data['Bathroom'].fillna(data['Bathroom'].median())
    data['Parking'] = data['Parking'].fillna(data['Parking'].median())
    
    for col in ['Furnishing', 'Status', 'Transaction', 'Type']:
        data[col] = data[col].fillna(data[col].mode()[0])
    
    # Outlier removal
    data = data[data['Price'] < 30000000]
    data = data[data['Area'] < 5000]
    
    data['Total_Rooms'] = data['BHK'] + data['Bathroom']
    data['Area_per_Room'] = data['Area'] / (data['Total_Rooms'] + 1)
    
    features = ['Area', 'BHK', 'Bathroom', 'Parking', 'Total_Rooms', 'Area_per_Room',
                'Furnishing', 'Status', 'Transaction', 'Type']
    
    X = data[features]
    y = data['Price']
    
    X = pd.get_dummies(X, columns=['Furnishing', 'Status', 'Transaction', 'Type'], drop_first=True)
    
    model = LinearRegression()
    model.fit(X, y)
    
    return model, X.columns

model, feature_columns = load_model()

# ====================== SIDEBAR INPUTS ======================
st.sidebar.header("Enter Property Details")

area = st.sidebar.number_input("Area (sqft)", min_value=300, max_value=5000, value=1200)
bhk = st.sidebar.selectbox("BHK", [1, 2, 3, 4, 5])
bathroom = st.sidebar.selectbox("Bathrooms", [1, 2, 3, 4, 5])
parking = st.sidebar.selectbox("Parking Spots", [0, 1, 2, 3, 4])

furnishing = st.sidebar.selectbox("Furnishing", 
    ["Unfurnished", "Semi-Furnished", "Furnished"])

status = st.sidebar.selectbox("Status", 
    ["Ready_to_move", "Almost_ready"])

transaction = st.sidebar.selectbox("Transaction", 
    ["New_Property", "Resale"])

house_type = st.sidebar.selectbox("Property Type", 
    ["Builder_Floor", "Apartment"])

# ====================== PREDICTION ======================
if st.button("🔍 Predict Price", type="primary"):
    input_data = pd.DataFrame({
        'Area': [area],
        'BHK': [bhk],
        'Bathroom': [bathroom],
        'Parking': [parking],
        'Total_Rooms': [bhk + bathroom],
        'Area_per_Room': [area / (bhk + bathroom + 1)],
        'Furnishing': [furnishing],
        'Status': [status],
        'Transaction': [transaction],
        'Type': [house_type]
    })
    
    # Encoding
    input_encoded = pd.get_dummies(input_data, 
                                 columns=['Furnishing', 'Status', 'Transaction', 'Type'], 
                                 drop_first=True)
    
    # Align columns
    input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)
    
    # Predict
    prediction = model.predict(input_encoded)[0]
    
    st.success(f"**Predicted House Price: ₹{prediction:,.0f}**")
    
    # Show price range
    st.info(f"**Price Range:** ₹{prediction*0.9:,.0f} - ₹{prediction*1.1:,.0f}")

# ====================== ABOUT ======================
st.sidebar.markdown("---")
st.sidebar.info("""
**Model Info:**
- Multiple Linear Regression
- Features: Area, BHK, Bathroom, Parking, etc.
- Trained on MagicBricks Delhi Data
""")

st.caption("Built with ❤️ using Streamlit | Data: MagicBricks")