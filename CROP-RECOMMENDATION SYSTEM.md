**CROP-RECOMMENDATION SYSTEM**

This AI-powered crop recommendation system is a machine learning-based solution designed to assist farmers in selecting the most suitable crop based on soil and weather conditions, without requiring live internet access or external APIs. The model is trained using the publicly available "Crop Recommendation Dataset," which includes features such as nitrogen (N), phosphorus (P), potassium (K), temperature, humidity, pH, and rainfall, with the target variable being the recommended crop.

Instead of relying on real-time weather APIs, the system uses simulated weather data for 10 predefined Indian cities. Users select their city and soil type (e.g., loamy, sandy, clayey), and input the potassium value. Internally, the system infers N, P, and pH based on the selected soil type, while temperature, humidity, and rainfall are retrieved from a preloaded mapping based on the selected city. These combined inputs are standardized and passed to a Random Forest Classifier, which predicts the most appropriate crop.

The model is deployed through a Gradio-based web app, making it simple and accessible to end-users. This lightweight, offline-capable tool offers a practical solution for small-scale farmers and agriculture extension officers, enabling data-driven decisions even in low-connectivity areas.



```
import pandas as pd
import numpy as np
import gradio as gr
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# === Load dataset ===
df = pd.read_csv('/content/Crop_recommendation.csv')  # Adjust path if needed

# === Model training ===
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)
# Fixed city-weather values (simulated but diverse). As weather api-keys require a minimum of 1-day to get activated
weather_data = {
    "Chennai":    {"temperature": 32, "humidity": 78, "rainfall": 90},
    "Delhi":      {"temperature": 30, "humidity": 55, "rainfall": 60},
    "Mumbai":     {"temperature": 29, "humidity": 80, "rainfall": 120},
    "Bangalore":  {"temperature": 27, "humidity": 70, "rainfall": 100},
    "Kolkata":    {"temperature": 31, "humidity": 85, "rainfall": 140},
    "Hyderabad":  {"temperature": 33, "humidity": 65, "rainfall": 75},
    "Ahmedabad":  {"temperature": 34, "humidity": 50, "rainfall": 50},
    "Pune":       {"temperature": 28, "humidity": 68, "rainfall": 90},
    "Thanjavur":  {"temperature": 30, "humidity": 76, "rainfall": 110},
    "Jaipur":     {"temperature": 35, "humidity": 40, "rainfall": 45},
}
# Soil nutrients (realistic approximations)
soil_nutrient_map = {
    "loamy": {"N": 85, "P": 55, "ph": 6.6},
    "sandy": {"N": 35, "P": 25, "ph": 6.0},
    "clayey": {"N": 65, "P": 42, "ph": 6.9},
    "black": {"N": 95, "P": 65, "ph": 7.1},
    "red": {"N": 70, "P": 40, "ph": 6.2},
}
def predict_crop(city, soil_type, K):
    # Get weather
    weather = weather_data.get(city)
    if weather is None:
        return "❌ Invalid city selected."

    temperature = weather["temperature"]
    humidity = weather["humidity"]
    rainfall = weather["rainfall"]

    # Get soil nutrients
    soil = soil_nutrient_map.get(soil_type.lower())
    if soil is None:
        return "❌ Invalid soil type selected."

    N = soil["N"]
    P = soil["P"]
    ph = soil["ph"]

    # Create input for model
    input_features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    input_scaled = scaler.transform(input_features)

    # Predict
    prediction = model.predict(input_scaled)[0]

    return (
        f"📍 City: {city}\n"
        f"🧪 Soil: {soil_type.title()}\n"
        f"🧬 N: {N}, P: {P}, K: {K}, pH: {ph}\n"
        f"🌡 Temp: {temperature}°C | 💧 Humidity: {humidity}% | 🌧 Rainfall: {rainfall}mm\n\n"
        f"✅ Recommended Crop: **{prediction.upper()}**"
    )
iface = gr.Interface(
    fn=predict_crop,
    inputs=[
        gr.Dropdown(choices=list(weather_data.keys()), label="📍 Select Your City"),
        gr.Radio(choices=["loamy", "sandy", "clayey", "black", "red"], label="🧪 Select Soil Type"),
        gr.Number(label="🧂 Potassium (K)")
    ],
    outputs="text",
    title="🌱 AI Crop Recommender",
    description="Choose your city and soil type, and enter Potassium value to get a crop recommendation without using internet APIs.",
)

iface.launch(share=True)
```
