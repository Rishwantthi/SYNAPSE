```
"""
Comprehensive database of plant diseases with detailed information about causes, symptoms, and treatments.
"""

def get_disease_database():
    """Returns detailed information about various plant diseases."""
    
    return {
        'Tomato Late Blight': {
            'scientific_name': 'Phytophthora infestans',
            'common_names': ['Late Blight', 'Potato Blight'],
            'affected_plants': ['Tomato', 'Potato', 'Eggplant'],
            'causes': [
                'Cool, moist weather conditions (60-70°F)',
                'High humidity and frequent rain',
                'Poor air circulation around plants',
                'Overhead watering that wets leaves',
                'Infected plant debris from previous seasons'
            ],
            'symptoms': [
                'Dark brown or black lesions on leaves',
                'Water-soaked spots that spread rapidly',
                'White fuzzy growth on leaf undersides',
                'Brown or black streaks on stems',
                'Dark, sunken spots on fruits'
            ],
            'organic_treatment': {
                'steps': [
                    'Remove and destroy infected plant parts immediately',
                    'Apply copper-based organic fungicide every 7-10 days',
                    'Spray baking soda solution (1 tsp per quart water)',
                    'Improve air circulation by proper spacing',
                    'Apply compost tea as foliar spray'
                ],
                'timing': 'Early morning or late evening',
                'duration': '2-3 weeks of consistent treatment',
                'recovery_time': '3-4 weeks for new growth'
            },
            'chemical_treatment': {
                'steps': [
                    'Apply systemic fungicide containing metalaxyl',
                    'Use protectant fungicide with chlorothalonil',
                    'Alternate between different fungicide types',
                    'Remove infected plant debris',
                    'Apply preventive fungicide before rain'
                ],
                'timing': 'Before rain or high humidity periods',
                'duration': '10-14 days treatment cycle',
                'recovery_time': '2-3 weeks for recovery'
            },
            'prevention_tips': [
                'Choose resistant tomato varieties',
                'Avoid overhead watering',
                'Provide adequate plant spacing',
                'Remove plant debris at season end',
                'Rotate crops every 3-4 years',
                'Apply mulch to prevent soil splash'
            ],
            'follow_up_care': 'Monitor plants weekly for new symptoms. Continue preventive spraying during favorable disease conditions.'
        },
        
        'Potato Early Blight': {
            'scientific_name': 'Alternaria solani',
            'common_names': ['Early Blight', 'Target Spot'],
            'affected_plants': ['Potato', 'Tomato', 'Eggplant'],
            'causes': [
                'Warm, humid weather (75-85°F)',
                'Plants stressed by drought or nutrients',
                'Dense plant canopy with poor air flow',
                'Wounds from insects or mechanical damage',
                'Infected seed potatoes or transplants'
            ],
            'symptoms': [
                'Brown spots with concentric rings on leaves',
                'Yellowing leaves starting from bottom',
                'Dark, sunken lesions on stems',
                'Raised, dark spots on tubers',
                'Premature leaf drop and defoliation'
            ],
            'organic_treatment': {
                'steps': [
                    'Remove infected leaves and dispose properly',
                    'Apply neem oil spray every 7-14 days',
                    'Use copper fungicide as directed',
                    'Improve soil nutrition with compost',
                    'Ensure adequate watering to reduce stress'
                ],
                'timing': 'Early morning application preferred',
                'duration': '3-4 weeks of regular treatment',
                'recovery_time': '4-6 weeks for full recovery'
            },
            'chemical_treatment': {
                'steps': [
                    'Apply fungicide containing azoxystrobin',
                    'Use alternating chemistry to prevent resistance',
                    'Treat soil with appropriate fungicide',
                    'Remove and destroy infected plant material',
                    'Apply foliar fertilizer to strengthen plants'
                ],
                'timing': 'Apply before disease pressure increases',
                'duration': '2-3 weeks intensive treatment',
                'recovery_time': '3-4 weeks for improvement'
            },
            'prevention_tips': [
                'Plant certified disease-free seed potatoes',
                'Maintain proper plant nutrition',
                'Avoid overhead irrigation',
                'Practice crop rotation',
                'Remove volunteer potato plants',
                'Hill potatoes properly to prevent tuber exposure'
            ],
            'follow_up_care': 'Continue monitoring for 6-8 weeks. Harvest tubers carefully to avoid wounding.'
        },
        
        'Corn Leaf Spot': {
            'scientific_name': 'Bipolaris maydis',
            'common_names': ['Southern Corn Leaf Blight', 'Leaf Spot'],
            'affected_plants': ['Corn', 'Sorghum'],
            'causes': [
                'Warm, humid conditions (70-80°F)',
                'Prolonged leaf wetness from dew or rain',
                'Dense plant populations',
                'Susceptible corn varieties',
                'Crop residue harboring spores'
            ],
            'symptoms': [
                'Small, oval spots on leaves',
                'Tan to brown lesions with dark borders',
                'Lesions may merge to form large dead areas',
                'Yellowing and death of lower leaves',
                'Reduced ear fill and grain quality'
            ],
            'organic_treatment': {
                'steps': [
                    'Remove infected plant debris',
                    'Apply organic fungicide with Bacillus subtilis',
                    'Improve air circulation between rows',
                    'Use foliar feeding to strengthen plants',
                    'Apply silica-based supplements'
                ],
                'timing': 'Early morning or evening application',
                'duration': '2-3 weeks treatment period',
                'recovery_time': '3-5 weeks for new growth'
            },
            'chemical_treatment': {
                'steps': [
                    'Apply fungicide containing propiconazole',
                    'Use systemic fungicide for severe infections',
                    'Time applications with disease forecasts',
                    'Ensure good spray coverage',
                    'Consider soil-applied fungicides'
                ],
                'timing': 'Tassel to early silk stage critical',
                'duration': '14-21 days treatment window',
                'recovery_time': '2-4 weeks for stabilization'
            },
            'prevention_tips': [
                'Plant resistant corn hybrids',
                'Manage crop residue properly',
                'Avoid excessive nitrogen fertilization',
                'Maintain proper plant population',
                'Scout fields regularly during humid periods',
                'Practice crop rotation'
            ],
            'follow_up_care': 'Monitor grain filling process. Harvest at proper moisture to prevent quality loss.'
        },
        
        'Rice Blast': {
            'scientific_name': 'Magnaporthe oryzae',
            'common_names': ['Rice Blast', 'Leaf Blast', 'Neck Blast'],
            'affected_plants': ['Rice', 'Wheat', 'Barley'],
            'causes': [
                'High humidity and frequent rain',
                'Temperature between 70-80°F',
                'Dense plant populations',
                'Excessive nitrogen fertilization',
                'Poor field drainage'
            ],
            'symptoms': [
                'Diamond-shaped lesions on leaves',
                'Gray centers with brown borders',
                'Neck rot causing lodging',
                'Panicle blast affecting grain fill',
                'Whitish or gray lesions on stems'
            ],
            'organic_treatment': {
                'steps': [
                    'Drain field to reduce humidity',
                    'Apply silicon fertilizer to strengthen plants',
                    'Use biological fungicides with Trichoderma',
                    'Remove infected plant parts',
                    'Apply potassium-rich organic fertilizer'
                ],
                'timing': 'Apply during dry weather',
                'duration': '3-4 weeks treatment cycle',
                'recovery_time': '4-6 weeks for recovery'
            },
            'chemical_treatment': {
                'steps': [
                    'Apply systemic fungicide containing tricyclazole',
                    'Use protective fungicides before rain',
                    'Time applications at critical growth stages',
                    'Ensure proper water management',
                    'Apply foliar fertilizer for plant health'
                ],
                'timing': 'Tillering and panicle initiation stages',
                'duration': '2-3 applications over 4 weeks',
                'recovery_time': '3-5 weeks for improvement'
            },
            'prevention_tips': [
                'Plant resistant rice varieties',
                'Maintain proper water levels',
                'Avoid excessive nitrogen fertilizer',
                'Practice crop rotation',
                'Remove crop residues',
                'Use certified clean seed'
            ],
            'follow_up_care': 'Monitor panicle development closely. Adjust water management based on weather conditions.'
        },
        
        'Wheat Rust': {
            'scientific_name': 'Puccinia triticina',
            'common_names': ['Leaf Rust', 'Brown Rust'],
            'affected_plants': ['Wheat', 'Barley', 'Rye'],
            'causes': [
                'Moderate temperatures (60-70°F)',
                'High humidity and dew formation',
                'Wind dispersal of spores',
                'Susceptible wheat varieties',
                'Continuous wheat cropping'
            ],
            'symptoms': [
                'Small orange-brown pustules on leaves',
                'Pustules may merge to form large patches',
                'Yellowing and drying of leaves',
                'Reduced grain filling',
                'Weakened stems leading to lodging'
            ],
            'organic_treatment': {
                'steps': [
                    'Apply sulfur-based organic fungicide',
                    'Use plant extracts like neem oil',
                    'Enhance plant nutrition with compost',
                    'Improve air circulation',
                    'Apply foliar micronutrients'
                ],
                'timing': 'Early morning application',
                'duration': '3-4 weeks treatment',
                'recovery_time': '4-6 weeks for stabilization'
            },
            'chemical_treatment': {
                'steps': [
                    'Apply fungicide containing tebuconazole',
                    'Use systemic fungicides for severe cases',
                    'Time applications with disease forecasts',
                    'Ensure complete plant coverage',
                    'Consider tank mixing with fertilizers'
                ],
                'timing': 'Flag leaf emergence to heading',
                'duration': '2-3 applications needed',
                'recovery_time': '3-4 weeks for recovery'
            },
            'prevention_tips': [
                'Plant rust-resistant wheat varieties',
                'Practice crop rotation',
                'Remove volunteer wheat plants',
                'Monitor weather conditions',
                'Scout fields regularly',
                'Maintain balanced plant nutrition'
            ],
            'follow_up_care': 'Continue monitoring through grain filling. Harvest at optimal timing to minimize losses.'
        },
        
        'Apple Scab': {
            'scientific_name': 'Venturia inaequalis',
            'common_names': ['Apple Scab', 'Black Spot'],
            'affected_plants': ['Apple', 'Crabapple', 'Pear'],
            'causes': [
                'Cool, wet spring weather',
                'Poor air circulation in orchard',
                'Infected fallen leaves',
                'Prolonged leaf wetness',
                'Susceptible apple varieties'
            ],
            'symptoms': [
                'Olive-green to black spots on leaves',
                'Velvety appearance of lesions',
                'Premature leaf drop',
                'Scabby lesions on fruits',
                'Cracked and distorted fruits'
            ],
            'organic_treatment': {
                'steps': [
                    'Remove and compost fallen leaves',
                    'Apply lime sulfur during dormant season',
                    'Use copper fungicide in early spring',
                    'Prune for better air circulation',
                    'Apply beneficial microorganisms'
                ],
                'timing': 'Start at bud break',
                'duration': '6-8 weeks treatment period',
                'recovery_time': '8-10 weeks for improvement'
            },
            'chemical_treatment': {
                'steps': [
                    'Apply fungicide containing myclobutanil',
                    'Use protective fungicides before rain',
                    'Time applications with infection periods',
                    'Ensure thorough spray coverage',
                    'Continue through petal fall'
                ],
                'timing': 'Green tip through petal fall',
                'duration': '4-6 applications needed',
                'recovery_time': '6-8 weeks for recovery'
            },
            'prevention_tips': [
                'Plant scab-resistant apple varieties',
                'Improve orchard sanitation',
                'Prune for air circulation',
                'Remove water sprouts and suckers',
                'Mulch around trees',
                'Monitor weather conditions'
            ],
            'follow_up_care': 'Continue preventive spraying through summer. Maintain good orchard hygiene.'
        },
        
        'Powdery Mildew': {
            'scientific_name': 'Erysiphe cichoracearum',
            'common_names': ['Powdery Mildew', 'White Mold'],
            'affected_plants': ['Cucumbers', 'Squash', 'Pumpkins', 'Roses'],
            'causes': [
                'High humidity with dry leaf surfaces',
                'Moderate temperatures (68-78°F)',
                'Poor air circulation',
                'Dense plant growth',
                'Shaded growing conditions'
            ],
            'symptoms': [
                'White powdery coating on leaves',
                'Yellowing and browning of affected leaves',
                'Stunted plant growth',
                'Distorted leaves and shoots',
                'Reduced fruit quality and yield'
            ],
            'organic_treatment': {
                'steps': [
                    'Spray baking soda solution (1 tsp per quart)',
                    'Apply neem oil every 7-14 days',
                    'Use milk spray (1 part milk to 10 parts water)',
                    'Improve air circulation around plants',
                    'Remove affected plant parts'
                ],
                'timing': 'Early morning or late evening',
                'duration': '2-4 weeks treatment',
                'recovery_time': '3-6 weeks for recovery'
            },
            'chemical_treatment': {
                'steps': [
                    'Apply fungicide containing propiconazole',
                    'Use systemic fungicides for severe cases',
                    'Rotate between different fungicide classes',
                    'Ensure complete plant coverage',
                    'Continue preventive applications'
                ],
                'timing': 'Apply at first sign of disease',
                'duration': '3-4 applications over 6 weeks',
                'recovery_time': '4-6 weeks for improvement'
            },
            'prevention_tips': [
                'Plant resistant varieties when available',
                'Provide adequate plant spacing',
                'Avoid overhead watering',
                'Improve air circulation',
                'Remove infected plant debris',
                'Avoid excessive nitrogen fertilization'
            ],
            'follow_up_care': 'Monitor plants weekly during favorable conditions. Maintain good growing practices.'
        }
    }
```
