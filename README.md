# 🌾 Farmer Planner AI — Smart Agriculture Suite

## 🔍 Abstract

**Farmer Planner AI** is an AI-powered agriculture planning and analysis platform tailored to empower farmers with actionable insights. It integrates multiple intelligent tools—from crop recommendations and economic planning to disease detection, voice assistance, and 3D plant modeling. This unified system enhances productivity, reduces risk, and modernizes traditional farming practices using cutting-edge technologies like AI, ML, and NLP.

---

## 📘 Introduction

Despite technological advances, many farmers still rely on conventional methods, facing challenges in crop selection, disease management, and market forecasting. **Farmer Planner AI** was built to bridge this gap through:

- Personalized recommendations (based on soil, land, and climate)
- Multilingual voice/text inputs
- AI integrations like disease detection, price trend prediction, and more
- Simple, farmer-friendly interface with high-level insights

---

## 🏗️ Project Structure

```
📁 farmer-planner-ai/pages
├── app.py                      # Main Streamlit application
├── login.py                    # Login system (email + OTP or Firebase-based)
├── crop_database.py            # Database of crop info
├── recommendation_engine.py    # AI logic for crop recommendations
├── voice_processor.py          # NLP for voice/text input
├── image_analyzer.py           # Land image analysis
├── economic_advisor.py         # Profit/loss + government schemes
├── .streamlit/
│   └── config.toml
├── requirements.txt
└── readme.md
```

## 💻 Tech Stack

| Component         | Technology Used            |
|------------------|----------------------------|
| Frontend UI      | Streamlit + HTML/CSS       |
| AI Integrations  | Gradio, HuggingFace, Replit|
| Backend Storage  | Local JSON / Python memory |
| Deployment       | Localhost (Streamlit), Replit |
| Language         | Python                     |

---

## 🚀 How It Works (A to Z)

### 🔐 Authentication
- Login & Signup are handled in `login.py` and `signup.py`.
- Data is stored locally using JSON or Python dictionaries.
- Upon successful login, user is redirected to:  
  👉 `http://localhost:8501/` (main dashboard with modules)

### 🧠 AI-Powered Tools
Each button in the main dashboard opens a specific live application hosted externally, giving users access to various agricultural AI modules:

| Tool                        | Description |
|----------------------------|-------------|
| 🌱 **Smart Garden AI**     | Interactive visual garden planning assistant. |
| 🦠 **Crop Disease Detection** | Upload leaf images and detect plant diseases. |
| 🧬 **Bio Digital Twin**    | A simulated plant bio model to monitor plant growth virtually. | 
| 🗣️ **Voice Integrated Chatbot** | 24x7 voice assistant for farming-related queries. | 
| 📈 **Price Trend Predictor** | Predict crop price trends using past data. | 
| 🌍 **Soil Health Predictor** | Input soil values to receive pH, fertility, and crop suggestions. |

### 🌐 Key Features (Fully Working from app.py)
## 1. 🎯 Input Methods Page
Users can choose how to provide their farm information:

📝 Form-Based Input
Input land size, soil type, season, and budget manually.

🖼️ Image Upload
Upload a photo of the farmland. The system analyzes it using AI/ML and extracts insights like sunlight exposure, soil type, etc.

🎤 Voice/Text Input
Talk or type in multiple languages: English, Tamil, Hindi, Telugu. Natural Language Processing (NLP) converts your speech into structured farm data.

## 2. 🌱 AI Crop Recommendation
Suggests the best crops based on:

Land size

Soil type

Season

Budget

Displays:

Water and fertilizer schedule

Expected yield and cost

Suitability score

Sunlight & temperature needs

✅ Multilingual recommendations are supported.

## 3. 🖼️ Image-Based Crop Land Analysis
Upload an image of your farmland and get:

Detected soil and land type

Sunlight analysis

Suggested crops that match the detected conditions

Tailored farming advice based on visual data

## 4. 🎤 Voice + Text AI Assistant (Multilingual NLP)
Describe your farm scenario naturally, for example:

“2 acres of clay soil, planting in summer, ₹3000 budget”

The system will:

Automatically extract key farm info

Recommend crops

Explain water/fertilizer needs

Give economic advice in plain language

Supports input in major Indian languages.

## 5. 💰 Economic Planner
After selecting a crop:

Enter:

Total land

Expected income

Location

Budget

The tool will then output:

📈 Profit/Loss estimation

💸 Cost breakdown per acre

🌍 Best local & export markets

🏛️ Relevant Government schemes

🔁 Alternative crop suggestions if current choice is unprofitable

---

## ✅ Features

- 🔒 **Login/Signup UI** with secure routing
- 📊 **Crop Intelligence Dashboard** (visually designed)
- 🧠 **AI Modules** linked and running on Gradio / Replit
- 🎙️ **Voice Chatbot** for real-time query solving
- 🏷️ **Prediction Models** for pricing, diseases, and soil
- 🧪 **No Database Needed** – lightweight & local data storage

🔐 Login System (via Firebase Auth)

---
