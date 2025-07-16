```
from datetime import datetime, timedelta
import json
import streamlit as st

class PlantCareScheduler:
    def __init__(self):
        self.care_frequency_map = {
            'daily': 1,
            'every 2-3 days': 2,
            'weekly': 7,
            'when dry': 3,  # Default to every 3 days for "when dry"
            'bi-weekly': 14,
            'monthly': 30
        }
    
    def create_care_schedule(self, plant_record):
        """
        Create a care schedule for a plant
        """
        plant_info = plant_record['info']
        care_requirements = plant_info['care_requirements']
        
        # Create different types of care tasks
        schedule = {
            'watering': {
                'frequency': self.care_frequency_map.get(care_requirements['water'], 3),
                'last_done': plant_record['care_start_date'],
                'description': f"Water your {plant_record['nickname']} according to {care_requirements['water']} schedule"
            },
            'fertilizing': {
                'frequency': 30,  # Monthly fertilizing
                'last_done': plant_record['care_start_date'],
                'description': f"Apply fertilizer to {plant_record['nickname']}"
            },
            'checking': {
                'frequency': 7,  # Weekly health check
                'last_done': plant_record['care_start_date'],
                'description': f"Check {plant_record['nickname']} for pests, diseases, and overall health"
            },
            'pruning': {
                'frequency': 90,  # Quarterly pruning
                'last_done': plant_record['care_start_date'],
                'description': f"Prune dead leaves and stems from {plant_record['nickname']}"
            }
        }
        
        # Add location-specific tasks
        if plant_record['location'].lower() in ['balcony', 'terrace']:
            schedule['sun_protection'] = {
                'frequency': 1,  # Daily during summer
                'last_done': plant_record['care_start_date'],
                'description': f"Check if {plant_record['nickname']} needs sun protection"
            }
        
        # Store in session state
        if 'care_schedule' not in st.session_state:
            st.session_state.care_schedule = {}
        
        st.session_state.care_schedule[plant_record['id']] = schedule
        
        return schedule
    
    def get_daily_tasks(self, plant_record, date):
        """
        Get tasks that need to be done for a plant on a specific date
        """
        import streamlit as st
        
        plant_id = plant_record['id']
        
        if plant_id not in st.session_state.care_schedule:
            return []
        
        schedule = st.session_state.care_schedule[plant_id]
        tasks = []
        
        for task_type, task_info in schedule.items():
            # Calculate if task is due
            last_done = datetime.strptime(task_info['last_done'], '%Y-%m-%d').date()
            days_since = (date - last_done).days
            
            if days_since >= task_info['frequency']:
                tasks.append({
                    'id': f"{plant_id}_{task_type}_{date}",
                    'plant_id': plant_id,
                    'plant_name': plant_record['custom_name'],
                    'task': task_type.replace('_', ' ').title(),
                    'description': task_info['description'],
                    'due_date': date,
                    'priority': self.get_task_priority(task_type, days_since, task_info['frequency'])
                })
        
        # Sort by priority
        tasks.sort(key=lambda x: x['priority'], reverse=True)
        return tasks
    
    def get_task_priority(self, task_type, days_since, frequency):
        """
        Calculate task priority based on type and overdue days
        """
        base_priority = {
            'watering': 10,
            'checking': 8,
            'fertilizing': 6,
            'pruning': 4,
            'sun_protection': 7
        }
        
        # Increase priority based on how overdue the task is
        overdue_multiplier = max(1, days_since / frequency)
        
        return base_priority.get(task_type, 5) * overdue_multiplier
    
    def get_weekly_schedule(self, plant_record, start_date):
        """
        Get a week's worth of tasks for a plant
        """
        weekly_tasks = {}
        
        for i in range(7):
            date = start_date + timedelta(days=i)
            daily_tasks = self.get_daily_tasks(plant_record, date)
            
            if daily_tasks:
                weekly_tasks[date.isoformat()] = daily_tasks
        
        return weekly_tasks
    
    def mark_task_complete(self, plant_id, task_type, completion_date):
        """
        Mark a task as complete and update the schedule
        """
        import streamlit as st
        
        if plant_id in st.session_state.care_schedule:
            if task_type in st.session_state.care_schedule[plant_id]:
                st.session_state.care_schedule[plant_id][task_type]['last_done'] = completion_date.isoformat()
                return True
        
        return False
    
    def get_plant_health_score(self, plant_record):
        """
        Calculate a health score based on care adherence
        """
        import streamlit as st
        
        plant_id = plant_record['id']
        
        if plant_id not in st.session_state.care_schedule:
            return 100  # New plant, assume healthy
        
        schedule = st.session_state.care_schedule[plant_id]
        today = datetime.now().date()
        
        total_score = 0
        task_count = 0
        
        for task_type, task_info in schedule.items():
            last_done = datetime.strptime(task_info['last_done'], '%Y-%m-%d').date()
            days_since = (today - last_done).days
            frequency = task_info['frequency']
            
            # Calculate score for this task (0-100)
            if days_since <= frequency:
                task_score = 100
            elif days_since <= frequency * 1.5:
                task_score = 75
            elif days_since <= frequency * 2:
                task_score = 50
            else:
                task_score = 25
            
            total_score += task_score
            task_count += 1
        
        return int(total_score / task_count) if task_count > 0 else 100
    
    def get_care_reminders(self, plant_record):
        """
        Get personalized care reminders for a plant
        """
        import streamlit as st
        
        plant_id = plant_record['id']
        reminders = []
        
        if plant_id not in st.session_state.care_schedule:
            return reminders
        
        schedule = st.session_state.care_schedule[plant_id]
        today = datetime.now().date()
        
        for task_type, task_info in schedule.items():
            last_done = datetime.strptime(task_info['last_done'], '%Y-%m-%d').date()
            days_since = (today - last_done).days
            frequency = task_info['frequency']
            
            if days_since >= frequency:
                urgency = "overdue" if days_since > frequency * 1.2 else "due"
                reminders.append({
                    'task': task_type.replace('_', ' ').title(),
                    'urgency': urgency,
                    'days_overdue': days_since - frequency,
                    'description': task_info['description']
                })
        
        return reminders
    
    def get_seasonal_adjustments(self, plant_record, season):
        """
        Get seasonal adjustments for care schedule
        """
        adjustments = {}
        
        plant_info = plant_record['info']
        
        if season.lower() == 'summer':
            # Increase watering frequency
            adjustments['watering'] = {
                'frequency_multiplier': 0.7,  # More frequent watering
                'note': 'Plants need more water in summer heat'
            }
            adjustments['sun_protection'] = {
                'frequency_multiplier': 1.0,
                'note': 'Daily sun protection check needed'
            }
        
        elif season.lower() == 'winter':
            # Decrease watering frequency
            adjustments['watering'] = {
                'frequency_multiplier': 1.5,  # Less frequent watering
                'note': 'Plants need less water in winter'
            }
            adjustments['fertilizing'] = {
                'frequency_multiplier': 2.0,  # Less frequent fertilizing
                'note': 'Plants grow slower in winter'
            }
        
        elif season.lower() == 'monsoon':
            # Adjust for high humidity and rain
            adjustments['watering'] = {
                'frequency_multiplier': 2.0,  # Much less frequent watering
                'note': 'Natural rainfall provides most water needs'
            }
            adjustments['checking'] = {
                'frequency_multiplier': 0.5,  # More frequent health checks
                'note': 'Watch for fungal problems in humid conditions'
            }
        
        return adjustments
```
