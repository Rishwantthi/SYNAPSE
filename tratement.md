```
"""
Treatment analysis system that provides detailed treatment recommendations for plant diseases.
"""

from disease_database import get_disease_database

class TreatmentAnalyzer:
    def __init__(self):
        self.disease_database = get_disease_database()
        
    def get_disease_info(self, disease_name):
        """Get comprehensive information about a specific disease."""
        return self.disease_database.get(disease_name, self._get_default_disease_info(disease_name))
    
    def _get_default_disease_info(self, disease_name):
        """Provide default disease information when specific disease is not in database."""
        return {
            'scientific_name': 'Unknown',
            'common_names': [disease_name],
            'affected_plants': ['Various'],
            'causes': [
                'Environmental stress conditions',
                'Poor plant health and nutrition',
                'Favorable weather for pathogen development',
                'Infected plant material or soil',
                'Poor garden hygiene practices'
            ],
            'symptoms': [
                'Discoloration of leaves or stems',
                'Unusual spots or lesions',
                'Wilting or stunted growth',
                'Abnormal plant appearance',
                'Reduced vigor and productivity'
            ],
            'organic_treatment': {
                'steps': [
                    'Remove and destroy infected plant parts',
                    'Improve air circulation around plants',
                    'Apply organic fungicide or bactericide',
                    'Enhance plant nutrition with compost',
                    'Reduce plant stress through proper care'
                ],
                'timing': 'Early morning or late evening',
                'duration': '2-4 weeks of consistent treatment',
                'recovery_time': '4-8 weeks depending on severity'
            },
            'chemical_treatment': {
                'steps': [
                    'Apply appropriate systemic fungicide',
                    'Use protective spray before rain',
                    'Follow label instructions carefully',
                    'Remove infected plant material',
                    'Monitor and reapply as needed'
                ],
                'timing': 'As directed on product label',
                'duration': '2-3 applications over 4-6 weeks',
                'recovery_time': '3-6 weeks for improvement'
            },
            'prevention_tips': [
                'Choose disease-resistant plant varieties',
                'Maintain proper plant spacing',
                'Practice crop rotation',
                'Keep garden clean and free of debris',
                'Water at soil level, not on leaves',
                'Monitor plants regularly for early detection'
            ],
            'follow_up_care': 'Continue monitoring for 6-8 weeks. Maintain good cultural practices to prevent recurrence.'
        }
    
    def analyze_treatment_effectiveness(self, disease_name, treatment_type, severity):
        """Analyze the effectiveness of different treatment approaches."""
        disease_info = self.get_disease_info(disease_name)
        
        effectiveness_scores = {
            'organic': {
                'mild': 85,
                'moderate': 70,
                'severe': 50
            },
            'chemical': {
                'mild': 95,
                'moderate': 90,
                'severe': 80
            }
        }
        
        base_score = effectiveness_scores.get(treatment_type, {}).get(severity.lower(), 70)
        
        # Adjust based on disease characteristics
        if disease_name in self.disease_database:
            # Some diseases respond better to specific treatments
            if 'rust' in disease_name.lower() and treatment_type == 'chemical':
                base_score += 5
            elif 'mildew' in disease_name.lower() and treatment_type == 'organic':
                base_score += 10
        
        return min(base_score, 100)
    
    def get_treatment_timeline(self, disease_name, treatment_type, severity):
        """Generate a detailed treatment timeline."""
        disease_info = self.get_disease_info(disease_name)
        treatment_info = disease_info.get(f'{treatment_type}_treatment', {})
        
        timeline = []
        
        # Week 1-2: Initial treatment
        timeline.append({
            'week': '1-2',
            'action': 'Begin intensive treatment',
            'tasks': [
                'Remove all infected plant parts',
                'Apply first treatment application',
                'Improve growing conditions',
                'Monitor plant response'
            ]
        })
        
        # Week 3-4: Follow-up treatment
        timeline.append({
            'week': '3-4',
            'action': 'Continue treatment protocol',
            'tasks': [
                'Apply second treatment if needed',
                'Assess treatment effectiveness',
                'Adjust treatment approach if necessary',
                'Continue monitoring'
            ]
        })
        
        # Week 5-6: Recovery phase
        timeline.append({
            'week': '5-6',
            'action': 'Recovery and prevention',
            'tasks': [
                'Reduce treatment frequency',
                'Focus on plant health improvement',
                'Implement prevention measures',
                'Monitor for new growth'
            ]
        })
        
        # Adjust timeline based on severity
        if severity.lower() == 'severe':
            timeline.append({
                'week': '7-8',
                'action': 'Extended recovery',
                'tasks': [
                    'Continue monitoring closely',
                    'Apply maintenance treatments',
                    'Support plant recovery',
                    'Plan prevention strategy'
                ]
            })
        
        return timeline
    
    def get_seasonal_recommendations(self, disease_name, current_season):
        """Provide season-specific treatment recommendations."""
        seasonal_advice = {
            'spring': {
                'focus': 'Prevention and early treatment',
                'activities': [
                    'Apply preventive treatments before disease pressure',
                    'Improve drainage from winter moisture',
                    'Remove overwintered disease sources',
                    'Monitor for early disease development'
                ]
            },
            'summer': {
                'focus': 'Active management and plant support',
                'activities': [
                    'Maintain consistent treatment schedule',
                    'Ensure adequate plant nutrition',
                    'Manage heat stress to prevent secondary infections',
                    'Monitor for disease spread'
                ]
            },
            'fall': {
                'focus': 'Cleanup and preparation',
                'activities': [
                    'Remove infected plant debris',
                    'Apply final treatments before dormancy',
                    'Prepare plants for winter',
                    'Plan next season prevention'
                ]
            },
            'winter': {
                'focus': 'Dormant season management',
                'activities': [
                    'Apply dormant season treatments',
                    'Plan next year\'s prevention strategy',
                    'Source resistant varieties',
                    'Prepare equipment and materials'
                ]
            }
        }
        
        return seasonal_advice.get(current_season.lower(), seasonal_advice['spring'])
    
    def get_integrated_management_plan(self, disease_name, farm_size_acres=1.0):
        """Create an integrated disease management plan."""
        disease_info = self.get_disease_info(disease_name)
        
        plan = {
            'immediate_actions': [
                'Assess disease severity and extent',
                'Remove and destroy infected plant material',
                'Begin appropriate treatment protocol',
                'Improve environmental conditions'
            ],
            'short_term_strategy': [
                'Implement consistent treatment schedule',
                'Monitor treatment effectiveness',
                'Adjust approach based on plant response',
                'Prevent disease spread to healthy plants'
            ],
            'long_term_prevention': [
                'Select disease-resistant varieties',
                'Improve cultural practices',
                'Implement crop rotation',
                'Maintain garden hygiene'
            ],
            'monitoring_schedule': {
                'daily': 'Check treated plants for response',
                'weekly': 'Assess overall disease progression',
                'bi_weekly': 'Evaluate treatment effectiveness',
                'monthly': 'Review and adjust management plan'
            },
            'success_indicators': [
                'Reduction in new disease symptoms',
                'Improved plant vigor and growth',
                'No spread to healthy plants',
                'Normal fruit/flower development'
            ]
        }
        
        return plan
    
    def get_resistance_management_advice(self, disease_name, treatment_type):
        """Provide advice on managing resistance to treatments."""
        advice = {
            'rotation_strategy': [
                'Alternate between different chemical classes',
                'Mix organic and chemical approaches',
                'Use cultural controls as primary defense',
                'Avoid over-reliance on single products'
            ],
            'application_best_practices': [
                'Use recommended rates and timing',
                'Ensure complete plant coverage',
                'Apply under optimal weather conditions',
                'Follow pre-harvest interval requirements'
            ],
            'monitoring_resistance': [
                'Track treatment effectiveness over time',
                'Note any reduced efficacy',
                'Consult with agricultural extension',
                'Consider resistance testing if available'
            ]
        }
        
        return advice
```
