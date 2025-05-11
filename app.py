import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# Load model and scaler
scaler = joblib.load("model/scaler.pkl")
model = load_model("model/autoencoder.h5")
threshold = 0.01  # Update with your actual threshold

# Protocol encoding
protocol_map = {"TCP": 0, "UDP": 1, "ICMP": 2}

st.title("🚦 Network Anomaly Detection")
st.markdown("Check if a network connection is anomalous based on traffic statistics.")

# Input fields
with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        source_port = st.number_input("Source Port", min_value=0, max_value=65535)
        destination_port = st.number_input("Destination Port", min_value=0, max_value=65535)
        protocol = st.selectbox("Protocol", options=list(protocol_map.keys()))
        duration = st.number_input("Duration (s)", min_value=0.0, format="%.2f")
    with col2:
        bytes_sent = st.number_input("Bytes Sent", min_value=0)
        bytes_received = st.number_input("Bytes Received", min_value=0)
        packets_sent = st.number_input("Packets Sent", min_value=0)
        packets_received = st.number_input("Packets Received", min_value=0)

    submitted = st.form_submit_button("Predict")

# On submit
if submitted:
    total_bytes = bytes_sent + bytes_received
    total_packets = packets_sent + packets_received
    protocol_encoded = protocol_map[protocol]

    # Dummy values for IP fields if preprocessed
    input_data = pd.DataFrame([{
        "SourceIP": 0,
        "DestinationIP": 0,
        "SourcePort": source_port,
        "DestinationPort": destination_port,
        "Protocol": protocol_encoded,
        "BytesSent": bytes_sent,
        "BytesReceived": bytes_received,
        "PacketsSent": packets_sent,
        "PacketsReceived": packets_received,
        "Duration": duration,
        "TotalBytes": total_bytes,
        "TotalPackets": total_packets
    }])

    input_scaled = scaler.transform(input_data)
    reconstructed = model.predict(input_scaled)
    error = np.mean(np.square(input_scaled - reconstructed))
    prediction = int(error > threshold)

    st.markdown("### 🧾 Prediction:")
    if prediction == 1:
        st.error("🚨 Anomalous traffic detected!")
    else:
        st.success("✅ Normal traffic.")
    st.markdown(f"**Reconstruction Error**: `{error:.6f}`")

