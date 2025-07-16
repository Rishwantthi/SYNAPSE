"""
Crop recommendation engine that analyzes user inputs and provides
personalized crop suggestions based on soil type, season, budget, and land size.
"""

import random
from crop_database import get_crop_database

class CropRecommendationEngine:
    def __init__(self):
        self.crop_db = get_crop_database()
        
    def get_recommendations(self, land_size, soil_type, season, budget):
        """
        Generate crop recommendations based on user inputs.
        
        Args:
            land_size (float): Available land in acres
            soil_type (str): Type of soil
            season (str): Planting season
            budget (float): Available budget in dollars
            
        Returns:
            dict: Recommendations with suitable crops and general tips
        """
        
        # Filter crops based on soil type and season
        suitable_crops = []
        
        for crop_id, crop_data in self.crop_db.items():
            # Check if crop is suitable for the soil type and season
            if (soil_type in crop_data['soil_preferences'] and 
                season in crop_data['seasons']):
                
                # Calculate if crop fits in budget
                total_cost = crop_data['cost_per_acre'] * land_size
                
                if total_cost <= budget:
                    # Create enhanced crop info with recommendation reasoning
                    enhanced_crop = crop_data.copy()
                    enhanced_crop['total_cost'] = total_cost
                    enhanced_crop['recommendation_reason'] = self._generate_reason(
                        crop_data, soil_type, season, land_size, budget
                    )
                    
                    # Calculate profit potential for this land size
                    enhanced_crop['total_profit_potential'] = (
                        enhanced_crop['profit_potential'] * land_size
                    )
                    
                    suitable_crops.append(enhanced_crop)
        
        # Sort crops by profit potential and suitability
        suitable_crops.sort(key=lambda x: (
            x['total_profit_potential'], 
            -x['cost_per_acre'],
            self._get_difficulty_score(x['difficulty'])
        ), reverse=True)
        
        # Limit to top 5 recommendations
        suitable_crops = suitable_crops[:5]
        
        # Generate general tips
        general_tips = self._generate_general_tips(soil_type, season, land_size, budget)
        
        return {
            'suitable_crops': suitable_crops,
            'general_tips': general_tips,
            'total_recommendations': len(suitable_crops)
        }
    
    def _generate_reason(self, crop_data, soil_type, season, land_size, budget):
        """Generate explanation for why this crop is recommended."""
        
        reasons = []
        
        # Soil compatibility
        if soil_type in crop_data['soil_preferences']:
            if soil_type == "Loamy":
                reasons.append(f"Loamy soil is ideal for {crop_data['name'].lower()} - provides perfect drainage and nutrients")
            elif soil_type == "Sandy":
                reasons.append(f"Sandy soil works great for {crop_data['name'].lower()} - offers good drainage and easy root penetration")
            elif soil_type == "Clay":
                reasons.append(f"Clay soil provides excellent water retention for {crop_data['name'].lower()}")
            else:
                reasons.append(f"Your {soil_type.lower()} soil is well-suited for growing {crop_data['name'].lower()}")
        
        # Seasonal appropriateness
        if season in crop_data['seasons']:
            if season == "Spring":
                reasons.append(f"Spring is perfect planting time - gives {crop_data['name'].lower()} the full growing season")
            elif season == "Summer":
                reasons.append(f"Summer planting works well for {crop_data['name'].lower()} - loves warm weather")
            elif season == "Fall":
                reasons.append(f"Fall planting is smart for {crop_data['name'].lower()} - cooler weather improves quality")
            else:
                reasons.append(f"Winter growing is possible for {crop_data['name'].lower()} in protected conditions")
        
        # Economic benefits
        profit_per_acre = crop_data['profit_potential']
        if profit_per_acre > 1000:
            reasons.append(f"High profit potential of ${profit_per_acre} per acre makes this a great money-maker")
        elif profit_per_acre > 500:
            reasons.append(f"Good profit potential of ${profit_per_acre} per acre provides solid returns")
        else:
            reasons.append(f"Reliable income crop with ${profit_per_acre} per acre - good for steady cash flow")
        
        # Difficulty consideration
        if crop_data['difficulty'] == "Easy":
            reasons.append("Easy to grow - perfect for beginners or low-maintenance farming")
        elif crop_data['difficulty'] == "Medium":
            reasons.append("Moderate difficulty - manageable with basic farming knowledge")
        
        # Land size consideration
        if land_size <= 1:
            reasons.append("Works well on small plots - efficient use of limited space")
        elif land_size <= 5:
            reasons.append("Great for medium-sized farms - scalable production")
        else:
            reasons.append("Excellent for large-scale farming - high volume potential")
        
        return " • ".join(reasons[:3])  # Limit to top 3 reasons
    
    def _get_difficulty_score(self, difficulty):
        """Convert difficulty to numeric score for sorting."""
        difficulty_scores = {
            "Easy": 3,
            "Medium": 2,
            "Hard": 1
        }
        return difficulty_scores.get(difficulty, 2)
    
    def _generate_general_tips(self, soil_type, season, land_size, budget):
        """Generate general farming tips based on user inputs."""
        
        tips = []
        
        # Soil-specific tips
        if soil_type == "Clay":
            tips.append("Clay soil: Add organic matter to improve drainage and work when slightly moist, not wet")
        elif soil_type == "Sandy":
            tips.append("Sandy soil: Add compost regularly to improve water retention and nutrient content")
        elif soil_type == "Loamy":
            tips.append("Loamy soil: You have the best soil type! Maintain with regular organic matter additions")
        elif soil_type == "Silty":
            tips.append("Silty soil: Good for most crops but can compact easily - avoid working when wet")
        elif soil_type == "Peaty":
            tips.append("Peaty soil: Excellent for water-loving crops but may need lime to reduce acidity")
        elif soil_type == "Chalky":
            tips.append("Chalky soil: Well-draining but alkaline - choose crops that tolerate higher pH")
        
        # Seasonal tips
        if season == "Spring":
            tips.append("Spring planting: Wait until soil can be worked and last frost has passed")
        elif season == "Summer":
            tips.append("Summer planting: Focus on heat-tolerant crops and ensure adequate water supply")
        elif season == "Fall":
            tips.append("Fall planting: Great for cool-season crops and preparing for next year's garden")
        elif season == "Winter":
            tips.append("Winter growing: Consider cold frames or greenhouse for season extension")
        
        # Budget-based tips
        if budget < 200:
            tips.append("Small budget: Start with easy, low-cost crops like lettuce and herbs for quick returns")
        elif budget < 1000:
            tips.append("Medium budget: Mix of quick-return crops and longer-term investments for steady income")
        else:
            tips.append("Good budget: Consider investing in perennial crops or value-added products")
        
        # Land size tips
        if land_size <= 1:
            tips.append("Small plot: Focus on high-value crops like herbs, salads, and specialty vegetables")
        elif land_size <= 5:
            tips.append("Medium farm: Perfect size for diverse crop rotation and direct-to-consumer sales")
        else:
            tips.append("Large farm: Consider wholesale markets and efficient mechanization for best profits")
        
        # General farming wisdom
        general_wisdom = [
            "Start small and expand gradually - learn as you grow",
            "Keep detailed records of costs, yields, and what works best",
            "Build healthy soil first - it's the foundation of successful farming",
            "Consider crop rotation to maintain soil health and break pest cycles",
            "Connect with local farmers and extension services for regional advice",
            "Plan for water access - irrigation can make or break your harvest",
            "Test your soil pH and nutrients before planting for best results"
        ]
        
        # Add 2-3 random general tips
        tips.extend(random.sample(general_wisdom, min(3, len(general_wisdom))))
        
        return tips[:6]  # Limit to 6 tips total
