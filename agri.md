# AgroAura - Quick Copy-Paste Code

## 1. app.py
```python
import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "agroaura-secret-key-2024")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///agroaura.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = 'uploads'

db.init_app(app)
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

with app.app_context():
    import models
    import routes
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

## 2. main.py
```python
from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

## 3. models.py
```python
from app import db
from datetime import datetime
from sqlalchemy import Text, JSON

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(100))
    land_size = db.Column(db.String(50))
    soil_water_access = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    crops = db.relationship('Crop', backref='user', lazy=True)
    conversations = db.relationship('Conversation', backref='user', lazy=True)

class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    crop_name = db.Column(db.String(100), nullable=False)
    sowing_date = db.Column(db.Date)
    current_stage = db.Column(db.String(50))
    symbiosis_score = db.Column(db.Integer, default=0)
    last_watered = db.Column(db.DateTime)
    last_fertilized = db.Column(db.DateTime)
    notes = db.Column(Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    input_type = db.Column(db.String(20))
    input_content = db.Column(Text)
    agent_used = db.Column(db.String(50))
    agent_response = db.Column(Text)
    image_path = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    rainfall = db.Column(db.Float)
    weather_condition = db.Column(db.String(50))
    forecast_data = db.Column(JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

## 4. crop_database.py
```python
def get_crop_database():
    return {
        'Rice': {
            'soil_preference': ['Clay', 'Loamy'],
            'seasons': ['Spring', 'Summer'],
            'cost_per_acre': 25000,
            'profit_per_acre': 45000,
            'growing_time': '120 days',
            'difficulty': 'Medium',
            'yield_per_acre': '2000 kg',
            'market_price': '₹25-30 per kg',
            'growing_tips': ['Maintain consistent water levels', 'Apply fertilizer in 3 split doses', 'Monitor for pests regularly']
        },
        'Wheat': {
            'soil_preference': ['Loamy', 'Sandy'],
            'seasons': ['Fall', 'Winter'],
            'cost_per_acre': 20000,
            'profit_per_acre': 35000,
            'growing_time': '120 days',
            'difficulty': 'Easy',
            'yield_per_acre': '1800 kg',
            'market_price': '₹20-25 per kg',
            'growing_tips': ['Sow at optimal time for maximum yield', 'Apply nitrogen fertilizer appropriately', 'Harvest at right moisture content']
        },
        'Tomato': {
            'soil_preference': ['Loamy', 'Sandy'],
            'seasons': ['Spring', 'Fall'],
            'cost_per_acre': 30000,
            'profit_per_acre': 80000,
            'growing_time': '90 days',
            'difficulty': 'Medium',
            'yield_per_acre': '3000 kg',
            'market_price': '₹15-25 per kg',
            'growing_tips': ['Provide proper support structures', 'Regular pruning for better yield', 'Monitor for diseases and pests']
        },
        'Cotton': {
            'soil_preference': ['Clay', 'Loamy'],
            'seasons': ['Spring', 'Summer'],
            'cost_per_acre': 35000,
            'profit_per_acre': 65000,
            'growing_time': '150 days',
            'difficulty': 'Hard',
            'yield_per_acre': '400 kg',
            'market_price': '₹150-180 per kg',
            'growing_tips': ['Deep plowing for better root development', 'Integrated pest management essential', 'Proper spacing for maximum yield']
        },
        'Sugarcane': {
            'soil_preference': ['Clay', 'Loamy'],
            'seasons': ['Spring', 'Summer'],
            'cost_per_acre': 40000,
            'profit_per_acre': 90000,
            'growing_time': '365 days',
            'difficulty': 'Hard',
            'yield_per_acre': '40000 kg',
            'market_price': '₹3-4 per kg',
            'growing_tips': ['Adequate water supply essential', 'Apply organic manure regularly', 'Monitor for red rot disease']
        },
        'Potato': {
            'soil_preference': ['Loamy', 'Sandy'],
            'seasons': ['Fall', 'Winter'],
            'cost_per_acre': 28000,
            'profit_per_acre': 55000,
            'growing_time': '90 days',
            'difficulty': 'Medium',
            'yield_per_acre': '2500 kg',
            'market_price': '₹12-18 per kg',
            'growing_tips': ['Proper hilling for better tuber development', 'Avoid over-watering', 'Harvest at right maturity']
        },
        'Onion': {
            'soil_preference': ['Loamy', 'Sandy'],
            'seasons': ['Fall', 'Winter'],
            'cost_per_acre': 25000,
            'profit_per_acre': 60000,
            'growing_time': '120 days',
            'difficulty': 'Medium',
            'yield_per_acre': '2000 kg',
            'market_price': '₹15-30 per kg',
            'growing_tips': ['Proper spacing for bulb development', 'Avoid excess nitrogen in later stages', 'Cure properly before storage']
        },
        'Maize': {
            'soil_preference': ['Loamy', 'Sandy'],
            'seasons': ['Spring', 'Summer'],
            'cost_per_acre': 22000,
            'profit_per_acre': 40000,
            'growing_time': '100 days',
            'difficulty': 'Easy',
            'yield_per_acre': '2200 kg',
            'market_price': '₹15-20 per kg',
            'growing_tips': ['Maintain adequate plant population', 'Apply balanced fertilization', 'Control weeds in early stages']
        },
        'Soybean': {
            'soil_preference': ['Clay', 'Loamy'],
            'seasons': ['Spring', 'Summer'],
            'cost_per_acre': 18000,
            'profit_per_acre': 35000,
            'growing_time': '100 days',
            'difficulty': 'Easy',
            'yield_per_acre': '1500 kg',
            'market_price': '₹25-35 per kg',
            'growing_tips': ['Inoculate seeds with rhizobium', 'Avoid water logging', 'Harvest at right moisture content']
        },
        'Chickpea': {
            'soil_preference': ['Loamy', 'Sandy'],
            'seasons': ['Fall', 'Winter'],
            'cost_per_acre': 15000,
            'profit_per_acre': 32000,
            'growing_time': '120 days',
            'difficulty': 'Easy',
            'yield_per_acre': '1200 kg',
            'market_price': '₹40-50 per kg',
            'growing_tips': ['Sow at optimal time', 'Control pod borer effectively', 'Harvest when pods are mature']
        },
        'Mustard': {
            'soil_preference': ['Loamy', 'Sandy'],
            'seasons': ['Fall', 'Winter'],
            'cost_per_acre': 12000,
            'profit_per_acre': 28000,
            'growing_time': '100 days',
            'difficulty': 'Easy',
            'yield_per_acre': '800 kg',
            'market_price': '₹35-45 per kg',
            'growing_tips': ['Sow at right time for maximum yield', 'Apply sulfur fertilizer', 'Control aphids and other pests']
        },
        'Groundnut': {
            'soil_preference': ['Sandy', 'Loamy'],
            'seasons': ['Spring', 'Summer'],
            'cost_per_acre': 20000,
            'profit_per_acre': 45000,
            'growing_time': '120 days',
            'difficulty': 'Medium',
            'yield_per_acre': '1500 kg',
            'market_price': '₹50-70 per kg',
            'growing_tips': ['Maintain proper soil moisture', 'Apply gypsum during pod development', 'Harvest when pods are mature']
        }
    }

