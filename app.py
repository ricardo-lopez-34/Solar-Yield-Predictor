import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(page_title="Solar Yield Forecast", page_icon="☀️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #fffdf5; }
    .stMetric { background-color: #ffffff; border-left: 5px solid #ffcc00; }
    </style>
    """, unsafe_allow_html=True)

st.title("☀️ Solar Yield Predictive Analytics")
st.sidebar.header("System Calibration")
panel_area = st.sidebar.slider("Panel Surface Area (m²)", 1.0, 50.0, 5.0)
st.sidebar.caption("Efficiency is automatically adjusted based on temperature.")

placeholder = st.empty()

for _ in range(100):
    irr = round(np.random.uniform(200, 1000), 1)
    temp = round(np.random.uniform(20.0, 45.0), 1)
    
    # Logic: 18% Base Efficiency with -0.4%/°C degradation
    eff = 0.18 * (1 - 0.004 * (temp - 25))
    p_out = round(irr * panel_area * eff, 2)

    with placeholder.container():
        c1, c2, c3 = st.columns(3)
        c1.metric("Solar Irradiance", f"{irr} W/m²")
        c2.metric("Ambient Temp", f"{temp} °C", delta="-0.4%/°C" if temp > 25 else "Stable")
        c3.metric("Predicted Power", f"{p_out} Watts")

        hours = [f"{h}:00" for h in range(6, 19)]
        curve = [p_out * np.sin(np.pi * (h-6)/12) for h in range(6, 19)]
        
        fig = go.Figure(go.Scatter(x=hours, y=curve, fill='tozeroy', line_color='orange', name="Yield"))
        fig.update_layout(title="Projected Generation Curve (Daily)", xaxis_title="Time", yaxis_title="Watts")
        st.plotly_chart(fig, use_container_width=True)

    time.sleep(2)
