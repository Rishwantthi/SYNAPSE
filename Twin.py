from flask import Flask, render_template, request, jsonify
import random
import datetime

app = Flask(__name__)

# --- Digital Twin Core Simulation (Simplified) ---
# This dictionary will hold the state of our virtual crop
# In a real system, this would be much more complex,
# potentially pulling from a database or a more sophisticated simulation engine.
crop_twin_data = {
    "growth_stage": "Seedling",
    "days_since_planting": 0,
    "height_cm": 0.5,
    "health_score": 100, # 0-100, 100 is perfect
    "soil_moisture": 70, # %
    "temperature_c": 25, # Celsius
    "humidity_percent": 60, # %
    "nutrition_level": "Optimal", # Optimal, Low N, Low P, Low K
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# --- Simple Growth Model ---
def simulate_growth(days_passed=1, soil_moisture=None, temperature_c=None, humidity_percent=None, nutrition_level=None):
    global crop_twin_data

    # Update parameters based on input, or use current twin data if not provided
    current_moisture = soil_moisture if soil_moisture is not None else crop_twin_data["soil_moisture"]
    current_temp = temperature_c if temperature_c is not None else crop_twin_data["temperature_c"]
    current_humidity = humidity_percent if humidity_percent is not None else crop_twin_data["humidity_percent"]
    current_nutrition = nutrition_level if nutrition_level is not None else crop_twin_data["nutrition_level"]

    for _ in range(days_passed):
        crop_twin_data["days_since_planting"] += 1

        # Simulate height growth based on conditions
        growth_factor = 1.0
        if 50 <= current_moisture <= 80: growth_factor += 0.2
        if 20 <= current_temp <= 30: growth_factor += 0.3
        if 50 <= current_humidity <= 70: growth_factor += 0.1
        if current_nutrition == "Optimal": growth_factor += 0.2

        # Penalties for poor conditions
        if current_moisture < 50 or current_moisture > 80: growth_factor -= 0.1
        if current_temp < 20 or current_temp > 30: growth_factor -= 0.1
        if current_nutrition != "Optimal": growth_factor -= 0.2

        # Ensure growth factor doesn't go below zero
        growth_factor = max(0.1, growth_factor)

        crop_twin_data["height_cm"] += (random.uniform(0.5, 1.5) * growth_factor)
        crop_twin_data["height_cm"] = round(crop_twin_data["height_cm"], 2)

        # Simulate health score based on conditions
        health_change = 0
        if growth_factor < 0.8: health_change = -random.randint(1, 5)
        elif growth_factor > 1.2: health_change = random.randint(0, 2) # Small positive for good conditions
        else: health_change = random.randint(-1, 1) # Minor fluctuations

        crop_twin_data["health_score"] = max(0, min(100, crop_twin_data["health_score"] + health_change))

        # Update growth stage (very simple example)
        if 0 <= crop_twin_data["days_since_planting"] < 10:
            crop_twin_data["growth_stage"] = "Seedling"
        elif 10 <= crop_twin_data["days_since_planting"] < 30:
            crop_twin_data["growth_stage"] = "Vegetative"
        elif 30 <= crop_twin_data["days_since_planting"] < 60:
            crop_twin_data["growth_stage"] = "Flowering"
        else:
            crop_twin_data["growth_stage"] = "Fruiting/Harvest"

        # Simulate sensor data fluctuations (if not controlled by user)
        if soil_moisture is None:
            crop_twin_data["soil_moisture"] = max(30, min(90, crop_twin_data["soil_moisture"] + random.randint(-5, 5)))
        if temperature_c is None:
            crop_twin_data["temperature_c"] = max(15, min(35, crop_twin_data["temperature_c"] + random.uniform(-1, 1)))
        if humidity_percent is None:
            crop_twin_data["humidity_percent"] = max(40, min(80, crop_twin_data["humidity_percent"] + random.randint(-3, 3)))
        # Nutrition level could degrade over time or improve with "fertilizer" input
        if current_nutrition == "Optimal" and random.random() < 0.1: # 10% chance to degrade
            crop_twin_data["nutrition_level"] = random.choice(["Low N", "Low P", "Low K"])

    crop_twin_data["last_updated"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- Flask Routes ---

@app.route('/')
def index():
    # Simulate initial growth for the first load
    if crop_twin_data["days_since_planting"] == 0:
        simulate_growth(days_passed=1) # Start with 1 day of growth
    return render_template('index.html', twin_data=crop_twin_data)

@app.route('/update_twin', methods=['POST'])
def update_twin():
    data = request.json
    days_to_simulate = int(data.get('days', 1))
    soil_moisture = data.get('soil_moisture')
    temperature_c = data.get('temperature_c')
    humidity_percent = data.get('humidity_percent')
    nutrition_level = data.get('nutrition_level')

    # Convert to float/int if they are not None, otherwise keep as None for simulation to fluctuate
    if soil_moisture is not None: soil_moisture = int(soil_moisture)
    if temperature_c is not None: temperature_c = float(temperature_c)
    if humidity_percent is not None: humidity_percent = int(humidity_percent)

    simulate_growth(
        days_passed=days_to_simulate,
        soil_moisture=soil_moisture,
        temperature_c=temperature_c,
        humidity_percent=humidity_percent,
        nutrition_level=nutrition_level
    )
    return jsonify(crop_twin_data)

@app.route('/ai_analysis', methods=['POST'])
def ai_analysis():
    # This is where you would integrate with a real AI model (e.g., Google Gemini)
    # For this demo, it's a simple rule-based analysis.
    current_health = crop_twin_data["health_score"]
    current_nutrition = crop_twin_data["nutrition_level"]
    current_moisture = crop_twin_data["soil_moisture"]
    current_temp = crop_twin_data["temperature_c"]

    analysis_report = "Based on the digital twin's current state:\n"

    if current_health < 70:
        analysis_report += "- The crop health is declining. "
        if current_nutrition != "Optimal":
            analysis_report += f"Consider checking for {current_nutrition} deficiency. "
        if current_moisture < 50:
            analysis_report += "Soil moisture is low, consider irrigation. "
        elif current_moisture > 80:
            analysis_report += "Soil moisture is high, ensure proper drainage. "
        if current_temp < 20:
            analysis_report += "Temperature is a bit low for optimal growth. "
        elif current_temp > 30:
            analysis_report += "Temperature is a bit high, ensure adequate water. "
    else:
        analysis_report += "- The crop appears to be in good health. Continue monitoring conditions."

    analysis_report += "\n\nFor a real system, an image upload would trigger a more detailed visual analysis by an AI model like Google Gemini's Vision capabilities."

    return jsonify({"analysis": analysis_report})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81) # Replit uses port 81 by default for Flask
