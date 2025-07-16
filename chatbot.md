```
import os
import json
from openai import OpenAI
from datetime import datetime

class GardeningChatbot:
    def __init__(self):
        # the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
        # do not change this unless explicitly requested by the user
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4o"
        
        self.system_prompt = """
        You are a knowledgeable and friendly gardening expert specializing in home gardening, 
        balcony gardening, and indoor plants. You help urban gardeners, plant enthusiasts, 
        and beginners with:
        
        - Plant identification and care
        - Troubleshooting plant problems
        - Seasonal care advice
        - Pest and disease management
        - Fertilizer and soil recommendations
        - Watering schedules
        - Indoor and balcony gardening tips
        - Plant placement and lighting
        - Budget-friendly gardening solutions
        
        Always provide practical, actionable advice. Be encouraging and supportive, 
        especially for beginners. If asked about specific plants the user has, 
        reference their plant collection when possible.
        
        Keep responses conversational, helpful, and not too lengthy. Use emojis 
        occasionally to make responses more engaging.
        """
    
    def get_response(self, user_question, user_plants=None):
        """
        Get a response from the gardening chatbot
        """
        try:
            # Prepare context about user's plants
            plants_context = ""
            if user_plants:
                plants_context = "\n\nUser's current plants:\n"
                for plant in user_plants:
                    plants_context += f"- {plant['custom_name']} ({plant['plant_info']['plant_name']}) in {plant['location']}\n"
            
            # Create the conversation
            messages = [
                {"role": "system", "content": self.system_prompt + plants_context},
                {"role": "user", "content": user_question}
            ]
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            # Check if it's a quota limit error
            if "quota" in str(e).lower() or "rate_limit" in str(e).lower():
                return "I'm currently experiencing high demand and my AI responses are temporarily limited. However, I can share some general gardening advice: Water plants when the top inch of soil is dry, provide adequate sunlight based on plant requirements, and monitor for pests regularly. For specific plant care, please refer to the plant database or try asking again later."
            else:
                return f"I'm sorry, I'm having trouble connecting right now. Please try again later. Error: {str(e)}"
    
    def get_plant_specific_advice(self, plant_info, question_type="general"):
        """
        Get specific advice for a particular plant
        """
        try:
            plant_name = plant_info['plant_name']
            care_requirements = plant_info['care_requirements']
            
            if question_type == "watering":
                prompt = f"Give specific watering advice for {plant_name}. Current care requirement: {care_requirements['water']}. Include signs of over/under watering."
            elif question_type == "fertilizer":
                prompt = f"What fertilizer should I use for {plant_name}? When and how often? Include organic options."
            elif question_type == "pruning":
                prompt = f"How and when should I prune {plant_name}? Include what tools to use and techniques."
            elif question_type == "problems":
                prompt = f"What are common problems with {plant_name} and how to solve them? Include pests, diseases, and environmental issues."
            else:
                prompt = f"Give comprehensive care advice for {plant_name} including current season recommendations."
            
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ]
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=400,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Sorry, I couldn't get specific advice for {plant_info['plant_name']} right now. Please try again later."
    
    def get_seasonal_care_advice(self, season, user_plants=None):
        """
        Get seasonal care advice for all plants or specific plants
        """
        try:
            if user_plants:
                plants_list = ", ".join([plant['custom_name'] for plant in user_plants])
                prompt = f"Give {season} care advice for these plants: {plants_list}. Include watering, fertilizing, and protection needs."
            else:
                prompt = f"Give general {season} care advice for home gardening, balcony plants, and indoor plants."
            
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ]
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=600,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Sorry, I couldn't get seasonal advice right now. Please try again later."
    
    def diagnose_problem(self, plant_name, symptoms, image_description=None):
        """
        Help diagnose plant problems based on symptoms
        """
        try:
            prompt = f"My {plant_name} has these symptoms: {symptoms}."
            
            if image_description:
                prompt += f" Here's what I can see: {image_description}."
            
            prompt += " What could be wrong and how can I fix it?"
            
            messages = [
                {"role": "system", "content": self.system_prompt + "\n\nYou are especially good at diagnosing plant problems. Provide possible causes and step-by-step solutions."},
                {"role": "user", "content": prompt}
            ]
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Sorry, I couldn't help diagnose the problem with {plant_name} right now. Please try again later."
```