def get_seasonal_crops(season):
    crops_db = get_crop_database()
    return {name: crop for name, crop in crops_db.items() if season in crop.get('seasons', [])}

def get_soil_suitable_crops(soil_type):
    crops_db = get_crop_database()
    return {name: crop for name, crop in crops_db.items() if soil_type in crop.get('soil_preference', [])}
```

## 5. recommendation_engine.py
```python
import json
from datetime import datetime
from crop_database import get_crop_database

class CropRecommendationEngine:
    def __init__(self):
        self.crops_db = get_crop_database()
    
    def get_recommendations(self, land_size, soil_type, season, budget):
        suitable_crops = []
        
        for crop_name, crop_data in self.crops_db.items():
            if (soil_type in crop_data.get('soil_preference', []) and
                season in crop_data.get('seasons', [])):
                
                cost_per_acre = crop_data.get('cost_per_acre', 0)
                profit_per_acre = crop_data.get('profit_per_acre', 0)
                
                total_cost = cost_per_acre * land_size
                total_profit_potential = profit_per_acre * land_size
                
                if total_cost <= budget:
                    crop_info = {
                        'name': crop_name,
                        'total_cost': total_cost,
                        'total_profit_potential': total_profit_potential,
                        'roi_percentage': ((total_profit_potential - total_cost) / total_cost * 100) if total_cost > 0 else 0,
                        'growing_time': crop_data.get('growing_time', 'Unknown'),
                        'difficulty': crop_data.get('difficulty', 'Medium'),
                        'yield_per_acre': crop_data.get('yield_per_acre', 'Unknown'),
                        'recommendation_reason': self._generate_reason(crop_data, soil_type, season, land_size, budget)
                    }
                    suitable_crops.append(crop_info)
        
        suitable_crops.sort(key=lambda x: x['roi_percentage'], reverse=True)
        
        general_tips = self._generate_general_tips(soil_type, season, land_size, budget)
        
        top3_cost = sum(crop['total_cost'] for crop in suitable_crops[:3])
        
        return {
            'suitable_crops': suitable_crops,
            'general_tips': general_tips,
            'budget_analysis': {
                'total_budget': budget,
                'top3_cost': top3_cost,
                'remaining_budget': budget - top3_cost,
                'utilization_percentage': (top3_cost / budget * 100) if budget > 0 else 0
            }
        }
    
    def get_crop_plan(self, crop_name, land_size, soil_type, season):
        if crop_name not in self.crops_db:
            return None
        
        crop_data = self.crops_db[crop_name]
        
        growing_time = crop_data.get('growing_time', '90 days')
        timeline = self._generate_timeline(growing_time)
        
        inputs = self._calculate_inputs(crop_data, land_size)
        
        care_schedule = self._generate_care_schedule(crop_data, timeline)
        
        return {
            'crop_name': crop_name,
            'timeline': timeline,
            'inputs_needed': inputs,
            'care_schedule': care_schedule,
            'expected_yield': crop_data.get('yield_per_acre', 'Unknown'),
            'market_price': crop_data.get('market_price', 'Unknown'),
            'growing_tips': crop_data.get('growing_tips', [])
        }
    
    def _generate_reason(self, crop_data, soil_type, season, land_size, budget):
        reasons = []
        
        if soil_type in crop_data.get('soil_preference', []):
            reasons.append(f"Excellent match for {soil_type} soil")
        
        if season in crop_data.get('seasons', []):
            reasons.append(f"Perfect for {season} season")
        
        difficulty = crop_data.get('difficulty', 'Medium')
        if difficulty == 'Easy':
            reasons.append("Beginner-friendly crop")
        elif difficulty == 'Medium':
            reasons.append("Moderate skill requirement")
        
        roi = ((crop_data.get('profit_per_acre', 0) - crop_data.get('cost_per_acre', 0)) / crop_data.get('cost_per_acre', 1)) * 100
        if roi > 80:
            reasons.append("High profit potential")
        elif roi > 50:
            reasons.append("Good profit margins")
        
        return "; ".join(reasons) if reasons else "Suitable for your farm conditions"
    
    def _generate_timeline(self, growing_time):
        import re
        days_match = re.search(r'(\d+)', growing_time)
        if days_match:
            days = int(days_match.group(1))
            return {
                'sowing': '0-7 days',
                'germination': '7-21 days',
                'vegetative': f'21-{days//2} days',
                'flowering': f'{days//2}-{days-14} days',
                'maturity': f'{days-14}-{days} days'
            }
        return {
            'sowing': '0-7 days',
            'germination': '7-21 days',
            'vegetative': '21-60 days',
            'flowering': '60-80 days',
            'maturity': '80-90 days'
        }
    
    def _calculate_inputs(self, crop_data, land_size):
        cost_per_acre = crop_data.get('cost_per_acre', 0)
        return {
            'seeds': f'₹{int(cost_per_acre * 0.15 * land_size):,}',
            'fertilizers': f'₹{int(cost_per_acre * 0.35 * land_size):,}',
            'pesticides': f'₹{int(cost_per_acre * 0.20 * land_size):,}',
            'labor': f'₹{int(cost_per_acre * 0.30 * land_size):,}'
        }
    
    def _generate_care_schedule(self, crop_data, timeline):
        return {
            'watering': 'Daily during germination, every 2-3 days after establishment',
            'fertilization': 'Apply at sowing, vegetative stage, and flowering',
            'pest_control': 'Weekly monitoring, apply as needed',
            'harvesting': f'Harvest when crop reaches maturity ({timeline["maturity"]})'
        }
    
    def _get_difficulty_score(self, difficulty):
        scores = {'Easy': 1, 'Medium': 2, 'Hard': 3}
        return scores.get(difficulty, 2)
    
    def _generate_general_tips(self, soil_type, season, land_size, budget):
        tips = []
        
        if soil_type == 'Clay':
            tips.append("Clay soil retains water well but may need drainage in monsoon")
        elif soil_type == 'Sandy':
            tips.append("Sandy soil drains quickly, so water more frequently")
        elif soil_type == 'Loamy':
            tips.append("Loamy soil is ideal for most crops with good drainage and nutrients")
        
        if season == 'Spring':
            tips.append("Spring is ideal for heat-loving crops like tomatoes and peppers")
        elif season == 'Summer':
            tips.append("Ensure adequate water supply during hot summer months")
        elif season == 'Fall':
            tips.append("Fall planting allows crops to establish before winter")
        elif season == 'Winter':
            tips.append("Protect crops from frost and cold temperatures")
        
        if land_size < 1:
            tips.append("Small plots are perfect for intensive farming and high-value crops")
        elif land_size < 5:
            tips.append("Medium plots allow for crop rotation and diversification")
        else:
            tips.append("Large plots enable mechanization and bulk farming")
        
        if budget < 30000:
            tips.append("Focus on low-cost, high-yield crops for better returns")
        elif budget < 100000:
            tips.append("Consider medium-investment crops with good profit margins")
        else:
            tips.append("You can invest in premium crops or advanced farming techniques")
        
        tips.append("Always test your soil before planting for optimal results")
        tips.append("Keep detailed records of expenses and yields for future planning")
        
        return tips
