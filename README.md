# Network Traffic Anomaly Detection Web App

This is a Streamlit web application for detecting anomalies in network traffic using a trained deep learning model (Autoencoder). The app allows users to input real-time traffic features (e.g., bytes, packets, ports) and receive a prediction indicating whether the traffic is **normal** or **anomalous**.

---

## 🧠 Purpose

This project is part of a thesis research titled **"A Deep Learning Approach for Forecasting Network Traffic."** The app is built to demonstrate the **real-world performance** of the trained anomaly detection model by allowing end users to test it interactively.

---

## 🚀 Features

- Simple, interactive UI built with **Streamlit**
- Accepts meaningful user inputs (e.g., protocol type, packets, duration)
- Applies preprocessing and scaling under the hood
- Uses a trained **Autoencoder model** to detect anomalies
- Displays prediction along with reconstruction error

---

## 📦 Tech Stack

- Python 3.8+
- Streamlit
- TensorFlow / Keras
- Scikit-learn
- Pandas, NumPy
- Pre-trained model (`autoencoder.h5`) + scaler (`scaler.pkl`)

---

## 📁 Project Structure

