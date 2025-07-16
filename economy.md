```

"""
Economic advisor module for providing financial analysis, market information,
and government scheme recommendations for crop cultivation.
"""

import streamlit as st

class EconomicAdvisor:
    def __init__(self):
        self.government_schemes = self._load_government_schemes()
        self.market_data = self._load_market_data()
        
    def _load_government_schemes(self):
        """Load government schemes and subsidies data for different crops and states."""
        return {
            'Tamil Nadu': {
                'rice': [
                    "Tamil Nadu Paddy Procurement Scheme",
                    "Direct Benefit Transfer for Rice Farmers",
                    "Crop Insurance under PMFBY"
                ],
                'sugarcane': [
                    "Sugarcane Development Scheme",
                    "Fair and Remunerative Price (FRP) for Sugarcane",
                    "Interest Subvention Scheme"
                ],
                'turmeric': [
                    "Spice Development Scheme",
                    "Export Promotion Scheme for Spices",
                    "Rural Development Loans"
                ],
                'cotton': [
                    "Cotton Development Program",
                    "Minimum Support Price (MSP) for Cotton",
                    "Technology Mission on Cotton"
                ],
                'general': [
                    "Pradhan Mantri Fasal Bima Yojana (PMFBY)",
                    "Kisan Credit Card Scheme",
                    "PM-KISAN Direct Benefit Transfer"
                ]
            },
            'Karnataka': {
                'rice': [
                    "Karnataka Raitha Sampada Scheme",
                    "Crop Insurance Scheme",
                    "Bhoochetana Scheme"
                ],
                'sugarcane': [
                    "Sugarcane Development Program",
                    "Fair and Remunerative Price Support",
                    "Drip Irrigation Subsidy"
                ],
                'turmeric': [
                    "Spice Development Scheme",
                    "Karnataka Spice Board Support",
                    "Organic Farming Promotion"
                ],
                'general': [
                    "Raitha Sampada Scheme",
                    "Kisan Credit Card",
                    "Zero Interest Loans for Farmers"
                ]
            },
            'Andhra Pradesh': {
                'rice': [
                    "YSR Rythu Bharosa Scheme",
                    "Paddy Procurement at MSP",
                    "Free Crop Insurance"
                ],
                'sugarcane': [
                    "Sugarcane Development Scheme",
                    "Fair Price Support",
                    "Drip Irrigation Subsidy"
                ],
                'turmeric': [
                    "Spice Development Program",
                    "Export Promotion Scheme",
                    "Cold Storage Subsidy"
                ],
                'general': [
                    "YSR Rythu Bharosa",
                    "Interest-Free Loans",
                    "Input Subsidy Scheme"
                ]
            },
            'Telangana': {
                'rice': [
                    "Rythu Bandhu Scheme",
                    "Paddy Procurement Support",
                    "Free Electricity for Agriculture"
                ],
                'cotton': [
                    "Cotton Development Program",
                    "Minimum Support Price",
                    "Seed Subsidy Scheme"
                ],
                'turmeric': [
                    "Spice Development Scheme",
                    "Market Development Support",
                    "Processing Unit Subsidy"
                ],
                'general': [
                    "Rythu Bandhu Investment Support",
                    "Rythu Bima Life Insurance",
                    "KCC Interest Subvention"
                ]
            }
        }
    
    def _load_market_data(self):
        """Load market and export destination data for different crops."""
        return {
            'rice': {
                'local_markets': ['Thanjavur', 'Coimbatore', 'Madurai', 'Chennai'],
                'export_destinations': ['Middle East', 'Africa', 'Europe', 'USA'],
                'processing_centers': ['Rice Mills', 'Parboiling Units', 'Modern Rice Parks']
            },
            'sugarcane': {
                'local_markets': ['Sugar Mills', 'Jaggery Units', 'Cooperative Societies'],
                'export_destinations': ['Middle East', 'Africa', 'Bangladesh'],
                'processing_centers': ['Sugar Factories', 'Ethanol Plants', 'Jaggery Production']
            },
            'turmeric': {
                'local_markets': ['Erode', 'Coimbatore', 'Salem', 'Madurai'],
                'export_destinations': ['USA', 'UK', 'UAE', 'Germany', 'Japan'],
                'processing_centers': ['Turmeric Processing Units', 'Spice Parks', 'Export Houses']
            },
            'cotton': {
                'local_markets': ['Cotton Markets', 'Ginning Mills', 'Textile Mills'],
                'export_destinations': ['China', 'Bangladesh', 'Vietnam', 'Turkey'],
                'processing_centers': ['Cotton Ginning', 'Spinning Mills', 'Textile Units']
            },
            'onion': {
                'local_markets': ['Nashik', 'Bangalore', 'Chennai', 'Hyderabad'],
                'export_destinations': ['Middle East', 'Malaysia', 'Singapore', 'Sri Lanka'],
                'processing_centers': ['Cold Storage', 'Dehydration Units', 'Processing Centers']
            },
            'tomato': {
                'local_markets': ['Bangalore', 'Chennai', 'Hyderabad', 'Kochi'],
                'export_destinations': ['Middle East', 'Maldives', 'Sri Lanka'],
                'processing_centers': ['Food Processing Units', 'Tomato Paste Plants', 'Canning Industry']
            }
        }
    
    def calculate_profit_loss(self, crop_name, budget, expected_turnover, location, language='English'):
        """Calculate profit/loss and provide financial analysis."""
        
        # Basic calculation
        profit_loss = expected_turnover - budget
        profit_percentage = (profit_loss / budget) * 100 if budget > 0 else 0
        
        # Get crop-specific costs and recommendations
        cost_breakdown = self._get_cost_breakdown(crop_name, budget)
        
        # Get market recommendations
        market_info = self._get_market_recommendations(crop_name, location, language)
        
        # Get government schemes
        schemes = self._get_government_schemes(crop_name, location, language)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(crop_name, profit_percentage, language)
        
        return {
            'profit_loss': profit_loss,
            'profit_percentage': profit_percentage,
            'cost_breakdown': cost_breakdown,
            'market_info': market_info,
            'government_schemes': schemes,
            'recommendations': recommendations
        }
    
    def _get_cost_breakdown(self, crop_name, budget):
        """Get typical cost breakdown for a crop."""
        # Typical cost distribution for Indian agriculture
        return {
            'seeds': budget * 0.15,  # 15% for seeds
            'fertilizers': budget * 0.25,  # 25% for fertilizers
            'irrigation': budget * 0.20,  # 20% for irrigation
            'labor': budget * 0.30,  # 30% for labor
            'miscellaneous': budget * 0.10  # 10% for other costs
        }
    
    def _get_market_recommendations(self, crop_name, location, language):
        """Get market recommendations for the crop."""
        
        crop_lower = crop_name.lower()
        market_data = self.market_data.get(crop_lower, {
            'local_markets': ['Local Agricultural Markets'],
            'export_destinations': ['Regional Export Markets'],
            'processing_centers': ['Local Processing Units']
        })
        
        translations = {
            'English': {
                'local_markets': 'Local Markets',
                'export_destinations': 'Export Opportunities',
                'processing_centers': 'Processing Centers'
            },
            'Hindi': {
                'local_markets': 'स्थानीय बाजार',
                'export_destinations': 'निर्यात अवसर',
                'processing_centers': 'प्रसंस्करण केंद्र'
            },
            'Tamil': {
                'local_markets': 'உள்ளூர் சந்தைகள்',
                'export_destinations': 'ஏற்றுமதி வாய்ப்புகள்',
                'processing_centers': 'செயலாக்க மையங்கள்'
            },
            'Telugu': {
                'local_markets': 'స్థానిక మార్కెట్లు',
                'export_destinations': 'ఎగుమతి అవకాశాలు',
                'processing_centers': 'ప్రాసెసింగ్ కేంద్రాలు'
            }
        }
        
        t = translations.get(language, translations['English'])
        
        return {
            'local_markets': {
                'title': t['local_markets'],
                'options': market_data['local_markets']
            },
            'export_destinations': {
                'title': t['export_destinations'],
                'options': market_data['export_destinations']
            },
            'processing_centers': {
                'title': t['processing_centers'],
                'options': market_data['processing_centers']
            }
        }
    
    def _get_government_schemes(self, crop_name, location, language):
        """Get government schemes for the crop and location."""
        
        # Extract state from location (simple approach)
        state = self._extract_state(location)
        
        crop_lower = crop_name.lower()
        state_schemes = self.government_schemes.get(state, self.government_schemes.get('Tamil Nadu', {}))
        
        # Get crop-specific schemes
        crop_schemes = state_schemes.get(crop_lower, [])
        general_schemes = state_schemes.get('general', [])
        
        return {
            'crop_specific': crop_schemes,
            'general': general_schemes
        }
    
    def _extract_state(self, location):
        """Extract state from location string."""
        location_lower = location.lower()
        
        if 'tamil nadu' in location_lower or 'erode' in location_lower or 'coimbatore' in location_lower:
            return 'Tamil Nadu'
        elif 'karnataka' in location_lower or 'bangalore' in location_lower or 'mysore' in location_lower:
            return 'Karnataka'
        elif 'andhra pradesh' in location_lower or 'vijayawada' in location_lower:
            return 'Andhra Pradesh'
        elif 'telangana' in location_lower or 'hyderabad' in location_lower:
            return 'Telangana'
        else:
            return 'Tamil Nadu'  # Default
    
    def _generate_recommendations(self, crop_name, profit_percentage, language):
        """Generate profit maximization recommendations."""
        
        recommendations = {
            'English': {
                'high_profit': [
                    "Excellent choice! Focus on quality seeds and proper timing",
                    "Consider value-added processing for higher profits",
                    "Explore export opportunities for premium prices"
                ],
                'medium_profit': [
                    "Good profit potential. Optimize input costs",
                    "Consider organic farming for premium pricing",
                    "Look for government subsidies to reduce costs"
                ],
                'low_profit': [
                    "Profit margins are tight. Consider cost reduction strategies",
                    "Look into contract farming for assured prices",
                    "Explore alternative crops with better returns"
                ],
                'loss': [
                    "Current plan may result in losses. Reconsider crop choice",
                    "Look for high-value crops suitable for your region",
                    "Consider consulting agricultural extension officers"
                ]
            },
            'Hindi': {
                'high_profit': [
                    "बहुत अच्छा विकल्प! अच्छे बीज और सही समय पर ध्यान दें",
                    "अधिक मुनाफे के लिए मूल्य संवर्धन पर विचार करें",
                    "प्रीमियम कीमतों के लिए निर्यात अवसरों का पता लगाएं"
                ],
                'medium_profit': [
                    "अच्छी लाभ संभावना। इनपुट लागत को अनुकूलित करें",
                    "प्रीमियम मूल्य के लिए जैविक खेती पर विचार करें",
                    "लागत कम करने के लिए सरकारी सब्सिडी देखें"
                ],
                'low_profit': [
                    "लाभ मार्जिन कम है। लागत कम करने की रणनीति पर विचार करें",
                    "निश्चित कीमतों के लिए कॉन्ट्रैक्ट फार्मिंग देखें",
                    "बेहतर रिटर्न वाली वैकल्पिक फसलों का पता लगाएं"
                ],
                'loss': [
                    "वर्तमान योजना में नुकसान हो सकता है। फसल चुनाव पर पुनर्विचार करें",
                    "अपने क्षेत्र के लिए उच्च मूल्य वाली फसलों की तलाश करें",
                    "कृषि विस्तार अधिकारियों से सलाह लें"
                ]
            },
            'Tamil': {
                'high_profit': [
                    "சிறந்த தேர்வு! தரமான விதைகள் மற்றும் சரியான நேரத்தில் கவனம் செலுத்துங்கள்",
                    "அதிக லாபத்திற்காக மதிப்பு கூட்டப்பட்ட செயலாக்கத்தை கருத்தில் கொள்ளுங்கள்",
                    "பிரீமியம் விலைகளுக்காக ஏற்றுமதி வாய்ப்புகளை ஆராயுங்கள்"
                ],
                'medium_profit': [
                    "நல்ல லாப சாத்தியம். உள்ளீட்டு செலவுகளை மேம்படுத்துங்கள்",
                    "பிரீமியம் விலைக்காக இயற்கை விவசாயத்தை கருத்தில் கொள்ளுங்கள்",
                    "செலவுகளை குறைக்க அரசு மானியங்களை பாருங்கள்"
                ],
                'low_profit': [
                    "லாப வரம்புகள் குறைவாக உள்ளன. செலவு குறைப்பு உத்திகளை கருத்தில் கொள்ளுங்கள்",
                    "உறுதியான விலைகளுக்காக ஒப்பந்த விவசாயத்தை பாருங்கள்",
                    "சிறந்த வருமானம் கொண்ட மாற்று பயிர்களை ஆராயுங்கள்"
                ],
                'loss': [
                    "தற்போதைய திட்டம் இழப்பை ஏற்படுத்தலாம். பயிர் தேர்வை மறுபரிசீலனை செய்யுங்கள்",
                    "உங்கள் பகுதிக்கு ஏற்ற அதிக மதிப்பு பயிர்களை தேடுங்கள்",
                    "விவசாய விரிவாக்க அதிகாரிகளிடம் ஆலோசனை பெறுங்கள்"
                ]
            },
            'Telugu': {
                'high_profit': [
                    "అద్భుతమైన ఎంపిక! నాణ్యమైన విత్తనాలు మరియు సరైన సమయంపై దృష్టి పెట్టండి",
                    "అధిక లాభాల కోసం విలువ జోడించిన ప్రాసెసింగ్‌ను పరిగణించండి",
                    "ప్రీమియం ధరలకు ఎగుమతి అవకాశాలను అన్వేషించండి"
                ],
                'medium_profit': [
                    "మంచి లాభ సంభావ్యత. ఇన్‌పుట్ వ్యయాలను ఆప్టిమైజ్ చేయండి",
                    "ప్రీమియం ధరల కోసం సేంద్రీయ వ్యవసాయాన్ని పరిగణించండి",
                    "వ్యయాలను తగ్గించడానికి ప్రభుత్వ సబ్సిడీలను చూడండి"
                ],
                'low_profit': [
                    "లాభ మార్జిన్లు తక్కువగా ఉన్నాయి. వ్యయ తగ్గింపు వ్యూహాలను పరిగణించండి",
                    "నిర్ధారిత ధరల కోసం కాంట్రాక్ట్ వ్యవసాయాన్ని చూడండి",
                    "మెరుగైన రిటర్న్లతో ప్రత్యామ్నాయ పంటలను అన్వేషించండి"
                ],
                'loss': [
                    "ప్రస్తుత ప్రణాళిక నష్టాలకు దారితీయవచ్చు. పంట ఎంపికను పునఃపరిశీలించండి",
                    "మీ ప్రాంతానికి అనుకూలమైన అధిక విలువ పంటలను వెతకండి",
                    "వ్యవసాయ విస్తరణ అధికారులను సంప్రదించండి"
                ]
            }
        }
        
        # Determine recommendation category based on profit percentage
        if profit_percentage >= 50:
            category = 'high_profit'
        elif profit_percentage >= 20:
            category = 'medium_profit'
        elif profit_percentage >= 0:
            category = 'low_profit'
        else:
            category = 'loss'
        
        return recommendations.get(language, recommendations['English']).get(category, [])
    
    def get_alternative_crops(self, current_crop, location, language='English'):
        """Suggest alternative crops with better profit potential."""
        
        alternatives = {
            'English': {
                'high_value': ['Saffron', 'Vanilla', 'Cardamom', 'Organic Vegetables'],
                'medium_value': ['Ginger', 'Turmeric', 'Chili', 'Coriander'],
                'safe_options': ['Onion', 'Tomato', 'Brinjal', 'Okra']
            },
            'Hindi': {
                'high_value': ['केसर', 'वनीला', 'इलायची', 'जैविक सब्जियां'],
                'medium_value': ['अदरक', 'हल्दी', 'मिर्च', 'धनिया'],
                'safe_options': ['प्याज', 'टमाटर', 'बैंगन', 'भिंडी']
            },
            'Tamil': {
                'high_value': ['குங்குமப்பூ', 'வெனிலா', 'ஏலக்காய்', 'இயற்கை காய்கறிகள்'],
                'medium_value': ['இஞ்சி', 'மஞ்சள்', 'மிளகாய்', 'கொத்தமல்லி'],
                'safe_options': ['வெங்காயம்', 'தக்காளி', 'கத்தரிக்காய்', 'வெண்டைக்காய்']
            },
            'Telugu': {
                'high_value': ['కుంకుమపువ్వు', 'వనిల్లా', 'ఏలకులు', 'సేంద్రీయ కూరగాయలు'],
                'medium_value': ['అల్లం', 'పసుపు', 'మిర్చి', 'కొత్తిమీర'],
                'safe_options': ['ఉల్లిపాయ', 'టమాటా', 'వంకాయ', 'భిండి']
            }
        }
     ```   
        return alternatives.get(language, alternatives['English'])
