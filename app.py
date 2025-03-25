import streamlit as st
import numpy as np
import joblib

# Cache model loading
@st.cache_resource
def load_model():
    return joblib.load('model2.pkl') 

# Load model
model = load_model()

# Title & Subtitle
st.title('Fuel Consumption Prediction Tool')
st.subheader('This tool helps predict fuel consumption in miles per gallon (MPG)')

# Check if model loaded successfully
if model:
    st.write('Please Input the Following Details:')

# User Inputs
Odometer = st.number_input('Odometer', value=0, min_value=0, help='Enter the odometer reading in miles')
Distance = st.number_input('Distance', value=0, min_value=0, help='Enter the distance in miles')

# Product Encoding
Product_encoded = st.selectbox('Select Product:', 
                               options=[(0, 'Diesel'), (1, 'CNG'), (2, 'Gasoil')], 
                               format_func=lambda x: x[1])
Product_encoded_value = Product_encoded[0]

# Prepare user input for model prediction
user_input = np.array([Odometer, Distance, Product_encoded_value]).reshape(1, -1)

# Prediction Button
if st.button('Click to determine fuel consumption'):
    prediction = model.predict(user_input)
    st.write(f'The predicted fuel consumption is **{prediction[0]:.2f} mpg**')

st.write('Use this result to make informed decisions about fuel efficiency.')
