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
        # Vegetables
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
        
        "lettuce": {
            "name": "Lettuce",
            "category": "Leafy Greens",
            "soil_preferences": ["Loamy", "Silty", "Sandy"],
            "seasons": ["Spring", "Fall"],
            "cost_per_acre": 1000,
            "yield_per_acre": "15-20 tons",
            "growing_time": "45-65 days",
            "difficulty": "Easy",
            "water_needs": "High",
            "profit_potential": 8000,
            "growing_tips": [
                "Plant in cool weather for best results",
                "Harvest in early morning for crispness",
                "Succession plant every 2 weeks",
                "Provide shade in hot weather"
            ]
        },
        
        "carrots": {
            "name": "Carrots",
            "category": "Root Vegetables",
            "soil_preferences": ["Sandy", "Loamy"],
            "seasons": ["Spring", "Fall"],
            "cost_per_acre": 120,
            "yield_per_acre": "20-25 tons",
            "growing_time": "70-80 days",
            "difficulty": "Easy",
            "water_needs": "Moderate",
            "profit_potential": 900,
            "growing_tips": [
                "Need loose, deep soil for straight roots",
                "Thin seedlings to prevent overcrowding",
                "Keep soil moist but not waterlogged",
                "Harvest before ground freezes"
            ]
        },
        
        "spinach": {
            "name": "Spinach",
            "category": "Leafy Greens",
            "soil_preferences": ["Loamy", "Silty", "Clay"],
            "seasons": ["Spring", "Fall", "Winter"],
            "cost_per_acre": 80,
            "yield_per_acre": "8-12 tons",
            "growing_time": "40-50 days",
            "difficulty": "Easy",
            "water_needs": "Moderate",
            "profit_potential": 600,
            "growing_tips": [
                "Cold tolerant, can survive light frosts",
                "Harvest outer leaves first",
                "Plant in partial shade in summer",
                "Quick growing, good for succession planting"
            ]
        },
        
        # Grains
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
        
        "wheat": {
            "name": "Wheat",
            "category": "Grains",
            "soil_preferences": ["Loamy", "Clay", "Silty"],
            "seasons": ["Fall", "Spring"],
            "cost_per_acre": 180,
            "yield_per_acre": "40-60 bushels",
            "growing_time": "120-150 days",
            "difficulty": "Medium",
            "water_needs": "Moderate",
            "profit_potential": 700,
            "growing_tips": [
                "Winter wheat planted in fall, spring wheat in spring",
                "Requires minimal cultivation once established",
                "Harvest when grain moisture is 13-14%",
                "Good rotation crop with legumes"
            ]
        },
        
        # Legumes
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
        
        "peas": {
            "name": "Peas",
            "category": "Legumes",
            "soil_preferences": ["Loamy", "Clay", "Silty"],
            "seasons": ["Spring", "Fall"],
            "cost_per_acre": 85,
            "yield_per_acre": "2-3 tons",
            "growing_time": "60-70 days",
            "difficulty": "Easy",
            "water_needs": "Moderate",
            "profit_potential": 600,
            "growing_tips": [
                "Plant early in cool weather",
                "Provide support for climbing varieties",
                "Harvest pods when plump but tender",
                "Improves soil nitrogen for next crop"
            ]
        },
        
        # Fruits
        "strawberries": {
            "name": "Strawberries",
            "category": "Fruits",
            "soil_preferences": ["Sandy", "Loamy"],
            "seasons": ["Spring"],
            "cost_per_acre": 300,
            "yield_per_acre": "10-15 tons",
            "growing_time": "90-120 days",
            "difficulty": "Medium",
            "water_needs": "High",
            "profit_potential": 2000,
            "growing_tips": [
                "Plant in raised beds for drainage",
                "Mulch heavily to suppress weeds",
                "Remove runners for larger berries",
                "Protect from birds with netting"
            ]
        },
        
        # Root crops
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
        },
        
        "sweet_potatoes": {
            "name": "Sweet Potatoes",
            "category": "Root Vegetables",
            "soil_preferences": ["Sandy", "Loamy"],
            "seasons": ["Spring", "Summer"],
            "cost_per_acre": 200,
            "yield_per_acre": "200-300 cwt",
            "growing_time": "90-120 days",
            "difficulty": "Medium",
            "water_needs": "Moderate",
            "profit_potential": 1200,
            "growing_tips": [
                "Need warm soil and long growing season",
                "Plant slips (rooted cuttings) not seeds",
                "Harvest before first frost",
                "Cure in warm, humid conditions"
            ]
        },
        
        # Herbs
        "basil": {
            "name": "Basil",
            "category": "Herbs",
            "soil_preferences": ["Loamy", "Sandy", "Silty"],
            "seasons": ["Spring", "Summer"],
            "cost_per_acre": 120,
            "yield_per_acre": "2-3 tons",
            "growing_time": "60-90 days",
            "difficulty": "Easy",
            "water_needs": "Moderate",
            "profit_potential": 1800,
            "growing_tips": [
                "Pinch flowers to keep leaves tender",
                "Harvest regularly for continuous growth",
                "Protect from cold temperatures",
                "High value crop for direct sales"
            ]
        },
        
        # Brassicas
        "cabbage": {
            "name": "Cabbage",
            "category": "Brassicas",
            "soil_preferences": ["Loamy", "Clay", "Silty"],
            "seasons": ["Spring", "Fall"],
            "cost_per_acre": 140,
            "yield_per_acre": "30-40 tons",
            "growing_time": "70-100 days",
            "difficulty": "Medium",
            "water_needs": "High",
            "profit_potential": 1000,
            "growing_tips": [
                "Start with transplants for best results",
                "Keep soil consistently moist",
                "Harvest before heads split",
                "Good storage crop for winter sales"
            ]
        },
        
        "broccoli": {
            "name": "Broccoli",
            "category": "Brassicas",
            "soil_preferences": ["Loamy", "Silty", "Clay"],
            "seasons": ["Spring", "Fall"],
            "cost_per_acre": 1600,
            "yield_per_acre": "8-12 tons",
            "growing_time": "60-80 days",
            "difficulty": "Medium",
            "water_needs": "High",
            "profit_potential": 14000,
            "growing_tips": [
                "Prefers cool weather for best heads",
                "Harvest main head before flowers open",
                "Side shoots will continue producing",
                "Protect from cabbage worms"
            ]
        },
        
        # Popular Indian crops
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
        }
    }
    
    return crops
