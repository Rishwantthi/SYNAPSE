```
import base64
import json
import os
from openai import OpenAI
from PIL import Image
import io

class PlantIdentifier:
    def __init__(self):
        # the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
        # do not change this unless explicitly requested by the user
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4o"
    
    def identify_plant(self, image_file):
        """
        Identify a plant from an uploaded image
        """
        try:
            # Convert image to base64
            image = Image.open(image_file)
            buffered = io.BytesIO()
            image.save(buffered, format="JPEG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode()
            
            # Prepare the prompt
            prompt = """
            Please identify this plant and provide detailed information in JSON format with the following structure:
            {
                "plant_name": "common name of the plant",
                "scientific_name": "scientific name",
                "plant_type": "herb/shrub/tree/flowering plant/vegetable/fruit/succulent/etc",
                "difficulty_level": "beginner/intermediate/advanced",
                "indoor_suitable": true/false,
                "care_requirements": {
                    "light": "low/medium/high/bright indirect",
                    "water": "daily/every 2-3 days/weekly/when dry",
                    "humidity": "low/medium/high",
                    "temperature": "temperature range in celsius",
                    "soil_type": "well-draining/moist/sandy/clay/etc"
                },
                "growing_tips": ["tip1", "tip2", "tip3"],
                "common_problems": ["problem1", "problem2"],
                "growth_time": "time to maturity/flowering",
                "suitable_locations": ["balcony", "terrace", "kitchen", "living room", "garden"],
                "budget_estimate": "low/medium/high",
                "seasonal_care": {
                    "spring": "care instructions",
                    "summer": "care instructions",
                    "monsoon": "care instructions",
                    "winter": "care instructions"
                }
            }
            """
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{img_base64}"
                                }
                            }
                        ]
                    }
                ],
                response_format={"type": "json_object"},
                max_tokens=1000
            )
            
            result = json.loads(response.choices[0].message.content)
            return result
            
        except Exception as e:
            # Check if it's a quota limit error
            if "quota" in str(e).lower() or "rate_limit" in str(e).lower():
                return {
                    "plant_name": "Demo Plant",
                    "scientific_name": "Plantae species",
                    "plant_type": "Unknown",
                    "difficulty_level": "intermediate",
                    "indoor_suitable": True,
                    "care_requirements": {
                        "light": "medium",
                        "water": "every 2-3 days",
                        "humidity": "medium",
                        "temperature": "18-25°C",
                        "soil_type": "well-draining"
                    },
                    "growing_tips": [
                        "Monitor plant regularly for signs of stress",
                        "Adjust care based on season and weather",
                        "Water when top inch of soil is dry"
                    ],
                    "common_problems": ["Over-watering", "Under-lighting", "Pests"],
                    "growth_time": "Variable depending on plant type",
                    "suitable_locations": ["balcony", "terrace", "garden"],
                    "budget_estimate": "medium",
                    "seasonal_care": {
                        "spring": "Regular watering and fertilizing",
                        "summer": "Increase watering frequency, provide shade",
                        "monsoon": "Reduce watering, ensure proper drainage",
                        "winter": "Reduce watering, protect from cold"
                    },
                    "note": "Plant identification temporarily unavailable due to API limits. Please try again later or add plant manually."
                }
            else:
                return {
                    "error": f"Failed to identify plant: {str(e)}",
                    "plant_name": "Unknown Plant",
                    "scientific_name": "Unknown",
                    "plant_type": "Unknown",
                    "difficulty_level": "intermediate",
                    "indoor_suitable": True,
                    "care_requirements": {
                        "light": "medium",
                        "water": "when dry",
                        "humidity": "medium",
                        "temperature": "18-25°C",
                        "soil_type": "well-draining"
                    },
                    "growing_tips": ["Monitor plant regularly", "Adjust care based on season"],
                    "common_problems": ["Over-watering", "Under-lighting"],
                    "growth_time": "Variable",
                    "suitable_locations": ["balcony", "terrace"],
                    "budget_estimate": "medium",
                    "seasonal_care": {
                        "spring": "Regular watering and fertilizing",
                        "summer": "Increase watering frequency",
                        "monsoon": "Reduce watering, ensure drainage",
                        "winter": "Reduce watering, protect from cold"
                    }
                }
    
    def get_plant_mood(self, plant_name, last_care_date, care_frequency):
        """
        Determine plant mood based on care schedule
        """
        from datetime import datetime, timedelta
        
        try:
            if isinstance(last_care_date, str):
                last_care = datetime.strptime(last_care_date, "%Y-%m-%d")
            else:
                last_care = last_care_date
            
            days_since_care = (datetime.now() - last_care).days
            
            # Define mood based on care frequency
            if care_frequency == "daily" and days_since_care <= 1:
                return {"mood": "😊", "status": "Happy", "message": "I'm well cared for!"}
            elif care_frequency == "every 2-3 days" and days_since_care <= 3:
                return {"mood": "😊", "status": "Happy", "message": "Feeling great!"}
            elif care_frequency == "weekly" and days_since_care <= 7:
                return {"mood": "😊", "status": "Happy", "message": "All good here!"}
            elif days_since_care <= 2:
                return {"mood": "😐", "status": "Okay", "message": "I'm doing fine, but could use some attention soon."}
            elif days_since_care <= 5:
                return {"mood": "😟", "status": "Needs attention", "message": "I need some care soon!"}
            else:
                return {"mood": "😢", "status": "Neglected", "message": "I really need your attention!"}
                
        except:
            return {"mood": "😐", "status": "Unknown", "message": "Check on me regularly!"}

```
