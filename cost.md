```
"""
Cost estimation system for plant disease treatments including materials, labor, and equipment costs.
"""

class CostEstimator:
    def __init__(self):
        self.material_costs = self._load_material_costs()
        self.labor_rates = self._load_labor_rates()
        self.equipment_costs = self._load_equipment_costs()
        
    def _load_material_costs(self):
        """Load material costs for different treatments (per acre) in Indian Rupees."""
        return {
            'organic': {
                'neem_oil': {'price_per_unit': 800, 'unit': 'litre', 'coverage_per_unit': 3.0},
                'copper_fungicide': {'price_per_unit': 600, 'unit': 'kg', 'coverage_per_unit': 4.0},
                'baking_soda': {'price_per_unit': 50, 'unit': 'kg', 'coverage_per_unit': 8.0},
                'compost_tea': {'price_per_unit': 200, 'unit': 'litre', 'coverage_per_unit': 2.0},
                'beneficial_microbes': {'price_per_unit': 1200, 'unit': 'packet', 'coverage_per_unit': 2.0},
                'lime_sulfur': {'price_per_unit': 700, 'unit': 'litre', 'coverage_per_unit': 4.0},
                'diatomaceous_earth': {'price_per_unit': 400, 'unit': 'kg', 'coverage_per_unit': 6.0}
            },
            'chemical': {
                'systemic_fungicide': {'price_per_unit': 1800, 'unit': 'litre', 'coverage_per_unit': 6.0},
                'protective_fungicide': {'price_per_unit': 1200, 'unit': 'kg', 'coverage_per_unit': 8.0},
                'copper_sulfate': {'price_per_unit': 350, 'unit': 'kg', 'coverage_per_unit': 5.0},
                'strobilurin_fungicide': {'price_per_unit': 2200, 'unit': '500ml', 'coverage_per_unit': 5.0},
                'triazole_fungicide': {'price_per_unit': 2800, 'unit': '500ml', 'coverage_per_unit': 4.0},
                'adjuvant': {'price_per_unit': 500, 'unit': 'litre', 'coverage_per_unit': 15.0},
                'spreader_sticker': {'price_per_unit': 600, 'unit': '500ml', 'coverage_per_unit': 10.0}
            }
        }
    
    def _load_labor_rates(self):
        """Load labor rates for different activities in Indian Rupees."""
        return {
            'scouting': 150,  # per hour
            'spraying': 200,  # per hour
            'pruning': 180,  # per hour
            'cleanup': 120,  # per hour
            'monitoring': 150  # per hour
        }
    
    def _load_equipment_costs(self):
        """Load equipment costs and rental rates in Indian Rupees."""
        return {
            'hand_sprayer': {'purchase': 800, 'rental_per_day': 50},
            'backpack_sprayer': {'purchase': 4500, 'rental_per_day': 150},
            'boom_sprayer': {'purchase': 80000, 'rental_per_day': 1200},
            'airblast_sprayer': {'purchase': 250000, 'rental_per_day': 3000},
            'protective_equipment': {'purchase': 1200, 'rental_per_day': 100}
        }
    
    def calculate_material_costs(self, treatment_type, disease, land_size_acres):
        """Calculate material costs for treatment."""
        if treatment_type not in self.material_costs:
            return {'total': 0, 'breakdown': {}}
        
        materials = self.material_costs[treatment_type]
        total_cost = 0
        breakdown = {}
        
        # Get treatment-specific materials based on disease
        required_materials = self._get_required_materials(treatment_type, disease)
        
        for material in required_materials:
            if material in materials:
                material_info = materials[material]
                units_needed = land_size_acres / material_info['coverage_per_unit']
                cost = units_needed * material_info['price_per_unit']
                total_cost += cost
                breakdown[material] = {
                    'units_needed': round(units_needed, 2),
                    'unit_type': material_info['unit'],
                    'unit_price': material_info['price_per_unit'],
                    'total_cost': round(cost, 2)
                }
        
        return {'total': round(total_cost, 2), 'breakdown': breakdown}
    
    def _get_required_materials(self, treatment_type, disease):
        """Get required materials based on treatment type and disease."""
        disease_materials = {
            'organic': {
                'Tomato Late Blight': ['copper_fungicide', 'neem_oil'],
                'Potato Early Blight': ['neem_oil', 'copper_fungicide'],
                'Corn Leaf Spot': ['beneficial_microbes', 'neem_oil'],
                'Rice Blast': ['beneficial_microbes', 'copper_fungicide'],
                'Wheat Rust': ['lime_sulfur', 'neem_oil'],
                'Apple Scab': ['lime_sulfur', 'copper_fungicide'],
                'Powdery Mildew': ['baking_soda', 'neem_oil'],
                'Bacterial Leaf Spot': ['copper_fungicide', 'beneficial_microbes'],
                'Anthracnose': ['copper_fungicide', 'neem_oil'],
                'default': ['neem_oil', 'copper_fungicide']
            },
            'chemical': {
                'Tomato Late Blight': ['systemic_fungicide', 'adjuvant'],
                'Potato Early Blight': ['systemic_fungicide', 'adjuvant'],
                'Corn Leaf Spot': ['strobilurin_fungicide', 'adjuvant'],
                'Rice Blast': ['triazole_fungicide', 'adjuvant'],
                'Wheat Rust': ['triazole_fungicide', 'adjuvant'],
                'Apple Scab': ['systemic_fungicide', 'adjuvant'],
                'Powdery Mildew': ['triazole_fungicide', 'spreader_sticker'],
                'Bacterial Leaf Spot': ['copper_sulfate', 'adjuvant'],
                'Anthracnose': ['systemic_fungicide', 'adjuvant'],
                'default': ['systemic_fungicide', 'adjuvant']
            }
        }
        
        return disease_materials.get(treatment_type, {}).get(disease, 
                disease_materials[treatment_type]['default'])
    
    def calculate_labor_costs(self, treatment_type, land_size_acres, severity):
        """Calculate labor costs for treatment application."""
        labor_breakdown = {}
        total_labor_cost = 0
        
        # Base time requirements (hours per acre) - adjusted for Indian farming conditions
        time_requirements = {
            'scouting': 0.3,
            'spraying': 0.8 if treatment_type == 'organic' else 0.6,
            'pruning': 1.5 if severity.lower() in ['severe', 'moderate'] else 0.8,
            'cleanup': 1.0 if severity.lower() == 'severe' else 0.6,
            'monitoring': 0.2
        }
        
        # Adjust for land size efficiency
        if land_size_acres > 5:
            efficiency_factor = 0.8  # More efficient on larger areas
        elif land_size_acres > 1:
            efficiency_factor = 0.9
        else:
            efficiency_factor = 1.0
        
        for activity, base_hours in time_requirements.items():
            if activity == 'pruning' and severity.lower() == 'mild':
                continue  # Skip pruning for mild cases
            
            hours_needed = base_hours * land_size_acres * efficiency_factor
            cost = hours_needed * self.labor_rates[activity]
            total_labor_cost += cost
            
            labor_breakdown[activity] = {
                'hours': round(hours_needed, 2),
                'rate_per_hour': self.labor_rates[activity],
                'total_cost': round(cost, 2)
            }
        
        return {'total': round(total_labor_cost, 2), 'breakdown': labor_breakdown}
    
    def calculate_equipment_costs(self, land_size_acres, treatment_duration_days=7):
        """Calculate equipment costs based on land size and treatment duration."""
        equipment_breakdown = {}
        total_equipment_cost = 0
        
        # Determine appropriate equipment based on land size
        if land_size_acres <= 1:
            equipment = ['hand_sprayer', 'protective_equipment']
        elif land_size_acres <= 5:
            equipment = ['backpack_sprayer', 'protective_equipment']
        elif land_size_acres <= 20:
            equipment = ['boom_sprayer', 'protective_equipment']
        else:
            equipment = ['airblast_sprayer', 'protective_equipment']
        
        for equip in equipment:
            if equip in self.equipment_costs:
                equip_info = self.equipment_costs[equip]
                
                # Decide between rental and purchase - more realistic for small farmers
                rental_cost = equip_info['rental_per_day'] * treatment_duration_days
                purchase_cost = equip_info['purchase']
                
                # For small farmers, favor rental unless very small equipment
                if land_size_acres < 5 or rental_cost < purchase_cost * 0.4:
                    cost = rental_cost
                    acquisition_type = 'rental'
                else:
                    cost = purchase_cost
                    acquisition_type = 'purchase'
                
                total_equipment_cost += cost
                equipment_breakdown[equip] = {
                    'acquisition_type': acquisition_type,
                    'duration_days': treatment_duration_days if acquisition_type == 'rental' else 'N/A',
                    'total_cost': round(cost, 2)
                }
        
        return {'total': round(total_equipment_cost, 2), 'breakdown': equipment_breakdown}
    
    def calculate_treatment_cost(self, treatment_type, disease, land_size_acres, severity='moderate'):
        """Calculate total treatment cost including all components."""
        
        # Calculate individual cost components
        material_costs = self.calculate_material_costs(treatment_type, disease, land_size_acres)
        labor_costs = self.calculate_labor_costs(treatment_type, land_size_acres, severity)
        equipment_costs = self.calculate_equipment_costs(land_size_acres)
        
        # Calculate totals
        total_cost = material_costs['total'] + labor_costs['total'] + equipment_costs['total']
        cost_per_acre = total_cost / land_size_acres if land_size_acres > 0 else total_cost
        
        # Generate cost-saving tips
        savings_tips = self._generate_savings_tips(treatment_type, land_size_acres, total_cost)
        
        return {
            'total_per_acre': round(cost_per_acre, 2),
            'total_cost': round(total_cost, 2),
            'materials': material_costs['total'],
            'labor': labor_costs['total'],
            'equipment': equipment_costs['total'],
            'detailed_breakdown': {
                'materials': material_costs['breakdown'],
                'labor': labor_costs['breakdown'],
                'equipment': equipment_costs['breakdown']
            },
            'savings_tips': savings_tips
        }
    
    def _generate_savings_tips(self, treatment_type, land_size_acres, total_cost):
        """Generate cost-saving tips based on treatment analysis."""
        tips = []
        
        if total_cost > 5000 * land_size_acres:
            tips.append("Consider organic alternatives to reduce material costs")
        
        if land_size_acres < 2:
            tips.append("Rent equipment instead of purchasing for small areas")
        
        if treatment_type == 'chemical':
            tips.append("Tank-mix compatible products to reduce application costs")
        
        tips.extend([
            "Buy materials in bulk during off-season for better prices",
            "Join with neighbors for group purchases",
            "Focus on prevention to reduce treatment needs",
            "Monitor regularly for early detection and cheaper treatment"
        ])
        
        return tips[:3]  # Return top 3 tips
    
    def compare_treatment_costs(self, disease, land_size_acres, severity='moderate'):
        """Compare costs between organic and chemical treatments."""
        organic_cost = self.calculate_treatment_cost('organic', disease, land_size_acres, severity)
        chemical_cost = self.calculate_treatment_cost('chemical', disease, land_size_acres, severity)
        
        comparison = {
            'organic': organic_cost,
            'chemical': chemical_cost,
            'cost_difference': round(chemical_cost['total_cost'] - organic_cost['total_cost'], 2),
            'cheaper_option': 'organic' if organic_cost['total_cost'] < chemical_cost['total_cost'] else 'chemical',
            'savings_amount': round(abs(chemical_cost['total_cost'] - organic_cost['total_cost']), 2)
        }
        
        return comparison
    
    def estimate_seasonal_costs(self, diseases_list, land_size_acres):
        """Estimate total seasonal disease management costs."""
        total_seasonal_cost = 0
        disease_costs = {}
        
        for disease in diseases_list:
            # Assume moderate severity and chemical treatment for estimation
            cost = self.calculate_treatment_cost('chemical', disease, land_size_acres, 'moderate')
            total_seasonal_cost += cost['total_cost']
            disease_costs[disease] = cost
        
        # Add 20% buffer for unexpected issues
        total_with_buffer = total_seasonal_cost * 1.2
        
        return {
            'total_base_cost': round(total_seasonal_cost, 2),
            'total_with_buffer': round(total_with_buffer, 2),
            'cost_per_acre': round(total_with_buffer / land_size_acres, 2),
            'individual_diseases': disease_costs,
            'budget_recommendations': self._generate_budget_recommendations(total_with_buffer, land_size_acres)
        }
    
    def _generate_budget_recommendations(self, total_cost, land_size_acres):
        """Generate budget recommendations for disease management."""
        cost_per_acre = total_cost / land_size_acres
        
        recommendations = []
        
        if cost_per_acre > 8000:
            recommendations.append("Consider disease-resistant varieties to reduce treatment needs")
            recommendations.append("Implement integrated pest management (IPM) practices")
        
        if cost_per_acre > 5000:
            recommendations.append("Focus on prevention and cultural controls")
            recommendations.append("Scout regularly for early disease detection")
        
        recommendations.extend([
            "Set aside 20% contingency fund for unexpected disease outbreaks",
            "Consider crop insurance for high-value crops",
            "Track treatment effectiveness to optimize future spending"
        ])
        
        return recommendations
```