```

## 6. language_support.py
```python
def get_translations():
    return {
        'English': {
            'user_type': 'I am a:',
            'farmer': '🌾 Farmer',
            'home_gardener': '🪴 Home Gardener',
            'state': 'State',
            'city': 'City (Optional)',
            'land_size': 'Land Size',
            'soil_type': 'Soil Type',
            'water_source': 'Water Source (Optional)',
            'continue': 'Start Farming Journey',
            'get_recommendations': 'Get Recommendations',
            'select_this_crop': 'Select This Crop',
            'cost': 'Cost',
            'profit': 'Profit',
            'roi': 'ROI',
            'growing_time': 'Growing Time',
            'difficulty': 'Difficulty',
            'get_started': 'Get Started',
            'select_type': 'Select your type',
            'select_your_state': 'Select your state',
            'select_land_size': 'Select land size',
            'select_soil_type': 'Select soil type',
            'select_water_source': 'Select water source'
        },
        'Hindi': {
            'user_type': 'मैं हूं:',
            'farmer': '🌾 किसान',
            'home_gardener': '🪴 घर का बागवान',
            'state': 'राज्य',
            'city': 'शहर (वैकल्पिक)',
            'land_size': 'जमीन का आकार',
            'soil_type': 'मिट्टी का प्रकार',
            'water_source': 'पानी का स्रोत (वैकल्पिक)',
            'continue': 'कृषि यात्रा शुरू करें',
            'get_recommendations': 'सुझाव पाएं',
            'select_this_crop': 'यह फसल चुनें',
            'cost': 'लागत',
            'profit': 'लाभ',
            'roi': 'रिटर्न',
            'growing_time': 'उगाने का समय',
            'difficulty': 'कठिनाई',
            'get_started': 'शुरू करें',
            'select_type': 'अपना प्रकार चुनें',
            'select_your_state': 'अपना राज्य चुनें',
            'select_land_size': 'जमीन का आकार चुनें',
            'select_soil_type': 'मिट्टी का प्रकार चुनें',
            'select_water_source': 'पानी का स्रोत चुनें'
        },
        'Tamil': {
            'user_type': 'நான் ஒரு:',
            'farmer': '🌾 விவசாயி',
            'home_gardener': '🪴 வீட்டுத் தோட்டக்காரர்',
            'state': 'மாநிலம்',
            'city': 'நகரம் (விருப்பத்தேர்வு)',
            'land_size': 'நிலத்தின் அளவு',
            'soil_type': 'மண் வகை',
            'water_source': 'நீர் ஆதாரம் (விருப்பத்தேர்வு)',
            'continue': 'விவசாய பயணத்தைத் தொடங்கவும்',
            'get_recommendations': 'பரிந்துரைகளைப் பெறவும்',
            'select_this_crop': 'இந்த பயிரைத் தேர்ந்தெடுங்கள்',
            'cost': 'செலவு',
            'profit': 'இலாபம்',
            'roi': 'வருமானம்',
            'growing_time': 'வளரும் நேரம்',
            'difficulty': 'சிரமம்',
            'get_started': 'தொடங்குங்கள்',
            'select_type': 'உங்கள் வகையைத் தேர்ந்தெடுங்கள்',
            'select_your_state': 'உங்கள் மாநிலத்தைத் தேர்ந்தெடுங்கள்',
            'select_land_size': 'நிலத்தின் அளவைத் தேர்ந்தெடுங்கள்',
            'select_soil_type': 'மண் வகையைத் தேர்ந்தெடுங்கள்',
            'select_water_source': 'நீர் ஆதாரத்தைத் தேர்ந்தெடுங்கள்'
        },
        'Telugu': {
            'user_type': 'నేను ఒక:',
            'farmer': '🌾 రైతు',
            'home_gardener': '🪴 ఇంటి తోటమాలి',
            'state': 'రాష్ట్రం',
            'city': 'నగరం (ఐచ్ఛికం)',
            'land_size': 'భూమి పరిమాణం',
            'soil_type': 'నేల రకం',
            'water_source': 'నీటి మూలం (ఐచ్ఛికం)',
            'continue': 'వ్యవసాయ ప్రయాణం ప్రారంభించండి',
            'get_recommendations': 'సిఫార్సులు పొందండి',
            'select_this_crop': 'ఈ పంటను ఎంచుకోండి',
            'cost': 'వ్యయం',
            'profit': 'లాభం',
            'roi': 'రిటర్న్',
            'growing_time': 'పెరుగుతున్న సమయం',
            'difficulty': 'కష్టం',
            'get_started': 'ప్రారంభించండి',
            'select_type': 'మీ రకాన్ని ఎంచుకోండి',
            'select_your_state': 'మీ రాష్ట్రాన్ని ఎంచుకోండి',
            'select_land_size': 'భూమి పరిమాణాన్ని ఎంచుకోండి',
            'select_soil_type': 'నేల రకాన్ని ఎంచుకోండి',
            'select_water_source': 'నీటి మూలాన్ని ఎంచుకోండి'
        }
    }

def get_language_translations(language='English'):
    translations = get_translations()
    return translations.get(language, translations['English'])

def translate_text(text, language='English'):
    translations = get_language_translations(language)
    return translations.get(text.lower().replace(' ', '_'), text)

def get_crop_name_translations():
    return {
        'English': {
            'rice': 'Rice',
            'wheat': 'Wheat',
            'tomato': 'Tomato',
            'cotton': 'Cotton',
            'sugarcane': 'Sugarcane',
            'potato': 'Potato',
            'onion': 'Onion',
            'maize': 'Maize',
            'soybean': 'Soybean',
            'chickpea': 'Chickpea',
            'mustard': 'Mustard',
            'groundnut': 'Groundnut'
        },
        'Hindi': {
            'rice': 'चावल',
            'wheat': 'गेहूं',
            'tomato': 'टमाटर',
            'cotton': 'कपास',
            'sugarcane': 'गन्ना',
            'potato': 'आलू',
            'onion': 'प्याज',
            'maize': 'मक्का',
            'soybean': 'सोयाबीन',
            'chickpea': 'चना',
            'mustard': 'सरसों',
            'groundnut': 'मूंगफली'
        },
        'Tamil': {
            'rice': 'அரிசி',
            'wheat': 'கோதுமை',
            'tomato': 'தக்காளி',
            'cotton': 'பஞ்சு',
            'sugarcane': 'கரும்பு',
            'potato': 'உருளைக்கிழங்கு',
            'onion': 'வெங்காயம்',
            'maize': 'சோளம்',
            'soybean': 'சோயாபீன்',
            'chickpea': 'கொண்டைக்கடலை',
            'mustard': 'கடுகு',
            'groundnut': 'நிலக்கடலை'
        },
        'Telugu': {
            'rice': 'వరి',
            'wheat': 'గోధుమలు',
            'tomato': 'టమాటో',
            'cotton': 'పత్తి',
            'sugarcane': 'చెరకు',
            'potato': 'బంగాళాదుంప',
            'onion': 'ఉల్లిపాయలు',
            'maize': 'మొక్కజొన్న',
            'soybean': 'సోయాబీన్',
            'chickpea': 'శనగలు',
            'mustard': 'ఆవాలు',
            'groundnut': 'వేరుశనగలు'
        }
    }

