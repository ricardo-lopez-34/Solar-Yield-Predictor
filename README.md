# ☀️ Solar Yield Predictor

A predictive analytics dashboard that calculates the real-time energy output of solar PV panels based on irradiance, temperature, and humidity.

## 🚀 Features
- **Thermal Degradation Modeling:** Adjusts efficiency based on ambient temperature.
- **Projected Yield Curves:** Visualizes the daily power generation cycle.
- **Dynamic WiFi Configuration:** Supports Serial Monitor input for network credentials.
- **Environmental Insights:** Real-time data logging of solar intensity.

## ⚙️ How it Works
1. **The Edge Layer:** An ESP32 uses an LDR (Light Dependent Resistor) to measure irradiance and a DHT11 for temperature/humidity.
2. **The Logic Layer:** Energy yield is calculated using the Temperature Coefficient formula:
   $$P_{out} = G \times A \times \eta \times [1 + \gamma(T_{amb} - 25)]$$
3. **The Presentation Layer:** Data is streamed to a Streamlit dashboard.
