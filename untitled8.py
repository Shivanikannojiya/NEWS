import streamlit as st
import joblib
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model and other files
model = tf.keras.models.load_model("C:/Users/shivani/OneDrive/Documents/NEWS/lstm_model.keras")
tokenizer = joblib.load("C:/Users/shivani/OneDrive/Documents/NEWS/tokenizer.pkl")
label_encoder = joblib.load("C:/Users/shivani/OneDrive/Documents/NEWS/label_encoder.pkl")

# UI
st.title("📰 News Category Classifier")
st.write("Enter a news headline to predict its category.")

# User input
user_input = st.text_area("Enter News Headline", "")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a headline.")
    else:
        # Preprocess input
        seq = tokenizer.texts_to_sequences([user_input])
        padded = pad_sequences(seq, maxlen=25)  # same maxlen used during training

        # Predict
        pred = model.predict(padded)
        predicted_label = label_encoder.inverse_transform([np.argmax(pred)])

        # Output
        st.success(f"Predicted Category: **{predicted_label[0]}**")
