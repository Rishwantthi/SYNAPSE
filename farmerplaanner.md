**FARMER PLANNER AI**


A multilingual crop recommendation system for Indian farmers supporting English, Hindi, Tamil, and Telugu languages.

## Features

- **Multilingual Support**: Complete interface in 4 languages
- **Indian Crop Database**: Rice, sugarcane, turmeric, onion, cotton, mustard
- **Smart Recommendations**: Based on soil type, season, land size, and budget
- **Currency Localization**: INR (₹) for Indian languages, USD ($) for English
- **Bilingual UI**: Soil types and seasons shown in English + local language


## app.py
```
import streamlit as st
import pandas as pd
from crop_database import get_crop_database
from recommendation_engine import CropRecommendationEngine

# Page configuration
st.set_page_config(
    page_title="Farmer Planner AI",
    page_icon="🌾",
    layout="wide"
)

# Initialize the recommendation engine
@st.cache_resource
def load_recommendation_engine():
    return CropRecommendationEngine()

# Language translations
def get_translations():
    return {
        'English': {
            'title': '🌾 Farmer Planner AI',
            'subtitle': 'Get personalized crop recommendations for your farm',
            'language_prompt': 'Hello! Which language would you like to continue in?',
            'land_size': 'What is the size of your land?',
            'land_size_help': 'Enter your farmland size in acres (e.g., 1.5 acres)',
            'soil_type': 'What type of soil do you have?',
            'soil_help': 'Choose your soil type. If not sure, Loamy is good for most crops.',
            'season': 'When do you want to plant?',
            'season_help': 'Choose your planting season',
            'budget': 'How much money can you spend?',
            'budget_help': 'Enter your budget in dollars for seeds, fertilizer, and supplies',
            'get_recommendations': 'Get My Crop Suggestions',
            'recommendations_title': 'Best Crops for Your Farm',
            'farm_summary': 'Your Farm',
            'acres': 'acres',
            'soil': 'soil',
            'planting': 'planting',
            'budget_text': 'budget',
            'economics': 'Money Details',
            'growing_info': 'Growing Details',
            'cost_per_acre': 'Cost per acre',
            'expected_yield': 'Expected harvest',
            'profit_potential': 'Profit potential',
            'growing_time': 'Growing time',
            'difficulty': 'Difficulty',
            'water_needs': 'Water needs',
            'why_crop': 'Why this crop?',
            'growing_tips': 'Growing Tips',
            'budget_breakdown': 'Budget Breakdown',
            'total_cost': 'Total cost for top 3 crops',
            'your_budget': 'Your budget',
            'can_afford': 'You can afford these crops!',
            'budget_warning': 'Consider fewer crops or cheaper options.',
            'no_crops': 'No suitable crops found. Try different inputs.',
            'general_tips': 'General Tips',
            'about_tool': 'About This Tool',
            'tool_description': 'This AI helper suggests the best crops for your specific farm by considering your land size, soil type, planting season, and budget.',
            'get_started': 'Fill in your farm details above to get started!'
        },
        'Hindi': {
            'title': '🌾 किसान योजना AI',
            'subtitle': 'अपने खेत के लिए व्यक्तिगत फसल सुझाव पाएं',
            'language_prompt': 'नमस्ते! आप किस भाषा में जारी रखना चाहते हैं?',
            'land_size': 'आपकी जमीन का आकार क्या है?',
            'land_size_help': 'अपनी खेती की जमीन एकड़ में लिखें (जैसे 1.5 एकड़)',
            'soil_type': 'आपकी मिट्टी किस प्रकार की है?',
            'soil_help': 'अपनी मिट्टी का प्रकार चुनें। अगर पता नहीं है, तो दोमट अच्छी है।',
            'season': 'आप कब बोना चाहते हैं?',
            'season_help': 'अपना बुवाई का मौसम चुनें',
            'budget': 'आप कितना पैसा खर्च कर सकते हैं?',
            'budget_help': 'बीज, खाद और सामान के लिए अपना बजट रुपयों में लिखें',
            'get_recommendations': 'मेरी फसल सुझाव पाएं',
            'recommendations_title': 'आपके खेत के लिए सबसे अच्छी फसलें',
            'farm_summary': 'आपका खेत',
            'acres': 'एकड़',
            'soil': 'मिट्टी',
            'planting': 'बुवाई',
            'budget_text': 'बजट',
            'economics': 'पैसे की जानकारी',
            'growing_info': 'उगाने की जानकारी',
            'cost_per_acre': 'प्रति एकड़ लागत',
            'expected_yield': 'अपेक्षित फसल',
            'profit_potential': 'लाभ की संभावना',
            'growing_time': 'उगने का समय',
            'difficulty': 'कठिनाई',
            'water_needs': 'पानी की जरूरत',
            'why_crop': 'यह फसल क्यों?',
            'growing_tips': 'उगाने की सलाह',
            'budget_breakdown': 'बजट विवरण',
            'total_cost': 'टॉप 3 फसलों की कुल लागत',
            'your_budget': 'आपका बजट',
            'can_afford': 'आप इन फसलों को उगा सकते हैं!',
            'budget_warning': 'कम फसलें या सस्ते विकल्प चुनें।',
            'no_crops': 'कोई उपयुक्त फसल नहीं मिली। अलग जानकारी दें।',
            'general_tips': 'सामान्य सलाह',
            'about_tool': 'इस टूल के बारे में',
            'tool_description': 'यह AI सहायक आपकी जमीन, मिट्टी, मौसम और बजट के अनुसार सबसे अच्छी फसलों का सुझाव देता है।',
            'get_started': 'शुरू करने के लिए ऊपर अपने खेत की जानकारी भरें!'
        },
        'Tamil': {
            'title': '🌾 விவசாயி திட்ட AI',
            'subtitle': 'உங்கள் பண்ணைக்கான தனிப்பட்ட பயிர் பரிந்துரைகளைப் பெறுங்கள்',
            'language_prompt': 'வணக்கம்! நீங்கள் எந்த மொழியில் தொடர விரும்புகிறீர்கள்?',
            'land_size': 'உங்கள் நிலத்தின் அளவு என்ன?',
            'land_size_help': 'உங்கள் விவசாய நிலத்தின் அளவை ஏக்கரில் உள்ளிடுங்கள் (எ.கா. 1.5 ஏக்கர்)',
            'soil_type': 'உங்களிடம் எந்த வகை மண் உள்ளது?',
            'soil_help': 'உங்கள் மண் வகையைத் தேர்ந்தெடுங்கள். தெரியவில்லை என்றால், களிமண் நல்லது.',
            'season': 'எப்போது விதைக்க விரும்புகிறீர்கள்?',
            'season_help': 'உங்கள் விதைப்பு பருவத்தைத் தேர்ந்தெடுங்கள்',
            'budget': 'நீங்கள் எவ்வளவு பணம் செலவழிக்க முடியும்?',
            'budget_help': 'விதைகள், உரம் மற்றும் பொருட்களுக்கான உங்கள் பட்ஜெட்டை ரூபாயில் உள்ளிடுங்கள்',
            'get_recommendations': 'எனது பயிர் பரிந்துரைகளைப் பெறுங்கள்',
            'recommendations_title': 'உங்கள் பண்ணைக்கான சிறந்த பயிர்கள்',
            'farm_summary': 'உங்கள் பண்ணை',
            'acres': 'ஏக்கர்',
            'soil': 'மண்',
            'planting': 'விதைப்பு',
            'budget_text': 'பட்ஜெட்',
            'economics': 'பணம் விவரங்கள்',
            'growing_info': 'வளர்ப்பு விவரங்கள்',
            'cost_per_acre': 'ஏக்கருக்கான செலவு',
            'expected_yield': 'எதிர்பார்க்கப்படும் அறுவடை',
            'profit_potential': 'லாப சாத்தியம்',
            'growing_time': 'வளரும் நேரம்',
            'difficulty': 'சிரமம்',
            'water_needs': 'நீர் தேவை',
            'why_crop': 'இந்த பயிர் ஏன்?',
            'growing_tips': 'வளர்ப்பு குறிப்புகள்',
            'budget_breakdown': 'பட்ஜெட் விவரம்',
            'total_cost': 'முதல் 3 பயிர்களின் மொத்த செலவு',
            'your_budget': 'உங்கள் பட்ஜெட்',
            'can_afford': 'நீங்கள் இந்த பயிர்களை வளர்க்க முடியும்!',
            'budget_warning': 'குறைவான பயிர்கள் அல்லது மலிவான விருப்பங்களைக் கருத்தில் கொள்ளுங்கள்.',
            'no_crops': 'பொருத்தமான பயிர்கள் கிடைக்கவில்லை. வெவ்வேறு உள்ளீடுகளை முயற்சிக்கவும்.',
            'general_tips': 'பொதுவான குறிப்புகள்',
            'about_tool': 'இந்த கருவி பற்றி',
            'tool_description': 'இந்த AI உதவியாளர் உங்கள் நிலம், மண், பருவம் மற்றும் பட்ஜெட்டைக் கருத்தில் கொண்டு சிறந்த பயிர்களை பரிந்துரைக்கிறது.',
            'get_started': 'தொடங்க மேலே உங்கள் பண்ணை விவரங்களை நிரப்பவும்!'
        },
        'Telugu': {
            'title': '🌾 రైతు ప్రణాళిక AI',
            'subtitle': 'మీ పొలానికి వ్యక్తిగత పంట సిఫార్సులను పొందండి',
            'language_prompt': 'నమస్కారం! మీరు ఏ భాషలో కొనసాగించాలని అనుకుంటున్నారు?',
            'land_size': 'మీ భూమి పరిమాణం ఎంత?',
            'land_size_help': 'మీ వ్యవసాయ భూమి పరిమాణాన్ని ఎకరాల్లో నమోదు చేయండి (ఉదా. 1.5 ఎకరాలు)',
            'soil_type': 'మీకు ఏ రకమైన నేల ఉంది?',
            'soil_help': 'మీ నేల రకాన్ని ఎంచుకోండి. తెలియకపోతే, లోమీ మంచిది.',
            'season': 'మీరు ఎప్పుడు విత్తాలని అనుకుంటున్నారు?',
            'season_help': 'మీ విత్తన సీజన్‌ను ఎంచుకోండి',
            'budget': 'మీరు ఎంత డబ్బు ఖర్చు పెట్టగలరు?',
            'budget_help': 'విత్తనాలు, ఎరువులు మరియు సామాగ్రి కోసం మీ బడ్జెట్‌ను రూపాయల్లో నమోదు చేయండి',
            'get_recommendations': 'నా పంట సిఫార్సులను పొందండి',
            'recommendations_title': 'మీ పొలానికి అత్యుత్తమ పంటలు',
            'farm_summary': 'మీ పొలం',
            'acres': 'ఎకరాలు',
            'soil': 'నేల',
            'planting': 'విత్తనం',
            'budget_text': 'బడ్జెట్',
            'economics': 'డబ్బు వివరాలు',
            'growing_info': 'పెరుగుదల వివరాలు',
            'cost_per_acre': 'ఎకరాకు ఖర్చు',
            'expected_yield': 'ఆశించిన దిగుబడి',
            'profit_potential': 'లాభ సంభావ్యత',
            'growing_time': 'పెరుగుదల సమయం',
            'difficulty': 'కష్టం',
            'water_needs': 'నీటి అవసరం',
            'why_crop': 'ఈ పంట ఎందుకు?',
            'growing_tips': 'పెరుగుదల చిట్కాలు',
            'budget_breakdown': 'బడ్జెట్ వివరణ',
            'total_cost': 'టాప్ 3 పంటల మొత్తం ఖర్చు',
            'your_budget': 'మీ బడ్జెట్',
            'can_afford': 'మీరు ఈ పంటలను పెంచగలరు!',
            'budget_warning': 'తక్కువ పంటలు లేదా తక్కువ ఖర్చైన ఎంపికలను పరిగణించండి.',
            'no_crops': 'తగిన పంటలు దొరకలేదు. వేరే ఇన్‌పుట్‌లను ప్రయత్నించండి.',
            'general_tips': 'సాధారణ చిట్కాలు',
            'about_tool': 'ఈ సాధనం గురించి',
            'tool_description': 'ఈ AI సహాయకుడు మీ భూమి, నేల, సీజన్ మరియు బడ్జెట్‌ను పరిగణనలోకి తీసుకుని అత్యుత్తమ పంటలను సిఫార్సు చేస్తుంది.',
            'get_started': 'ప్రారంభించడానికి పైన మీ పొలం వివరాలను నింపండి!'
        }
    }

def main():
    # Initialize session state
    if 'selected_language' not in st.session_state:
        st.session_state.selected_language = None
    if 'step' not in st.session_state:
        st.session_state.step = 'language_selection'
    
    translations = get_translations()
    
    # Language selection step
    if st.session_state.step == 'language_selection':
        st.title("🌾 Farmer Planner AI")
        st.markdown("**Get personalized crop recommendations for your farm**")
        
        st.subheader("🌍 Language Selection / भाषा चयन / மொழி தேர்வு / భాష ఎంపిక")
        
        languages = ['English', 'Hindi', 'Tamil', 'Telugu']
        selected_lang = st.selectbox(
            "Hello! Which language would you like to continue in? / नमस्ते! आप किस भाषा में जारी रखना चाहते हैं? / வணக்கம்! எந்த மொழியில் தொடர விரும்புகிறீர்கள்? / నమస్కారం! మీరు ఏ భాషలో కొనసాగించాలని అనుకుంటున్నారు?",
            languages,
            index=0
        )
        
        if st.button("Continue / जारी रखें / தொடர் / కొనసాగించండి", type="primary"):
            st.session_state.selected_language = selected_lang
            st.session_state.step = 'farm_details'
            st.rerun()
    
    # Farm details and recommendations step
    elif st.session_state.step == 'farm_details':
        lang = st.session_state.selected_language
        t = translations[lang]
        
        st.title(t['title'])
        st.markdown(f"**{t['subtitle']}**")
        
        # Create two columns for layout
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📋 " + t['farm_summary'])
            
            # Land size input
            land_size = st.number_input(
                t['land_size'],
                min_value=0.1,
                max_value=1000.0,
                value=1.0,
                step=0.1,
                help=t['land_size_help']
            )
            
            # Soil type selection with multilingual options
            if lang == 'Hindi':
                soil_options = [
                    "Clay / चिकनी मिट्टी", "Sandy / रेतीली मिट्टी", "Loamy / दोमट मिट्टी", 
                    "Silty / गाद मिट्टी", "Peaty / पीट मिट्टी", "Chalky / चूना मिट्टी"
                ]
            elif lang == 'Tamil':
                soil_options = [
                    "Clay / களி மண்", "Sandy / மணல் மண்", "Loamy / வண்டல் மண்", 
                    "Silty / கனிம மண்", "Peaty / கரி மண்", "Chalky / சுண்ணாம்பு மண்"
                ]
            elif lang == 'Telugu':
                soil_options = [
                    "Clay / బంకమట్టి", "Sandy / ఇసుక మట్టి", "Loamy / లోమి మట్టి", 
                    "Silty / సిల్టీ మట్టి", "Peaty / పీట్ మట్టి", "Chalky / సుణ్ణం మట్టి"
                ]
            else:
                soil_options = [
                    "Clay", "Sandy", "Loamy", "Silty", "Peaty", "Chalky"
                ]
            
            soil_selection = st.selectbox(
                t['soil_type'],
                soil_options,
                help=t['soil_help']
            )
            
            # Extract English soil type for processing
            soil_type = soil_selection.split(' / ')[0] if ' / ' in soil_selection else soil_selection
            
            # Season selection with multilingual options
            if lang == 'Hindi':
                season_options = [
                    "Spring / वसंत", "Summer / गर्मी", "Fall / शरद", "Winter / सर्दी"
                ]
            elif lang == 'Tamil':
                season_options = [
                    "Spring / வசந்த காலம்", "Summer / கோடை காலம்", "Fall / இலையுதிர் காலம்", "Winter / குளிர் காலம்"
                ]
            elif lang == 'Telugu':
                season_options = [
                    "Spring / వసంత ఋతువు", "Summer / వేసవి ఋతువు", "Fall / శరదృతువు", "Winter / శీతాకాలం"
                ]
            else:
                season_options = [
                    "Spring", "Summer", "Fall", "Winter"
                ]
            
            season_selection = st.selectbox(
                t['season'],
                season_options,
                help=t['season_help']
            )
            
            # Extract English season for processing
            season = season_selection.split(' / ')[0] if ' / ' in season_selection else season_selection
            
            # Budget input with currency context
            budget_label = t['budget']
            if lang in ['Hindi', 'Tamil', 'Telugu']:
                budget_label += " (₹)"
            else:
                budget_label += " ($)"
                
            budget = st.number_input(
                budget_label,
                min_value=50,
                max_value=100000,
                value=5000 if lang in ['Hindi', 'Tamil', 'Telugu'] else 500,
                step=50,
                help=t['budget_help']
            )
            
            # Get recommendations button
            if st.button(f"🌱 {t['get_recommendations']}", type="primary"):
                engine = load_recommendation_engine()
                recommendations = engine.get_recommendations(
                    land_size=land_size,
                    soil_type=soil_type,
                    season=season,
                    budget=budget
                )
                
                # Store recommendations in session state
                st.session_state.recommendations = recommendations
                st.session_state.farm_details = {
                    'land_size': land_size,
                    'soil_type': soil_type,
                    'season': season,
                    'budget': budget
                }
        
        with col2:
            st.subheader("🎯 " + t['recommendations_title'])
            
            # Display recommendations if available
            if hasattr(st.session_state, 'recommendations') and st.session_state.recommendations:
                recommendations = st.session_state.recommendations
                farm_details = st.session_state.farm_details
                
                # Summary box
                currency_symbol = "₹" if lang in ['Hindi', 'Tamil', 'Telugu'] else "$"
                st.info(f"**{t['farm_summary']}:** {farm_details['land_size']} {t['acres']} • {farm_details['soil_type']} {t['soil']} • {farm_details['season']} {t['planting']} • {currency_symbol}{farm_details['budget']} {t['budget_text']}")
                
                if recommendations['suitable_crops']:
                    st.success(f"Found {len(recommendations['suitable_crops'])} suitable crops for your farm!")
                    
                    # Display each recommended crop
                    for i, crop in enumerate(recommendations['suitable_crops'], 1):
                        with st.expander(f"#{i} {crop['name']} - {crop['category']}", expanded=i<=2):
                            
                            # Crop details in columns
                            detail_col1, detail_col2 = st.columns(2)
                            
                            with detail_col1:
                                st.write(f"**💰 {t['economics']}:**")
                                st.write(f"• {t['cost_per_acre']}: {currency_symbol}{crop['cost_per_acre']}")
                                st.write(f"• {t['expected_yield']}: {crop['yield_per_acre']}")
                                st.write(f"• {t['profit_potential']}: {currency_symbol}{crop['profit_potential']}")
                                
                            with detail_col2:
                                st.write(f"**🌱 {t['growing_info']}:**")
                                st.write(f"• {t['growing_time']}: {crop['growing_time']}")
                                st.write(f"• {t['difficulty']}: {crop['difficulty']}")
                                st.write(f"• {t['water_needs']}: {crop['water_needs']}")
                            
                            # Why this crop section
                            st.write(f"**🤔 {t['why_crop']}**")
                            st.write(crop['recommendation_reason'])
                            
                            # Growing tips
                            if crop['growing_tips']:
                                st.write(f"**💡 {t['growing_tips']}:**")
                                for tip in crop['growing_tips']:
                                    st.write(f"• {tip}")
                    
                    # Budget breakdown
                    st.subheader(f"💵 {t['budget_breakdown']}")
                    total_cost = sum(crop['cost_per_acre'] for crop in recommendations['suitable_crops'][:3])
                    st.write(f"**{t['total_cost']}:** {currency_symbol}{total_cost:.2f}")
                    st.write(f"**{t['your_budget']}:** {currency_symbol}{farm_details['budget']}")
                    
                    if total_cost <= farm_details['budget']:
                        st.success(f"✅ {t['can_afford']}")
                    else:
                        st.warning(f"⚠️ {t['budget_warning']}")
                        
                else:
                    st.warning(t['no_crops'])
                    
                # Additional tips
                st.subheader(f"🌟 {t['general_tips']}")
                for tip in recommendations['general_tips']:
                    st.write(f"• {tip}")
                    
            else:
                st.info(f"👈 {t['get_started']}")
                
                # Show some general information while waiting
                st.markdown(f"### 🌾 {t['about_tool']}")
                st.write(t['tool_description'])
        
        # Language change button
        if st.button("🌍 Change Language / भाषा बदलें / மொழியை மாற்று / భాష మార్చు"):
            st.session_state.step = 'language_selection'
            st.rerun()

if __name__ == "__main__":
    main()
```
## crop_database.py
```
"""
Crop database containing information about different crops,
their requirements, costs, and growing characteristics.
"""

def get_crop_database():
    """
    Returns a comprehensive database of crops with their characteristics.
    Each crop includes soil preferences, seasonal information, costs, and growing tips.
    """
    
    crops = {
        # Popular Indian crops with realistic INR pricing
        "rice": {
            "name": "Rice",
            "category": "Grains",
            "soil_preferences": ["Clay", "Loamy", "Silty"],
            "seasons": ["Summer"],
            "cost_per_acre": 2000,
            "yield_per_acre": "40-50 quintal",
            "growing_time": "120-150 days",
            "difficulty": "Medium",
            "water_needs": "High",
            "profit_potential": 15000,
            "growing_tips": [
                "Need flooded fields for growing",
                "Plant during monsoon season",
                "Use good quality seeds",
                "Control weeds regularly"
            ]
        },
        
        "sugarcane": {
            "name": "Sugarcane",
            "category": "Cash Crops",
            "soil_preferences": ["Loamy", "Clay", "Sandy"],
            "seasons": ["Spring", "Summer"],
            "cost_per_acre": 3000,
            "yield_per_acre": "80-100 tons",
            "growing_time": "365 days",
            "difficulty": "Medium",
            "water_needs": "High",
            "profit_potential": 25000,
            "growing_tips": [
                "Long growing season crop",
                "Need plenty of water",
                "Plant in rows with good spacing",
                "Harvest after 12 months"
            ]
        },
        
        "turmeric": {
            "name": "Turmeric",
            "category": "Spices",
            "soil_preferences": ["Loamy", "Sandy", "Clay"],
            "seasons": ["Spring", "Summer"],
            "cost_per_acre": 3500,
            "yield_per_acre": "20-25 quintal",
            "growing_time": "270-300 days",
            "difficulty": "Medium",
            "water_needs": "High",
            "profit_potential": 30000,
            "growing_tips": [
                "Plant rhizomes in good soil",
                "Need regular watering",
                "Harvest after 9-10 months",
                "Dry and grind for spice"
            ]
        },
        
        "onion": {
            "name": "Onion",
            "category": "Vegetables",
            "soil_preferences": ["Loamy", "Sandy", "Silty"],
            "seasons": ["Spring", "Fall"],
            "cost_per_acre": 2500,
            "yield_per_acre": "15-20 tons",
            "growing_time": "120-150 days",
            "difficulty": "Medium",
            "water_needs": "Moderate",
            "profit_potential": 18000,
            "growing_tips": [
                "Plant small bulbs in rows",
                "Keep soil moist but not wet",
                "Harvest when green tops fall over",
                "Dry well before storing"
            ]
        },
        
        "cotton": {
            "name": "Cotton",
            "category": "Cash Crops",
            "soil_preferences": ["Sandy", "Loamy", "Clay"],
            "seasons": ["Spring", "Summer"],
            "cost_per_acre": 4000,
            "yield_per_acre": "8-12 quintal",
            "growing_time": "180-200 days",
            "difficulty": "Medium",
            "water_needs": "Moderate",
            "profit_potential": 20000,
            "growing_tips": [
                "Plant after soil warms up",
                "Control pests regularly",
                "Pick cotton when bolls open",
                "Store in dry place"
            ]
        },
        
        "mustard": {
            "name": "Mustard",
            "category": "Oilseeds",
            "soil_preferences": ["Loamy", "Sandy", "Clay"],
            "seasons": ["Fall", "Winter"],
            "cost_per_acre": 800,
            "yield_per_acre": "8-12 quintal",
            "growing_time": "90-120 days",
            "difficulty": "Easy",
            "water_needs": "Low",
            "profit_potential": 8000,
            "growing_tips": [
                "Plant in cool weather",
                "Broadcast seeds evenly",
                "Harvest when pods turn brown",
                "Good crop for winter season"
            ]
        },
        
        # Additional crops for variety
        "tomatoes": {
            "name": "Tomatoes",
            "category": "Vegetables",
            "soil_preferences": ["Loamy", "Sandy", "Silty"],
            "seasons": ["Spring", "Summer"],
            "cost_per_acre": 1500,
            "yield_per_acre": "25-35 tons",
            "growing_time": "75-85 days",
            "difficulty": "Medium",
            "water_needs": "Moderate",
            "profit_potential": 12000,
            "growing_tips": [
                "Plant after winter season ends",
                "Support tall plants with sticks",
                "Water regularly but don't flood",
                "Cover soil around plants"
            ]
        },
        
        "corn": {
            "name": "Corn",
            "category": "Grains",
            "soil_preferences": ["Loamy", "Silty", "Clay"],
            "seasons": ["Spring", "Summer"],
            "cost_per_acre": 200,
            "yield_per_acre": "150-200 bushels",
            "growing_time": "90-120 days",
            "difficulty": "Medium",
            "water_needs": "High",
            "profit_potential": 1000,
            "growing_tips": [
                "Plant when soil temperature reaches 60°F",
                "Needs plenty of space between rows",
                "Side-dress with nitrogen mid-season",
                "Hand-pollinate if needed for small plots"
            ]
        },
        
        "beans": {
            "name": "Beans",
            "category": "Legumes",
            "soil_preferences": ["Loamy", "Sandy", "Silty"],
            "seasons": ["Spring", "Summer"],
            "cost_per_acre": 90,
            "yield_per_acre": "1-2 tons",
            "growing_time": "50-70 days",
            "difficulty": "Easy",
            "water_needs": "Moderate",
            "profit_potential": 500,
            "growing_tips": [
                "Don't plant until soil warms up",
                "Fixes nitrogen in soil naturally",
                "Don't overwater to prevent root rot",
                "Pick regularly to encourage production"
            ]
        },
        
        "potatoes": {
            "name": "Potatoes",
            "category": "Root Vegetables",
            "soil_preferences": ["Sandy", "Loamy"],
            "seasons": ["Spring", "Summer"],
            "cost_per_acre": 250,
            "yield_per_acre": "300-400 cwt",
            "growing_time": "80-100 days",
            "difficulty": "Medium",
            "water_needs": "Moderate",
            "profit_potential": 1500,
            "growing_tips": [
                "Plant seed potatoes, not grocery store ones",
                "Hill soil around plants as they grow",
                "Harvest when foliage starts to die back",
                "Cure in cool, dark place before storage"
            ]
        }
    }
    
    return crops
```
