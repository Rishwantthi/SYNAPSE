"""
Voice processing module for handling speech input in regional languages
and converting text to speech for farmer-friendly interaction.
"""

import streamlit as st
import re

class VoiceProcessor:
    def __init__(self):
        self.supported_languages = ['English', 'Hindi', 'Tamil', 'Telugu', 'Kannada']
        A
    def process_voice_input(self, text_input, detected_language='English'):
        """
        Process voice/text input and extract farming-related information.
        
        Args:
            text_input: Transcribed text from voice or direct text input
            detected_language: Detected language of the input
            
        Returns:
            dict: Extracted farming information
        """
        
        # Normalize text input
        text_input = text_input.lower().strip()
        
        # Extract farming details based on language
        extracted_info = self._extract_farming_details(text_input, detected_language)
        
        return extracted_info
    
    def _extract_farming_details(self, text, language):
        """Extract farming details from text input."""
        
        # Initialize extraction results
        farming_info = {
            'land_size': None,
            'land_type': None,
            'crop_preference': None,
            'location': None,
            'soil_type': None,
            'season': None,
            'budget': None,
            'water_availability': None,
            'language': language
        }
        
        # Language-specific keyword extraction
        if language == 'Hindi':
            farming_info.update(self._extract_hindi_details(text))
        elif language == 'Tamil':
            farming_info.update(self._extract_tamil_details(text))
        elif language == 'Telugu':
            farming_info.update(self._extract_telugu_details(text))
        elif language == 'Kannada':
            farming_info.update(self._extract_kannada_details(text))
        else:
            farming_info.update(self._extract_english_details(text))
        
        return farming_info
    
    def _extract_english_details(self, text):
        """Extract farming details from English text."""
        
        details = {}
        
        # Land size extraction
        size_patterns = [
            r'(\d+(?:\.\d+)?)\s*(?:acre|acres|hectare|hectares)',
            r'(\d+(?:\.\d+)?)\s*(?:bigha|bighas)',
            r'(\d+(?:\.\d+)?)\s*(?:square feet|sq ft|square meter|sq m)'
        ]
        
        for pattern in size_patterns:
            match = re.search(pattern, text)
            if match:
                details['land_size'] = float(match.group(1))
                break
        
        # Crop extraction
        crops = ['rice', 'wheat', 'corn', 'tomato', 'potato', 'onion', 'sugarcane', 'cotton', 'turmeric']
        for crop in crops:
            if crop in text:
                details['crop_preference'] = crop.capitalize()
                break
        
        # Soil type extraction
        soil_types = ['clay', 'sandy', 'loamy', 'silty', 'black', 'red']
        for soil in soil_types:
            if soil in text:
                details['soil_type'] = soil.capitalize()
                break
        
        # Season extraction
        seasons = ['spring', 'summer', 'winter', 'monsoon', 'rainy']
        for season in seasons:
            if season in text:
                details['season'] = season.capitalize()
                break
        
        return details
    
    def _extract_hindi_details(self, text):
        """Extract farming details from Hindi text."""
        
        details = {}
        
        # Common Hindi farming terms
        if 'एकड़' in text:
            # Extract acre information
            match = re.search(r'(\d+(?:\.\d+)?)\s*एकड़', text)
            if match:
                details['land_size'] = float(match.group(1))
        
        # Crop names in Hindi
        hindi_crops = {
            'चावल': 'Rice', 'गेहूं': 'Wheat', 'मक्का': 'Corn', 'टमाटर': 'Tomato',
            'आलू': 'Potato', 'प्याज': 'Onion', 'गन्ना': 'Sugarcane', 'कपास': 'Cotton',
            'हल्दी': 'Turmeric', 'मिर्च': 'Chili', 'बैंगन': 'Eggplant'
        }
        
        for hindi_crop, english_crop in hindi_crops.items():
            if hindi_crop in text:
                details['crop_preference'] = english_crop
                break
        
        # Soil types in Hindi
        hindi_soils = {
            'चिकनी': 'Clay', 'रेतीली': 'Sandy', 'दोमट': 'Loamy', 'काली': 'Black', 'लाल': 'Red'
        }
        
        for hindi_soil, english_soil in hindi_soils.items():
            if hindi_soil in text:
                details['soil_type'] = english_soil
                break
        
        return details
    
    def _extract_tamil_details(self, text):
        """Extract farming details from Tamil text."""
        
        details = {}
        
        # Tamil farming terms
        if 'ஏக்கர்' in text:
            # Extract acre information
            match = re.search(r'(\d+(?:\.\d+)?)\s*ஏக்கர்', text)
            if match:
                details['land_size'] = float(match.group(1))
        
        # Crop names in Tamil
        tamil_crops = {
            'அரிசி': 'Rice', 'கோதுமை': 'Wheat', 'சோளம்': 'Corn', 'தக்காளி': 'Tomato',
            'உருளைக்கிழங்கு': 'Potato', 'வெங்காயம்': 'Onion', 'கரும்பு': 'Sugarcane',
            'பருத்தி': 'Cotton', 'மஞ்சள்': 'Turmeric', 'மிளகாய்': 'Chili'
        }
        
        for tamil_crop, english_crop in tamil_crops.items():
            if tamil_crop in text:
                details['crop_preference'] = english_crop
                break
        
        # Soil types in Tamil
        tamil_soils = {
            'களிமண்': 'Clay', 'மணல்': 'Sandy', 'கலவை': 'Loamy', 'கருப்பு': 'Black', 'சிவப்பு': 'Red'
        }
        
        for tamil_soil, english_soil in tamil_soils.items():
            if tamil_soil in text:
                details['soil_type'] = english_soil
                break
        
        return details
    
    def _extract_telugu_details(self, text):
        """Extract farming details from Telugu text."""
        
        details = {}
        
        # Telugu farming terms
        if 'ఎకరాలు' in text or 'ఎకరం' in text:
            # Extract acre information
            match = re.search(r'(\d+(?:\.\d+)?)\s*(?:ఎకరాలు|ఎకరం)', text)
            if match:
                details['land_size'] = float(match.group(1))
        
        # Crop names in Telugu
        telugu_crops = {
            'వరి': 'Rice', 'గోధుమ': 'Wheat', 'మొక్కజొన్న': 'Corn', 'టమోటా': 'Tomato',
            'బంగాళాదుంప': 'Potato', 'ఉల్లిపాయ': 'Onion', 'చెరకు': 'Sugarcane',
            'పత్తి': 'Cotton', 'పసుపు': 'Turmeric', 'మిరపకాయ': 'Chili'
        }
        
        for telugu_crop, english_crop in telugu_crops.items():
            if telugu_crop in text:
                details['crop_preference'] = english_crop
                break
        
        # Soil types in Telugu
        telugu_soils = {
            'బంకమట్టి': 'Clay', 'ఇసుకమట్టి': 'Sandy', 'లోమిమట్టి': 'Loamy', 'నల్లమట్టి': 'Black', 'ఎర్రమట్టి': 'Red'
        }
        
        for telugu_soil, english_soil in telugu_soils.items():
            if telugu_soil in text:
                details['soil_type'] = english_soil
                break
        
        return details
    
    def _extract_kannada_details(self, text):
        """Extract farming details from Kannada text."""
        
        details = {}
        
        # Kannada farming terms (basic implementation)
        if 'ಎಕರೆ' in text:
            # Extract acre information
            match = re.search(r'(\d+(?:\.\d+)?)\s*ಎಕರೆ', text)
            if match:
                details['land_size'] = float(match.group(1))
        
        # Basic Kannada crop names
        kannada_crops = {
            'ಅಕ್ಕಿ': 'Rice', 'ಗೋಧಿ': 'Wheat', 'ಸೋಳ': 'Corn', 'ಟೊಮೇಟೊ': 'Tomato',
            'ಆಲೂಗಡ್ಡೆ': 'Potato', 'ಈರುಳ್ಳಿ': 'Onion', 'ಕಬ್ಬು': 'Sugarcane'
        }
        
        for kannada_crop, english_crop in kannada_crops.items():
            if kannada_crop in text:
                details['crop_preference'] = english_crop
                break
        
        return details
    
    def generate_response(self, recommendations, language='English'):
        """Generate farmer-friendly response in the specified language."""
        
        responses = {
            'English': {
                'greeting': "Based on your input, here are my recommendations:",
                'crop_suggestion': "Recommended crops for your land:",
                'care_schedule': "Daily care schedule:",
                'water_info': "Water requirements:",
                'fertilizer_info': "Fertilizer recommendations:",
                'yield_info': "Expected yield:",
                'tips': "Additional tips:"
            },
            'Hindi': {
                'greeting': "आपकी जानकारी के आधार पर मेरे सुझाव:",
                'crop_suggestion': "आपकी जमीन के लिए सुझाई गई फसलें:",
                'care_schedule': "रोज की देखभाल:",
                'water_info': "पानी की जरूरत:",
                'fertilizer_info': "खाद की सलाह:",
                'yield_info': "अपेक्षित उत्पादन:",
                'tips': "अतिरिक्त सलाह:"
            },
            'Tamil': {
                'greeting': "உங்கள் தகவலின் அடிப்படையில் எனது பரிந்துரைகள்:",
                'crop_suggestion': "உங்கள் நிலத்திற்கு பரிந்துரைக்கப்பட்ட பயிர்கள்:",
                'care_schedule': "தினசரி பராமரிப்பு:",
                'water_info': "நீர் தேவைகள்:",
                'fertilizer_info': "உர பரிந்துரைகள்:",
                'yield_info': "எதிர்பார்க்கப்படும் மகசூல்:",
                'tips': "கூடுதல் குறிப்புகள்:"
            },
            'Telugu': {
                'greeting': "మీ సమాచారం ఆధారంగా నా సిఫార్సులు:",
                'crop_suggestion': "మీ భూమికి సిఫార్సు చేయబడిన పంటలు:",
                'care_schedule': "రోజువారీ సంరక్షణ:",
                'water_info': "నీటి అవసరాలు:",
                'fertilizer_info': "ఎరువుల సిఫార్సులు:",
                'yield_info': "ఊహించిన దిగుబడి:",
                'tips': "అదనపు సలహాలు:"
            }
        }
        
        return responses.get(language, responses['English'])