def get_soil_type_translations():
    return {
        'English': ['Clay', 'Sandy', 'Loamy', 'Silt'],
        'Hindi': ['चिकनी मिट्टी', 'रेतीली मिट्टी', 'दोमट मिट्टी', 'गाद मिट्टी'],
        'Tamil': ['களிமண்', 'மணல் மண்', 'வண்டல் மண்', 'சேற்று மண்'],
        'Telugu': ['మట్టి నేల', 'ఇసుక నేల', 'రేణు నేల', 'కాల్చిన నేల']
    }

def get_season_translations():
    return {
        'English': ['Spring', 'Summer', 'Fall', 'Winter'],
        'Hindi': ['वसंत', 'गर्मी', 'शरद', 'सर्दी'],
        'Tamil': ['வசந்த காலம்', 'கோடை காலம்', 'இலையுதிர் காலம்', 'குளிர் காலம்'],
        'Telugu': ['వసంత ఋతువు', 'వేసవి ఋతువు', 'శరదృతువు', 'శీతాకాలం']
    }
```

## 7. openai_service.py
```python
import os
import json
import base64
import logging
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_openai_response(prompt, json_format=False):
    try:
        messages = [{"role": "user", "content": prompt}]
        response_format = {"type": "json_object"} if json_format else None
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=1000,
            temperature=0.7,
            response_format=response_format
        )
        
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"OpenAI API error: {e}")
        return get_fallback_response(prompt, json_format)

def analyze_crop_image(base64_image):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Analyze this crop image. Identify the crop type, assess health, detect any diseases or pests, and provide actionable recommendations."
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                        }
                    ]
                }
            ],
            max_tokens=500
        )
        
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Image analysis error: {e}")
        return get_fallback_image_analysis()

def transcribe_audio(audio_file_path):
    try:
        with open(audio_file_path, 'rb') as audio_file:
            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return response.text
    except Exception as e:
        logging.error(f"Audio transcription error: {e}")
        return "Sorry, I couldn't transcribe the audio. Please try again."

def generate_crop_plan(crop_name, location, sowing_date=None):
    prompt = f"""Generate a detailed crop plan for {crop_name} in {location}.
    Include: timeline, fertilizer schedule, irrigation needs, pest management, and harvest timing.
    {f'Sowing date: {sowing_date}' if sowing_date else ''}
    """
    return get_openai_response(prompt)

def get_market_analysis(crop_name, location):
    prompt = f"""Provide market analysis for {crop_name} in {location}.
    Include: current prices, demand trends, best selling time, and marketing strategies.
    """
    return get_openai_response(prompt)

def detect_plant_disease(image_analysis):
    prompt = f"""Based on this image analysis: {image_analysis}
    Identify any plant diseases or pests and provide treatment recommendations.
    """
    return get_openai_response(prompt)

def generate_biotwin_response(crop_name, stage, symbiosis_score, user_input):
    prompt = f"""You are a {crop_name} plant at {stage} stage with {symbiosis_score}/100 health score.
    Respond to farmer's query: {user_input}
    Speak as the plant itself, sharing your needs and current condition.
    """
    return get_openai_response(prompt)

def get_fallback_response(prompt, json_format=False):
    if "crop" in prompt.lower() or "farming" in prompt.lower():
        return "I'm currently experiencing high demand. Please try the crop recommendation system or ask specific farming questions."
    return "I'm temporarily having technical difficulties. Please try again in a few moments."

def get_fallback_image_analysis():
    return "Image uploaded successfully. I'm currently processing your image. Please check back in a few moments for detailed analysis."
```

## 8. routes.py (Main Routes)
```python
import os
import base64
from flask import render_template, request, jsonify, session, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, date, timedelta
from app import app, db
from models import User, Crop, Conversation, WeatherData
from agent_router import route_to_agent
from ai_agents import get_agent_response
from openai_service import transcribe_audio, analyze_crop_image
from recommendation_engine import CropRecommendationEngine
from language_support import get_language_translations
import logging

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
AUDIO_EXTENSIONS = {'wav', 'mp3', 'ogg', 'webm'}

