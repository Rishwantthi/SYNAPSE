## SOIL HEALTH PREDICTOR ##

The *Soil Health Predictor* is a machine learning-based web application designed to assess soil quality using key parameters: Nitrogen, Phosphorous, Potassium, Moisture, and Temperature. By analyzing these features, the model predicts whether the soil is healthy or unhealthy using a Random Forest Classifier trained on real-world agricultural data. It uses statistical medians to define health thresholds and standardizes input data for accurate predictions. The tool helps farmers and agronomists make informed decisions about soil management. Built with Gradio, it offers a user-friendly interface for instant predictions, supporting sustainable farming and improving crop productivity through better soil analysis.

```
# STEP 1: Import libraries
import pandas as pd
import numpy as np
import gradio as gr
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# STEP 2: Load dataset
df = pd.read_csv('/content/data_core.csv')
df = df.rename(columns={'Temparature': 'Temperature'})  # fix typo

# STEP 3: Select relevant features & create labels
features = ['Nitrogen', 'Phosphorous', 'Potassium', 'Moisture', 'Temperature']
df = df[features].dropna()

medians = df.median()
df['Healthy'] = (
    (df['Nitrogen'] > medians['Nitrogen']) &
    (df['Phosphorous'] > medians['Phosphorous']) &
    (df['Potassium'] > medians['Potassium']) &
    (df['Moisture'] > medians['Moisture']) &
    (df['Temperature'] > medians['Temperature'])
).astype(int)

# STEP 4: Model training
X = df[features]
y = df['Healthy']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_s, y_train)

# STEP 5: Prediction function
def predict_soil_health(Nitrogen, Phosphorous, Potassium, Moisture, Temperature):
    input_data = pd.DataFrame([[Nitrogen, Phosphorous, Potassium, Moisture, Temperature]],
                              columns=features)
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    return "✅ Healthy Soil" if prediction == 1 else "⚠️ Unhealthy Soil"

# STEP 6: Gradio web app
gr.Interface(
    fn=predict_soil_health,
    inputs=[
        gr.Number(label="Nitrogen (mg/kg)"),
        gr.Number(label="Phosphorous (mg/kg)"),
        gr.Number(label="Potassium (mg/kg)"),
        gr.Number(label="Moisture (%)"),
        gr.Number(label="Temperature (°C)")
    ],
    outputs="text",
    title="🌱 Soil Health Prediction App",
    description="Enter key soil nutrient levels to predict whether the soil is healthy or not."
).launch(share=True)

```