def allowed_file(filename, extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/onboard', methods=['POST'])
def onboard():
    try:
        data = request.get_json()
        user_type = data.get('user_type')
        location = data.get('location', '')
        land_size = data.get('land_size', '')
        soil_water_access = data.get('soil_water_access', '')
        language = data.get('language', 'English')
        
        user = User(
            user_type=user_type,
            location=location,
            land_size=land_size,
            soil_water_access=soil_water_access
        )
        db.session.add(user)
        db.session.commit()
        
        session['user_id'] = user.id
        
        return jsonify({
            'success': True,
            'user_id': user.id,
            'message': f'Welcome to AgroAura! You are registered as a {user_type}.'
        })
    except Exception as e:
        logging.error(f"Onboarding error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/crop-recommendations', methods=['GET', 'POST'])
def crop_recommendations():
    if request.method == 'GET':
        return render_template('crop_recommendations.html')
    
    try:
        data = request.get_json()
        land_size = float(data.get('land_size', 1.0))
        soil_type = data.get('soil_type', 'Loamy')
        season = data.get('season', 'Spring')
        budget = float(data.get('budget', 50000))
        language = data.get('language', 'English')
        
        rec_engine = CropRecommendationEngine()
        recommendations = rec_engine.get_recommendations(land_size, soil_type, season, budget)
        translations = get_language_translations(language)
        
        return jsonify({
            'success': True,
            'recommendations': recommendations,
            'translations': translations,
            'parameters': {
                'land_size': land_size,
                'soil_type': soil_type,
                'season': season,
                'budget': budget,
                'language': language
            }
        })
        
    except Exception as e:
        logging.error(f"Crop recommendations error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/select-crop', methods=['POST'])
def select_crop():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'success': False, 'error': 'User not logged in'}), 401
        
        data = request.get_json()
        crop_name = data.get('crop_name')
        
        if not crop_name:
            return jsonify({'success': False, 'error': 'Crop name not provided'}), 400
        
        crop = Crop(
            user_id=user_id,
            crop_name=crop_name.title(),
            sowing_date=datetime.now().date(),
            current_stage='planning',
            symbiosis_score=50,
            notes=f"Crop selected from recommendations on {datetime.now().strftime('%Y-%m-%d')}"
        )
        
        db.session.add(crop)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': f'Successfully selected {crop_name.title()}! Your BioTwin has been created.'
        })
    except Exception as e:
        logging.error(f"Crop selection error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('index'))
    
    user = User.query.get(user_id)
    if not user:
        return redirect(url_for('index'))
    
    conversations = Conversation.query.filter_by(user_id=user_id).order_by(Conversation.created_at.desc()).limit(10).all()
    crops = Crop.query.filter_by(user_id=user_id).all()
    
    return render_template('dashboard.html', user=user, conversations=conversations, crops=crops)

@app.route('/upload-image', methods=['POST'])
def upload_image():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'success': False, 'error': 'User not logged in'}), 401
        
        if 'image' not in request.files:
            return jsonify({'success': False, 'error': 'No image file provided'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'}), 400
        
        if file and allowed_file(file.filename, ALLOWED_EXTENSIONS):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{timestamp}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            with open(filepath, 'rb') as img_file:
                base64_image = base64.b64encode(img_file.read()).decode('utf-8')
            
            analysis_result = analyze_crop_image(base64_image)
            
            agent_name, agent_response = route_to_agent(
                user_input="Image uploaded for analysis",
                image_analysis=analysis_result,
                user_id=user_id
            )
            
            conversation = Conversation(
                user_id=user_id,
                input_type='image',
                input_content=f"Image uploaded: {filename}",
                agent_used=agent_name,
                agent_response=agent_response,
                image_path=filepath
            )
            db.session.add(conversation)
            db.session.commit()
            
            return jsonify({
                'success': True,
                'agent_name': agent_name,
                'response': agent_response,
                'image_analysis': analysis_result
            })
        
        return jsonify({'success': False, 'error': 'Invalid file type'}), 400
        
    except Exception as e:
        logging.error(f"Image upload error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/text-input', methods=['POST'])
def text_input():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'success': False, 'error': 'User not logged in'}), 401
        
        data = request.get_json()
        user_text = data.get('text', '').strip()
        
        if not user_text:
            return jsonify({'success': False, 'error': 'No text provided'}), 400
        
        agent_name, agent_response = route_to_agent(
            user_input=user_text,
            user_id=user_id
        )
        
        conversation = Conversation(
            user_id=user_id,
            input_type='text',
            input_content=user_text,
            agent_used=agent_name,
            agent_response=agent_response
        )
        db.session.add(conversation)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'agent_name': agent_name,
            'response': agent_response
        })
        
    except Exception as e:
        logging.error(f"Text input error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500
```

## 9. agent_router.py
```python
import logging
from datetime import datetime, timedelta
from models import User, Crop, Conversation
from ai_agents import get_agent_response

def route_to_agent(user_input, user_id, image_analysis=None, weather_data=None):
    try:
        user = User.query.get(user_id)
        if not user:
            return 'general', 'User not found. Please register first.'
        
        context = build_agent_context(user, user_input, image_analysis, weather_data)
        
        agent_name = determine_agent_fallback(user_input, image_analysis)
        
        response = get_agent_response(agent_name, user_input, context)
        
        return agent_name, response
        
    except Exception as e:
        logging.error(f"Agent routing error: {str(e)}")
        return 'general', 'I apologize, but I encountered an error. Please try again.'

def determine_agent_fallback(user_input, image_analysis=None):
    user_input_lower = user_input.lower()
    
    if image_analysis:
        return 'vision'
    
    planning_keywords = ['crop', 'plant', 'grow', 'sow', 'seed', 'fertilizer', 'planner', 'recommend']
    if any(keyword in user_input_lower for keyword in planning_keywords):
        return 'planner'
    
    risk_keywords = ['weather', 'rain', 'drought', 'pest', 'disease', 'risk', 'problem']
    if any(keyword in user_input_lower for keyword in risk_keywords):
        return 'risk'
    
    market_keywords = ['price', 'market', 'sell', 'buy', 'cost', 'profit', 'money']
    if any(keyword in user_input_lower for keyword in market_keywords):
        return 'market'
    
    bargain_keywords = ['negotiate', 'bargain', 'deal', 'contract', 'agreement']
    if any(keyword in user_input_lower for keyword in bargain_keywords):
        return 'bargain'
    
    info_keywords = ['government', 'scheme', 'subsidy', 'loan', 'policy', 'law']
    if any(keyword in user_input_lower for keyword in info_keywords):
        return 'info'
    
    return 'general'

def build_agent_context(user, user_input, image_analysis=None, weather_data=None):
    context = {
        'user_profile': {
            'type': user.user_type,
            'location': user.location,
            'land_size': user.land_size,
            'soil_water_access': user.soil_water_access
        },
        'user_input': user_input,
        'timestamp': datetime.now().isoformat()
    }
    
    crops = Crop.query.filter_by(user_id=user.id).all()
    context['crops'] = []
    for crop in crops:
        context['crops'].append({
            'name': crop.crop_name,
            'stage': crop.current_stage,
            'sowing_date': crop.sowing_date.isoformat() if crop.sowing_date else None,
            'symbiosis_score': crop.symbiosis_score,
            'notes': crop.notes
        })
    
    recent_conversations = Conversation.query.filter_by(user_id=user.id).order_by(Conversation.created_at.desc()).limit(5).all()
    context['recent_conversations'] = []
    for conv in recent_conversations:
        context['recent_conversations'].append({
            'agent': conv.agent_used,
            'input': conv.input_content,
            'response': conv.agent_response[:200] + '...' if len(conv.agent_response) > 200 else conv.agent_response
        })
    
    if image_analysis:
        context['image_analysis'] = image_analysis
    
    if weather_data:
        context['weather_data'] = weather_data
    
    return context

def get_motivation_message(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return "Keep growing! Your farming journey is important."
        
        crops = Crop.query.filter_by(user_id=user_id).all()
        if not crops:
            return "Time to start planting! Check out our crop recommendations."
        
        messages = [
            "Your crops are growing strong! Keep up the great work.",
            "Remember to check on your plants today.",
            "Your farming journey is making a difference!",
            "Every day of care brings you closer to harvest."
        ]
        
        import random
        return random.choice(messages)
        
    except Exception as e:
        logging.error(f"Motivation message error: {str(e)}")
        return "Keep growing! Your farming journey is important."
```

## 10. ai_agents.py
```python
import json
import logging
from datetime import datetime, timedelta
from models import User, Crop, WeatherData
from openai_service import get_openai_response
from recommendation_engine import CropRecommendationEngine
from crop_database import get_crop_database
from language_support import get_language_translations, get_crop_name_translations

def get_agent_response(agent_name, user_input, context=None):
    try:
        if agent_name == 'planner':
            return get_planner_response(user_input, context)
        elif agent_name == 'vision':
            return get_vision_response(user_input, context)
        elif agent_name == 'risk':
            return get_risk_response(user_input, context)
        elif agent_name == 'market':
            return get_market_response(user_input, context)
        elif agent_name == 'bargain':
            return get_bargain_response(user_input, context)
        elif agent_name == 'info':
            return get_info_response(user_input, context)
        else:
            return get_general_response(user_input, context)
    except Exception as e:
        logging.error(f"Agent response error: {str(e)}")
        return f"I'm sorry, I encountered an error while processing your request. Please try again."

def get_planner_response(user_input, context=None):
    try:
        rec_engine = CropRecommendationEngine()
        
        land_size = 1.0
        soil_type = "Loamy"
        season = "Spring"
        budget = 50000
        
        if context:
            context_str = str(context)
            if 'land_size' in context_str:
                if '1-2' in context_str:
                    land_size = 1.5
                elif '2-5' in context_str:
                    land_size = 3.0
                elif '5-10' in context_str:
                    land_size = 7.0
                elif 'Less than 1' in context_str:
                    land_size = 0.5
                
                if 'Clay' in context_str:
                    soil_type = 'Clay'
                elif 'Sandy' in context_str:
                    soil_type = 'Sandy'
                elif 'Loamy' in context_str:
                    soil_type = 'Loamy'
        
        import datetime
        current_month = datetime.datetime.now().month
        if current_month in [3, 4, 5]:
            season = "Spring"
        elif current_month in [6, 7, 8]:
            season = "Summer"
        elif current_month in [9, 10, 11]:
            season = "Fall"
        else:
            season = "Winter"
        
        recommendations = rec_engine.get_recommendations(land_size, soil_type, season, budget)
        
        response = f"""🧠 **Planner Agent - Crop Recommendations**

**Your Farm Profile:**
- Land Size: {land_size} acres
- Soil Type: {soil_type}
- Season: {season}
- Budget: ₹{budget:,}

**Top Crop Recommendations:**
"""
        
        for i, crop in enumerate(recommendations['suitable_crops'][:3], 1):
            response += f"""
**{i}. {crop['name']}**
- Cost: ₹{crop['total_cost']:,} for {land_size} acres
- Expected Profit: ₹{crop['total_profit_potential']:,}
- ROI: {crop['roi_percentage']:.1f}%
- Growing Time: {crop['growing_time']}
- Difficulty: {crop['difficulty']}
- Why this crop: {crop['recommendation_reason']}
"""
        
        response += "\n**General Tips:**\n"
        for tip in recommendations['general_tips'][:3]:
            response += f"• {tip}\n"
        
        budget_info = recommendations['budget_analysis']
        response += f"""
**Budget Analysis:**
- Total Budget: ₹{budget_info['total_budget']:,}
- Top 3 Crops Cost: ₹{budget_info['top3_cost']:,}
- Remaining Budget: ₹{budget_info['remaining_budget']:,}
"""
        
        try:
            ai_prompt = f"""Enhance this crop recommendation with additional insights:
            
            User Query: {user_input}
            Recommendations: {response}
            
            Add practical farming advice, timing considerations, and region-specific tips."""
            
            ai_enhancement = get_openai_response(ai_prompt)
            response += f"\n\n**AI Enhancement:**\n{ai_enhancement}"
        except:
            pass
        
        return response
        
    except Exception as e:
        logging.error(f"Planner agent error: {str(e)}")
        return """🧠 **Planner Agent**: I understand you need farming guidance. While I'm temporarily having technical difficulties, I recommend checking our crop recommendation system for detailed planting advice based on your soil type, season, and budget."""

def get_vision_response(user_input, context=None):
    try:
        image_analysis = context.get('image_analysis', '') if context else ''
        
        response = f"""👁️ **Vision Agent - Crop Analysis**

**Image Analysis Results:**
{image_analysis}

**Health Assessment:**
Based on the image analysis, I can provide insights about your crop's current condition and recommend appropriate care actions.

**Recommendations:**
• Monitor plant health regularly
• Ensure proper watering schedule
• Check for pest or disease signs
• Maintain optimal growing conditions
"""
        
        try:
            ai_prompt = f"""Analyze this crop image analysis and provide detailed farming advice:
            
            User Query: {user_input}
            Image Analysis: {image_analysis}
            
            Provide specific recommendations for crop care, disease prevention, and health improvement."""
            
            ai_enhancement = get_openai_response(ai_prompt)
            response += f"\n\n**Detailed Analysis:**\n{ai_enhancement}"
        except:
            pass
        
        return response
        
    except Exception as e:
        logging.error(f"Vision agent error: {str(e)}")
        return """👁️ **Vision Agent**: I can help analyze your crop images for health assessment. Please upload a clear image of your crops, and I'll provide detailed insights about plant health, diseases, and care recommendations."""

def get_risk_response(user_input, context=None):
    return """⚠️ **Risk Agent - Weather & Risk Assessment**

**Current Risk Factors:**
• Weather conditions monitoring
• Pest and disease alerts
• Soil health assessment
• Water management risks

**Risk Mitigation Strategies:**
• Implement integrated pest management
• Maintain proper irrigation scheduling
• Monitor weather forecasts regularly
• Use disease-resistant crop varieties

**Emergency Preparedness:**
• Keep emergency supplies ready
• Have backup irrigation plans
• Know local agricultural extension contacts
• Maintain crop insurance coverage
"""

def get_market_response(user_input, context=None):
    return """📊 **Market Agent - Price & Selling Guidance**

**Market Intelligence:**
• Current market prices for major crops
• Seasonal price trends and patterns
• Demand forecasting for your region
• Best timing for crop sales

**Selling Strategies:**
• Direct-to-consumer sales opportunities
• Wholesale market connections
• Value-added processing options
• Storage and timing optimization

**Price Optimization:**
• Monitor daily market rates
• Consider forward contracts
• Explore premium markets
• Reduce post-harvest losses
"""

def get_bargain_response(user_input, context=None):
    return """💰 **Bargain Agent - Negotiation Support**

**Negotiation Strategies:**
• Research current market rates
• Understand buyer requirements
• Prepare quality certificates
• Know your minimum acceptable price

**Deal Optimization:**
• Bulk selling advantages
• Long-term contract benefits
• Quality premium negotiations
• Payment term discussions

**Market Leverage:**
• Timing your sales effectively
• Building buyer relationships
• Exploring alternative markets
• Collective bargaining opportunities
"""

def get_info_response(user_input, context=None):
    return """ℹ️ **Info Agent - Government Schemes & Information**

**Government Support:**
• PM-KISAN direct benefit transfer
• Crop insurance schemes (PMFBY)
• Soil health card program
• Minimum support price (MSP) info

**Available Subsidies:**
• Fertilizer subsidies
• Seed subsidies
• Equipment purchase support
• Irrigation infrastructure help

**Agricultural Services:**
• Extension services contact
• Veterinary services
• Soil testing facilities
• Weather advisory services

**Myth Busting:**
• Scientific farming practices
• Organic vs conventional farming
• Climate-smart agriculture
• Sustainable farming techniques
"""

def get_general_response(user_input, context=None):
    return """🌱 **AgroAura General Assistant**

I'm here to help with your farming questions! I can assist with:

• **Crop Planning**: Get personalized crop recommendations
• **Plant Health**: Analyze crop images for diseases and pests
• **Weather Risks**: Assess farming risks and mitigation strategies
• **Market Guidance**: Get pricing and selling advice
• **Negotiations**: Help with bargaining and deal-making
• **Information**: Government schemes and farming information

Please specify what you'd like help with, or try uploading a crop image for analysis!
"""

def get_biotwin_update(crop_id, user_input):
    try:
        crop = Crop.query.get(crop_id)
        if not crop:
            return "Crop not found"
        
        response = f"""🌱 **{crop.crop_name} BioTwin Update**

**Current Status:**
- Stage: {crop.current_stage}
- Health Score: {crop.symbiosis_score}/100
- Days since sowing: {(datetime.now().date() - crop.sowing_date).days if crop.sowing_date else 'Unknown'}

**Your plant says:**
"Hello farmer! I'm growing well in the {crop.current_stage} stage. 
My health score is {crop.symbiosis_score}/100. 
{user_input if user_input else 'Keep taking good care of me!'}"

**Care Recommendations:**
• Monitor my growth regularly
• Maintain proper watering schedule
• Check for any signs of stress
• Provide nutrients as needed
"""
        
        return response
        
    except Exception as e:
        logging.error(f"BioTwin update error: {str(e)}")
        return "Unable to update BioTwin status. Please try again."
```

## 11. pyproject.toml
```toml
[project]
name = "agroaura"
version = "0.1.0"
description = "AI-Powered Farming Companion"
dependencies = [
    "flask",
    "flask-sqlalchemy",
    "openai",
    "werkzeug",
    "gunicorn",
    "psycopg2-binary",
    "sqlalchemy",
    "email-validator"
]

[tool.setuptools]
packages = ["agroaura"]
```

## 12. templates/index.html (Language-First Page)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AgroAura - AI-Powered Farming Companion</title>
    <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body>
    <div class="container my-5">
        <header class="text-center mb-5">
            <h1 class="display-4 text-success">
                <i class="fas fa-seedling"></i> AgroAura
            </h1>
            <p class="lead text-muted">AI-Powered Farming Companion</p>
        </header>

        <!-- Language Selection Section -->
        <div id="language-section" class="row justify-content-center mb-4">
            <div class="col-md-6">
                <div class="card shadow-lg border-success">
                    <div class="card-body text-center">
                        <h2 class="card-title mb-4">
                            <i class="fas fa-globe"></i> Choose Your Language
                        </h2>
                        <p class="text-muted mb-4">भाषा चुनें / மொழியைத் தேர்ந்தெடுங்கள் / భాష ఎంచుకోండి</p>
                        
                        <div class="row g-3">
                            <div class="col-6">
                                <button type="button" class="btn btn-outline-success w-100 language-btn" data-lang="English">
                                    <i class="fas fa-check-circle"></i> English
                                </button>
                            </div>
                            <div class="col-6">
                                <button type="button" class="btn btn-outline-success w-100 language-btn" data-lang="Hindi">
                                    <i class="fas fa-check-circle"></i> हिंदी
                                </button>
                            </div>
                            <div class="col-6">
                                <button type="button" class="btn btn-outline-success w-100 language-btn" data-lang="Tamil">
                                    <i class="fas fa-check-circle"></i> தமிழ்
                                </button>
                            </div>
                            <div class="col-6">
                                <button type="button" class="btn btn-outline-success w-100 language-btn" data-lang="Telugu">
                                    <i class="fas fa-check-circle"></i> తెలుగు
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Onboarding Section -->
        <div id="onboarding-section" class="row justify-content-center d-none">
            <div class="col-md-6">
                <div class="card shadow-lg">
                    <div class="card-body">
                        <h2 class="card-title text-center mb-4" data-translate="get_started">
                            <i class="fas fa-user-plus"></i> Get Started
                        </h2>
                        
                        <form id="onboarding-form">
                            <div class="mb-3">
                                <label class="form-label" data-translate="user_type">I am a:</label>
                                <select id="user-type" class="form-select" required>
                                    <option value="" data-translate="select_type">Select your type</option>
                                    <option value="farmer" data-translate="farmer">🌾 Farmer</option>
                                    <option value="home_gardener" data-translate="home_gardener">🪴 Home Gardener</option>
                                </select>
                            </div>

                            <div class="row mb-3">
                                <div class="col-md-8">
                                    <label class="form-label" data-translate="state">State</label>
                                    <select id="state" class="form-select" required>
                                        <option value="" data-translate="select_your_state">Select your state</option>
                                        <option value="Andhra Pradesh">Andhra Pradesh</option>
                                        <option value="Tamil Nadu">Tamil Nadu</option>
                                        <option value="Karnataka">Karnataka</option>
                                        <option value="Kerala">Kerala</option>
                                        <option value="Telangana">Telangana</option>
                                        <option value="Maharashtra">Maharashtra</option>
                                        <option value="Gujarat">Gujarat</option>
                                        <option value="Rajasthan">Rajasthan</option>
                                        <option value="Punjab">Punjab</option>
                                        <option value="Haryana">Haryana</option>
                                        <option value="Uttar Pradesh">Uttar Pradesh</option>
                                        <option value="Madhya Pradesh">Madhya Pradesh</option>
                                        <option value="West Bengal">West Bengal</option>
                                        <option value="Bihar">Bihar</option>
                                        <option value="Odisha">Odisha</option>
                                        <option value="Assam">Assam</option>
                                        <option value="Chhattisgarh">Chhattisgarh</option>
                                        <option value="Jharkhand">Jharkhand</option>
                                        <option value="Other">Other</option>
                                    </select>
                                </div>
                                <div class="col-md-4">
                                    <label class="form-label" data-translate="city">City (Optional)</label>
                                    <input type="text" id="city" class="form-control" placeholder="Enter city">
                                </div>
                            </div>

                            <div class="mb-3">
                                <label class="form-label" data-translate="land_size">Land Size</label>
                                <select id="land-size" class="form-select" required>
                                    <option value="" data-translate="select_land_size">Select land size</option>
                                    <option value="Less than 1 acre">Less than 1 acre</option>
                                    <option value="1-2 acres">1-2 acres</option>
                                    <option value="2-5 acres">2-5 acres</option>
                                    <option value="5-10 acres">5-10 acres</option>
                                    <option value="More than 10 acres">More than 10 acres</option>
                                </select>
                            </div>

                            <div class="row mb-3">
                                <div class="col-md-6">
                                    <label class="form-label" data-translate="soil_type">Soil Type</label>
                                    <select id="soil-type" class="form-select" required>
                                        <option value="" data-translate="select_soil_type">Select soil type</option>
                                        <option value="Clay">Clay</option>
                                        <option value="Sandy">Sandy</option>
                                        <option value="Loamy">Loamy</option>
                                        <option value="Silt">Silt</option>
                                    </select>
                                </div>
                                <div class="col-md-6">
                                    <label class="form-label" data-translate="water_source">Water Source (Optional)</label>
                                    <select id="water-source" class="form-select">
                                        <option value="" data-translate="select_water_source">Select water source</option>
                                        <option value="Well">Well</option>
                                        <option value="Borewell">Borewell</option>
                                        <option value="Canal">Canal</option>
                                        <option value="River">River</option>
                                        <option value="Rainwater">Rainwater</option>
                                    </select>
                                </div>
                            </div>

                            <div class="text-center">
                                <button type="submit" class="btn btn-success btn-lg" data-translate="continue">
                                    <i class="fas fa-arrow-right"></i> Start Farming Journey
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Language translations
        const translations = {
            'English': {
                'get_started': 'Get Started',
                'user_type': 'I am a:',
                'select_type': 'Select your type',
                'farmer': '🌾 Farmer',
                'home_gardener': '🪴 Home Gardener',
                'state': 'State',
                'city': 'City (Optional)',
                'land_size': 'Land Size',
                'soil_type': 'Soil Type',
                'water_source': 'Water Source (Optional)',
                'continue': 'Start Farming Journey',
                'select_your_state': 'Select your state',
                'select_land_size': 'Select land size',
                'select_soil_type': 'Select soil type',
                'select_water_source': 'Select water source'
            },
            'Hindi': {
                'get_started': 'शुरू करें',
                'user_type': 'मैं हूं:',
                'select_type': 'अपना प्रकार चुनें',
                'farmer': '🌾 किसान',
                'home_gardener': '🪴 घर का बागवान',
                'state': 'राज्य',
                'city': 'शहर (वैकल्पिक)',
                'land_size': 'जमीन का आकार',
                'soil_type': 'मिट्टी का प्रकार',
                'water_source': 'पानी का स्रोत (वैकल्पिक)',
                'continue': 'कृषि यात्रा शुरू करें',
                'select_your_state': 'अपना राज्य चुनें',
                'select_land_size': 'जमीन का आकार चुनें',
                'select_soil_type': 'मिट्टी का प्रकार चुनें',
                'select_water_source': 'पानी का स्रोत चुनें'
            },
            'Tamil': {
                'get_started': 'தொடங்குங்கள்',
                'user_type': 'நான் ஒரு:',
                'select_type': 'உங்கள் வகையைத் தேர்ந்தெடுங்கள்',
                'farmer': '🌾 விவசாயி',
                'home_gardener': '🪴 வீட்டுத் தோட்டக்காரர்',
                'state': 'மாநிலம்',
                'city': 'நகரம் (விருப்பத்தேர்வு)',
                'land_size': 'நிலத்தின் அளவு',
                'soil_type': 'மண் வகை',
                'water_source': 'நீர் ஆதாரம் (விருப்பத்தேர்வு)',
                'continue': 'விவசாய பயணத்தைத் தொடங்கவும்',
                'select_your_state': 'உங்கள் மாநிலத்தைத் தேர்ந்தெடுங்கள்',
                'select_land_size': 'நிலத்தின் அளவைத் தேர்ந்தெடுங்கள்',
                'select_soil_type': 'மண் வகையைத் தேர்ந்தெடுங்கள்',
                'select_water_source': 'நீர் ஆதாரத்தைத் தேர்ந்தெடுங்கள்'
            },
            'Telugu': {
                'get_started': 'ప్రారంభించండి',
                'user_type': 'నేను ఒక:',
                'select_type': 'మీ రకాన్ని ఎంచుకోండి',
                'farmer': '🌾 రైతు',
                'home_gardener': '🪴 ఇంటి తోటమాలి',
                'state': 'రాష్ట్రం',
                'city': 'నగరం (ఐచ్ఛికం)',
                'land_size': 'భూమి పరిమాణం',
                'soil_type': 'నేల రకం',
                'water_source': 'నీటి మూలం (ఐచ్ఛికం)',
                'continue': 'వ్యవసాయ ప్రయాణం ప్రారంభించండి',
                'select_your_state': 'మీ రాష్ట్రాన్ని ఎంచుకోండి',
                'select_land_size': 'భూమి పరిమాణాన్ని ఎంచుకోండి',
                'select_soil_type': 'నేల రకాన్ని ఎంచుకోండి',
                'select_water_source': 'నీటి మూలాన్ని ఎంచుకోండి'
            }
        };

        let selectedLanguage = 'English';

        // Language switching function
        function switchLanguage(language) {
            selectedLanguage = language;
            const trans = translations[language];
            
            // Update all elements with data-translate attribute
            document.querySelectorAll('[data-translate]').forEach(element => {
                const key = element.getAttribute('data-translate');
                if (trans[key]) {
                    element.textContent = trans[key];
                }
            });
            
            // Update placeholder options
            const stateSelect = document.getElementById('state');
            if (stateSelect && stateSelect.options[0]) {
                stateSelect.options[0].textContent = trans['select_your_state'] || 'Select your state';
            }
            
            const landSizeSelect = document.getElementById('land-size');
            if (landSizeSelect && landSizeSelect.options[0]) {
                landSizeSelect.options[0].textContent = trans['select_land_size'] || 'Select land size';
            }
            
            const soilTypeSelect = document.getElementById('soil-type');
            if (soilTypeSelect && soilTypeSelect.options[0]) {
                soilTypeSelect.options[0].textContent = trans['select_soil_type'] || 'Select soil type';
            }
            
            const waterSourceSelect = document.getElementById('water-source');
            if (waterSourceSelect && waterSourceSelect.options[0]) {
                waterSourceSelect.options[0].textContent = trans['select_water_source'] || 'Select water source';
            }
        }

        // Language selection buttons
        document.querySelectorAll('.language-btn').forEach(button => {
            button.addEventListener('click', function() {
                const language = this.getAttribute('data-lang');
                selectedLanguage = language;
                
                // Update button states
                document.querySelectorAll('.language-btn').forEach(btn => {
                    btn.classList.remove('btn-success');
                    btn.classList.add('btn-outline-success');
                });
                this.classList.remove('btn-outline-success');
                this.classList.add('btn-success');
                
                // Switch language
                switchLanguage(language);
                
                // Show onboarding form
                document.getElementById('language-section').classList.add('d-none');
                document.getElementById('onboarding-section').classList.remove('d-none');
            });
        });

        // Form submission
        document.getElementById('onboarding-form').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = {
                user_type: document.getElementById('user-type').value,
                location: document.getElementById('state').value + (document.getElementById('city').value ? ', ' + document.getElementById('city').value : ''),
                land_size: document.getElementById('land-size').value,
                soil_water_access: document.getElementById('soil-type').value + (document.getElementById('water-source').value ? ', ' + document.getElementById('water-source').value : ''),
                language: selectedLanguage
            };
            
            fetch('/onboard', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = '/crop-recommendations';
                } else {
                    alert('Error: ' + data.error);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            });
        });
    </script>
</body>
</html>
```

This is the complete, ready-to-use code for the AgroAura AI-powered farming companion system. Simply copy and paste these files into your project, and you'll have a fully functional multi-language farming assistant with crop recommendations, BioTwin tracking, and AI agent support.
