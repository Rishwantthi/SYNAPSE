```
import streamlit as st
import json
from datetime import datetime, timedelta
from plant_identifier import PlantIdentifier
from chatbot import GardeningChatbot
from plant_care_scheduler import PlantCareScheduler
from translate import get_translations
from plant_database import get_plant_database

class HomeGardenerApp:
    def __init__(self, language='English'):
        self.language = language
        self.plant_identifier = PlantIdentifier()
        self.chatbot = GardeningChatbot()
        self.scheduler = PlantCareScheduler()
        self.translations = get_translations()[language]
        
    def run(self):
        st.title(self.translations['gardener_title'])
        st.markdown("### " + self.translations['gardener_subtitle'])
        
        # Single flow: Plant identification and full setup
        self.plant_identification_flow()
    
    def plant_identification_flow(self):
        """Integrated flow for plant identification and setup"""
        
        # Step 1: Plant identification
        st.subheader("🌱 " + self.translations['add_plant'])
        
        # Check if plant is already identified
        if 'identified_plant' not in st.session_state:
            st.session_state.identified_plant = None
        
        if st.session_state.identified_plant is None:
            st.markdown("**" + self.translations['upload_plant_photo'] + "**")
            
            uploaded_file = st.file_uploader(
                self.translations['choose_photo'],
                type=['jpg', 'jpeg', 'png'],
                help=self.translations['photo_help']
            )
            
            if uploaded_file is not None:
                # Display uploaded image
                st.image(uploaded_file, caption=self.translations['uploaded_photo'], use_container_width=True)
                
                # Identify plant button
                if st.button("🔍 " + self.translations['identify_plant'], type="primary"):
                    with st.spinner(self.translations['identifying']):
                        plant_info = self.plant_identifier.identify_plant(uploaded_file)
                        st.session_state.identified_plant = plant_info
                        st.rerun()
                        
            # Option to add plant manually
            st.markdown("---")
            st.markdown("**" + self.translations['or_add_manually'] + "**")
            if st.button("✏️ " + self.translations['add_manually']):
                st.session_state.identified_plant = {"manual_entry": True}
                st.rerun()
        
        else:
            # Step 2: Plant setup after identification
            plant_info = st.session_state.identified_plant
            
            if plant_info.get("manual_entry"):
                self.manual_plant_entry()
            else:
                self.plant_care_setup(plant_info)
    
    def manual_plant_entry(self):
        """Manual plant entry form"""
        st.subheader("✏️ " + self.translations['add_manually'])
        
        with st.form("manual_plant_form"):
            plant_name = st.text_input(self.translations['plant_name'], placeholder=self.translations['plant_name_placeholder'])
            plant_type = st.selectbox(
                self.translations['plant_type'],
                ["Flowering", "Foliage", "Succulent", "Herb", "Vegetable", "Fruit", "Tree", "Other"]
            )
            
            difficulty = st.selectbox(
                self.translations['difficulty_level'],
                ["Easy", "Medium", "Hard"]
            )
            
            indoor_suitable = st.checkbox(self.translations['indoor_suitable'], value=True)
            
            submitted = st.form_submit_button(self.translations['add_plant_btn'])
            
            if submitted and plant_name:
                # Create plant info structure
                plant_info = {
                    "plant_name": plant_name,
                    "plant_type": plant_type,
                    "difficulty_level": difficulty.lower(),
                    "indoor_suitable": indoor_suitable,
                    "care_requirements": {
                        "light": "medium",
                        "water": "every 2-3 days",
                        "humidity": "medium",
                        "temperature": "18-25°C",
                        "soil_type": "well-draining"
                    },
                    "growing_tips": ["Monitor plant regularly", "Adjust care based on season"],
                    "common_problems": ["Over-watering", "Under-lighting"],
                    "suitable_locations": ["balcony", "terrace", "garden"],
                    "seasonal_care": {
                        "spring": "Regular watering and fertilizing",
                        "summer": "Increase watering frequency",
                        "monsoon": "Reduce watering, ensure drainage",
                        "winter": "Reduce watering, protect from cold"
                    }
                }
                
                st.session_state.identified_plant = plant_info
                st.rerun()
    
    def plant_care_setup(self, plant_info):
        """Integrated plant care setup after identification"""
        
        # Display identified plant
        st.success("🌿 " + self.translations['plant_identified'])
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown(f"**{self.translations['plant_name']}:** {plant_info['plant_name']}")
            if 'scientific_name' in plant_info:
                st.markdown(f"**{self.translations['scientific_name']}:** {plant_info['scientific_name']}")
            st.markdown(f"**{self.translations['plant_type']}:** {plant_info.get('plant_type', 'Unknown')}")
            st.markdown(f"**{self.translations['difficulty_level']}:** {plant_info.get('difficulty_level', 'medium').title()}")
            
            # Display any API quota note
            if 'note' in plant_info:
                st.info(plant_info['note'])
        
        with col2:
            # Care requirements
            st.markdown(f"**{self.translations['care_requirements']}:**")
            care_req = plant_info.get('care_requirements', {})
            st.markdown(f"💡 **{self.translations['light']}:** {care_req.get('light', 'medium')}")
            st.markdown(f"💧 **{self.translations['water']}:** {care_req.get('water', 'regular')}")
            st.markdown(f"🌡️ **{self.translations['temperature']}:** {care_req.get('temperature', '18-25°C')}")
        
        # Step 3: Care setup form
        st.markdown("---")
        st.subheader("📅 " + self.translations['setup_care'])
        
        with st.form("care_setup_form"):
            # Care start date
            care_start_date = st.date_input(
                "📆 " + self.translations['care_start_date'],
                value=datetime.now().date(),
                help=self.translations['care_start_help']
            )
            
            # Plant location
            location_options = ["balcony", "terrace", "garden", "kitchen", "living_room", "bedroom", "bathroom", "outdoor"]
            location = st.selectbox(
                "🏡 " + self.translations['plant_location'],
                location_options,
                help=self.translations['location_help']
            )
            
            # Custom plant nickname
            plant_nickname = st.text_input(
                "🏷️ " + self.translations['plant_nickname'],
                value=plant_info['plant_name'],
                help=self.translations['nickname_help']
            )
            
            setup_submitted = st.form_submit_button("✅ " + self.translations['setup_plant'], type="primary")
            
            if setup_submitted:
                # Create complete plant record
                plant_record = {
                    "id": len(st.session_state.user_plants) + 1,
                    "nickname": plant_nickname,
                    "info": plant_info,
                    "location": location,
                    "care_start_date": care_start_date,
                    "added_date": datetime.now().date(),
                    "last_watered": None,
                    "last_fertilized": None,
                    "health_score": 100
                }
                
                # Add to user plants
                st.session_state.user_plants.append(plant_record)
                
                # Create care schedule
                care_schedule = self.scheduler.create_care_schedule(plant_record)
                st.session_state.care_schedule[plant_record['id']] = care_schedule
                
                st.success("🎉 " + self.translations['plant_added_success'])
                st.session_state.current_plant = plant_record
                st.session_state.show_care_features = True
                st.rerun()
        
        # Step 4: Show care features after setup
        if hasattr(st.session_state, 'show_care_features') and st.session_state.show_care_features:
            self.show_integrated_care_features()
    
    def show_integrated_care_features(self):
        """Show all care features integrated in one flow"""
        
        current_plant = st.session_state.current_plant
        
        st.markdown("---")
        st.subheader("🌱 " + self.translations['your_plant_care'])
        
        # Plant mood and status
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Plant mood
            mood = self.plant_identifier.get_plant_mood(
                current_plant['nickname'],
                current_plant.get('last_watered'),
                current_plant['info']['care_requirements'].get('water', 'every 2-3 days')
            )
            st.markdown(f"**🌿 {self.translations['plant_mood']}:** {mood}")
            
        with col2:
            # Health score
            health_score = current_plant.get('health_score', 100)
            st.markdown(f"**💚 {self.translations['health_score']}:** {health_score}%")
            
        with col3:
            # Days since added
            days_added = (datetime.now().date() - current_plant['added_date']).days
            st.markdown(f"**📅 {self.translations['days_with_you']}:** {days_added} days")
        
        # Daily care instructions
        st.markdown("---")
        st.subheader("📋 " + self.translations['daily_instructions'])
        
        # Get today's tasks
        today_tasks = self.scheduler.get_daily_tasks(current_plant, datetime.now().date())
        
        if today_tasks:
            st.markdown("**" + self.translations['today_tasks'] + ":**")
            for task in today_tasks:
                task_col1, task_col2 = st.columns([3, 1])
                with task_col1:
                    priority_emoji = "🔴" if task['priority'] == 'high' else "🟡" if task['priority'] == 'medium' else "🟢"
                    st.markdown(f"{priority_emoji} {task['task']} - {task['description']}")
                with task_col2:
                    if st.button(f"✅ Done", key=f"complete_{task['type']}"):
                        self.mark_task_complete(task)
                        st.rerun()
        else:
            st.info("✨ " + self.translations['no_tasks_today'])
        
        # Care reminders
        st.markdown("---")
        st.subheader("⏰ " + self.translations['care_reminders'])
        
        reminders = self.scheduler.get_care_reminders(current_plant)
        for reminder in reminders:
            st.info(f"💡 {reminder}")
        
        # Growing tips
        st.markdown("---")
        st.subheader("🌱 " + self.translations['growing_tips'])
        
        tips = current_plant['info'].get('growing_tips', [])
        for tip in tips:
            st.markdown(f"• {tip}")
        
        # Quick care actions
        st.markdown("---")
        st.subheader("⚡ " + self.translations['quick_actions'])
        
        quick_col1, quick_col2, quick_col3 = st.columns(3)
        
        with quick_col1:
            if st.button("💧 " + self.translations['water_now']):
                current_plant['last_watered'] = datetime.now().date()
                st.success("💧 " + self.translations['watered_success'])
                st.rerun()
        
        with quick_col2:
            if st.button("🌱 " + self.translations['fertilize_now']):
                current_plant['last_fertilized'] = datetime.now().date()
                st.success("🌱 " + self.translations['fertilized_success'])
                st.rerun()
        
        with quick_col3:
            if st.button("📝 " + self.translations['add_note']):
                st.session_state.show_note_input = True
                st.rerun()
        
        # Note input
        if hasattr(st.session_state, 'show_note_input') and st.session_state.show_note_input:
            note = st.text_area(self.translations['plant_note'], placeholder=self.translations['note_placeholder'])
            if st.button(self.translations['save_note']):
                if 'notes' not in current_plant:
                    current_plant['notes'] = []
                current_plant['notes'].append({
                    'date': datetime.now().date(),
                    'note': note
                })
                st.success(self.translations['note_saved'])
                st.session_state.show_note_input = False
                st.rerun()
        
        # Ask gardening questions
        st.markdown("---")
        st.subheader("💬 " + self.translations['ask_question'])
        
        question = st.text_input(
            self.translations['your_question'],
            placeholder=self.translations['question_placeholder']
        )
        
        if st.button("🤔 " + self.translations['ask_expert']):
            if question:
                with st.spinner(self.translations['thinking']):
                    response = self.chatbot.get_response(question, [current_plant])
                    st.markdown("**" + self.translations['expert_says'] + ":**")
                    st.markdown(response)
            else:
                st.warning(self.translations['enter_question'])
        
        # Start over button
        st.markdown("---")
        if st.button("🔄 " + self.translations['add_another_plant']):
            st.session_state.identified_plant = None
            st.session_state.show_care_features = False
            del st.session_state.current_plant
            st.rerun()
    
    def mark_task_complete(self, task):
        """Mark a task as complete"""
        # This method is called from the integrated care features
        current_plant = st.session_state.current_plant
        
        # Update plant record
        if task['type'] == 'water':
            current_plant['last_watered'] = datetime.now().date()
        elif task['type'] == 'fertilize':
            current_plant['last_fertilized'] = datetime.now().date()
        
        # Update care schedule
        self.scheduler.mark_task_complete(
            current_plant['id'], 
            task['type'], 
            datetime.now().date()
        )
        
        st.success(f"✅ {task['task']} completed!")
    
    # Legacy methods - kept for compatibility but not used in new flow
    def add_plant_tab(self):
        st.header("🌱 " + self.translations['add_new_plant'])
        
        # Method selection
        method = st.radio(
            self.translations['how_add_plant'],
            [self.translations['upload_photo'], self.translations['select_from_list'], self.translations['enter_manually']]
        )
        
        if method == self.translations['upload_photo']:
            self.add_plant_by_photo()
        elif method == self.translations['select_from_list']:
            self.add_plant_from_list()
        else:
            self.add_plant_manually()
    
    def add_plant_by_photo(self):
        uploaded_file = st.file_uploader(
            self.translations['upload_plant_photo'],
            type=['png', 'jpg', 'jpeg'],
            help=self.translations['photo_help']
        )
        
        if uploaded_file is not None:
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(uploaded_file, caption=self.translations['uploaded_photo'], use_column_width=True)
            
            with col2:
                if st.button(self.translations['identify_plant']):
                    with st.spinner(self.translations['identifying']):
                        plant_info = self.plant_identifier.identify_plant(uploaded_file)
                        
                        if 'error' not in plant_info:
                            st.success(f"{self.translations['identified_as']}: **{plant_info['plant_name']}**")
                            st.write(f"**{self.translations['scientific_name']}**: {plant_info['scientific_name']}")
                            st.write(f"**{self.translations['plant_type']}**: {plant_info['plant_type']}")
                            st.write(f"**{self.translations['difficulty']}**: {plant_info['difficulty_level']}")
                            
                            # Ask if user wants to add this plant
                            if st.button(self.translations['add_this_plant']):
                                self.register_plant(plant_info)
                        else:
                            st.error(plant_info['error'])
    
    def add_plant_from_list(self):
        plant_db = get_plant_database()
        
        # Category filter
        categories = list(set(plant['plant_type'] for plant in plant_db))
        selected_category = st.selectbox(
            self.translations['select_category'],
            [self.translations['all_categories']] + categories
        )
        
        # Filter plants by category
        if selected_category != self.translations['all_categories']:
            filtered_plants = [p for p in plant_db if p['plant_type'] == selected_category]
        else:
            filtered_plants = plant_db
        
        # Plant selection
        plant_names = [plant['plant_name'] for plant in filtered_plants]
        selected_plant_name = st.selectbox(
            self.translations['select_plant'],
            plant_names
        )
        
        if selected_plant_name:
            plant_info = next(p for p in filtered_plants if p['plant_name'] == selected_plant_name)
            
            # Display plant information
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**{self.translations['scientific_name']}**: {plant_info['scientific_name']}")
                st.write(f"**{self.translations['plant_type']}**: {plant_info['plant_type']}")
                st.write(f"**{self.translations['difficulty']}**: {plant_info['difficulty_level']}")
                st.write(f"**{self.translations['indoor_suitable']}**: {self.translations['yes'] if plant_info['indoor_suitable'] else self.translations['no']}")
            
            with col2:
                st.write(f"**{self.translations['light_needs']}**: {plant_info['care_requirements']['light']}")
                st.write(f"**{self.translations['water_needs']}**: {plant_info['care_requirements']['water']}")
                st.write(f"**{self.translations['humidity_needs']}**: {plant_info['care_requirements']['humidity']}")
                st.write(f"**{self.translations['temperature_range']}**: {plant_info['care_requirements']['temperature']}")
            
            if st.button(self.translations['add_this_plant']):
                self.register_plant(plant_info)
    
    def add_plant_manually(self):
        with st.form("manual_plant_form"):
            plant_name = st.text_input(self.translations['plant_name'])
            plant_type = st.selectbox(
                self.translations['plant_type'],
                ['Herb', 'Shrub', 'Tree', 'Flowering Plant', 'Vegetable', 'Fruit', 'Succulent', 'Other']
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
                light_needs = st.selectbox(self.translations['light_needs'], ['Low', 'Medium', 'High', 'Bright Indirect'])
                water_frequency = st.selectbox(self.translations['water_frequency'], ['Daily', 'Every 2-3 days', 'Weekly', 'When dry'])
                
            with col2:
                humidity = st.selectbox(self.translations['humidity_needs'], ['Low', 'Medium', 'High'])
                difficulty = st.selectbox(self.translations['difficulty'], ['Beginner', 'Intermediate', 'Advanced'])
            
            submitted = st.form_submit_button(self.translations['add_plant'])
            
            if submitted and plant_name:
                plant_info = {
                    'plant_name': plant_name,
                    'scientific_name': 'Unknown',
                    'plant_type': plant_type,
                    'difficulty_level': difficulty.lower(),
                    'indoor_suitable': True,
                    'care_requirements': {
                        'light': light_needs.lower(),
                        'water': water_frequency.lower(),
                        'humidity': humidity.lower(),
                        'temperature': '18-25°C',
                        'soil_type': 'well-draining'
                    },
                    'growing_tips': ['Monitor regularly', 'Adjust care based on season'],
                    'suitable_locations': ['balcony', 'terrace'],
                    'budget_estimate': 'medium'
                }
                self.register_plant(plant_info)
    
    def register_plant(self, plant_info):
        st.subheader(self.translations['plant_details'])
        
        with st.form("register_plant_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                custom_name = st.text_input(
                    self.translations['custom_plant_name'],
                    value=plant_info['plant_name'],
                    help=self.translations['custom_name_help']
                )
                
                location = st.selectbox(
                    self.translations['plant_location'],
                    ['Balcony', 'Terrace', 'Kitchen', 'Living Room', 'Garden', 'Bedroom', 'Office', 'Other']
                )
                
                care_start_date = st.date_input(
                    self.translations['care_start_date'],
                    value=datetime.now().date()
                )
            
            with col2:
                budget = st.selectbox(
                    self.translations['budget_range'],
                    ['Low (₹100-500)', 'Medium (₹500-2000)', 'High (₹2000+)']
                )
                
                notifications = st.checkbox(
                    self.translations['enable_notifications'],
                    value=True
                )
                
                notes = st.text_area(
                    self.translations['additional_notes'],
                    placeholder=self.translations['notes_placeholder']
                )
            
            if st.form_submit_button(self.translations['register_plant']):
                # Create plant record
                plant_record = {
                    'id': len(st.session_state.user_plants) + 1,
                    'custom_name': custom_name,
                    'plant_info': plant_info,
                    'location': location,
                    'care_start_date': care_start_date.isoformat(),
                    'budget': budget,
                    'notifications': notifications,
                    'notes': notes,
                    'last_care_date': datetime.now().date().isoformat(),
                    'care_history': []
                }
                
                # Add to session state
                st.session_state.user_plants.append(plant_record)
                
                # Create care schedule
                self.scheduler.create_care_schedule(plant_record)
                
                st.success(f"{self.translations['plant_added_success']}: {custom_name}")
                st.rerun()
    
    def care_schedule_tab(self):
        st.header("📅 " + self.translations['care_schedule'])
        
        if not st.session_state.user_plants:
            st.info(self.translations['no_plants_added'])
            return
        
        # Today's care tasks
        today = datetime.now().date()
        st.subheader(self.translations['todays_tasks'])
        
        todays_tasks = []
        for plant in st.session_state.user_plants:
            tasks = self.scheduler.get_daily_tasks(plant, today)
            if tasks:
                todays_tasks.extend(tasks)
        
        if todays_tasks:
            for task in todays_tasks:
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    st.write(f"🌱 **{task['plant_name']}** - {task['task']}")
                    st.caption(task['description'])
                
                with col2:
                    if st.button(self.translations['mark_done'], key=f"done_{task['id']}"):
                        self.mark_task_complete(task)
                
                with col3:
                    if st.button(self.translations['skip'], key=f"skip_{task['id']}"):
                        self.skip_task(task)
        else:
            st.info(self.translations['no_tasks_today'])
        
        # Weekly overview
        st.subheader(self.translations['weekly_overview'])
        
        week_start = today - timedelta(days=today.weekday())
        week_days = [week_start + timedelta(days=i) for i in range(7)]
        
        for day in week_days:
            with st.expander(f"{day.strftime('%A, %B %d')} {'📅' if day == today else ''}"):
                daily_tasks = []
                for plant in st.session_state.user_plants:
                    tasks = self.scheduler.get_daily_tasks(plant, day)
                    if tasks:
                        daily_tasks.extend(tasks)
                
                if daily_tasks:
                    for task in daily_tasks:
                        st.write(f"• {task['plant_name']}: {task['task']}")
                else:
                    st.write(self.translations['no_tasks_this_day'])
    
    def my_plants_tab(self):
        st.header("🌿 " + self.translations['my_plants'])
        
        if not st.session_state.user_plants:
            st.info(self.translations['no_plants_added'])
            return
        
        # Plant overview cards
        for plant in st.session_state.user_plants:
            with st.expander(f"🌱 {plant['custom_name']} ({plant['plant_info']['plant_name']})", expanded=False):
                col1, col2, col3 = st.columns([2, 2, 1])
                
                with col1:
                    st.write(f"**{self.translations['location']}**: {plant['location']}")
                    st.write(f"**{self.translations['added_on']}**: {plant['care_start_date']}")
                    st.write(f"**{self.translations['difficulty']}**: {plant['plant_info']['difficulty_level']}")
                    st.write(f"**{self.translations['budget']}**: {plant['budget']}")
                
                with col2:
                    # Plant mood
                    mood_info = self.plant_identifier.get_plant_mood(
                        plant['plant_info']['plant_name'],
                        plant['last_care_date'],
                        plant['plant_info']['care_requirements']['water']
                    )
                    
                    st.write(f"**{self.translations['plant_mood']}**: {mood_info['mood']} {mood_info['status']}")
                    st.caption(mood_info['message'])
                    
                    # Care requirements
                    care_req = plant['plant_info']['care_requirements']
                    st.write(f"**{self.translations['water_needs']}**: {care_req['water']}")
                    st.write(f"**{self.translations['light_needs']}**: {care_req['light']}")
                
                with col3:
                    if st.button(self.translations['care_now'], key=f"care_{plant['id']}"):
                        self.quick_care_action(plant)
                    
                    if st.button(self.translations['edit_plant'], key=f"edit_{plant['id']}"):
                        self.edit_plant(plant)
                    
                    if st.button(self.translations['remove_plant'], key=f"remove_{plant['id']}"):
                        self.remove_plant(plant)
                
                # Care tips
                if plant['plant_info']['growing_tips']:
                    st.markdown(f"**{self.translations['growing_tips']}**")
                    for tip in plant['plant_info']['growing_tips'][:3]:
                        st.write(f"• {tip}")
                
                # Notes
                if plant['notes']:
                    st.markdown(f"**{self.translations['notes']}**: {plant['notes']}")
    
    def chatbot_tab(self):
        st.header("💬 " + self.translations['ask_expert'])
        st.write(self.translations['chatbot_description'])
        
        # Chat history
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        # Display chat history
        for message in st.session_state.chat_history:
            if message['role'] == 'user':
                st.write(f"**{self.translations['you']}**: {message['content']}")
            else:
                st.write(f"**{self.translations['expert']}**: {message['content']}")
        
        # Chat input
        user_question = st.text_input(
            self.translations['ask_question'],
            placeholder=self.translations['question_placeholder']
        )
        
        if st.button(self.translations['send_question']) and user_question:
            # Add user message to history
            st.session_state.chat_history.append({
                'role': 'user',
                'content': user_question
            })
            
            # Get bot response
            with st.spinner(self.translations['thinking']):
                response = self.chatbot.get_response(user_question, st.session_state.user_plants)
                
                # Add bot response to history
                st.session_state.chat_history.append({
                    'role': 'assistant',
                    'content': response
                })
            
            st.rerun()
        
        # Quick question buttons
        st.subheader(self.translations['quick_questions'])
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(self.translations['watering_tips']):
                self.ask_quick_question(self.translations['watering_tips_question'])
            
            if st.button(self.translations['pest_problems']):
                self.ask_quick_question(self.translations['pest_problems_question'])
        
        with col2:
            if st.button(self.translations['fertilizer_advice']):
                self.ask_quick_question(self.translations['fertilizer_advice_question'])
            
            if st.button(self.translations['seasonal_care']):
                self.ask_quick_question(self.translations['seasonal_care_question'])
    
    def plant_guide_tab(self):
        st.header("📚 " + self.translations['plant_guide'])
        
        # Search functionality
        search_term = st.text_input(self.translations['search_plants'])
        
        plant_db = get_plant_database()
        
        if search_term:
            filtered_plants = [
                p for p in plant_db 
                if search_term.lower() in p['plant_name'].lower() or 
                   search_term.lower() in p['plant_type'].lower()
            ]
        else:
            filtered_plants = plant_db[:10]  # Show first 10 plants by default
        
        if filtered_plants:
            for plant in filtered_plants:
                with st.expander(f"🌱 {plant['plant_name']} ({plant['scientific_name']})"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write(f"**{self.translations['plant_type']}**: {plant['plant_type']}")
                        st.write(f"**{self.translations['difficulty']}**: {plant['difficulty_level']}")
                        st.write(f"**{self.translations['indoor_suitable']}**: {self.translations['yes'] if plant['indoor_suitable'] else self.translations['no']}")
                        st.write(f"**{self.translations['budget_estimate']}**: {plant['budget_estimate']}")
                    
                    with col2:
                        care_req = plant['care_requirements']
                        st.write(f"**{self.translations['light_needs']}**: {care_req['light']}")
                        st.write(f"**{self.translations['water_needs']}**: {care_req['water']}")
                        st.write(f"**{self.translations['humidity_needs']}**: {care_req['humidity']}")
                        st.write(f"**{self.translations['temperature_range']}**: {care_req['temperature']}")
                    
                    if plant['growing_tips']:
                        st.markdown(f"**{self.translations['growing_tips']}**:")
                        for tip in plant['growing_tips'][:3]:
                            st.write(f"• {tip}")
                    
                    if st.button(self.translations['add_this_plant'], key=f"guide_add_{plant['plant_name']}"):
                        self.register_plant(plant)
        else:
            st.info(self.translations['no_plants_found'])
    
    def mark_task_complete(self, task):
        # Update last care date for the plant
        for plant in st.session_state.user_plants:
            if plant['id'] == task['plant_id']:
                plant['last_care_date'] = datetime.now().date().isoformat()
                plant['care_history'].append({
                    'date': datetime.now().isoformat(),
                    'task': task['task'],
                    'status': 'completed'
                })
                break
        
        st.success(f"{self.translations['task_completed']}: {task['task']}")
        st.rerun()
    
    def skip_task(self, task):
        # Add to care history as skipped
        for plant in st.session_state.user_plants:
            if plant['id'] == task['plant_id']:
                plant['care_history'].append({
                    'date': datetime.now().isoformat(),
                    'task': task['task'],
                    'status': 'skipped'
                })
                break
        
        st.info(f"{self.translations['task_skipped']}: {task['task']}")
        st.rerun()
    
    def quick_care_action(self, plant):
        st.success(f"{self.translations['quick_care_done']}: {plant['custom_name']}")
        plant['last_care_date'] = datetime.now().date().isoformat()
        st.rerun()
    
    def edit_plant(self, plant):
        # This would open an edit form - simplified for now
        st.info(f"{self.translations['edit_feature_coming']}: {plant['custom_name']}")
    
    def remove_plant(self, plant):
        if st.button(f"{self.translations['confirm_remove']}: {plant['custom_name']}?", key=f"confirm_remove_{plant['id']}"):
            st.session_state.user_plants = [p for p in st.session_state.user_plants if p['id'] != plant['id']]
            st.success(f"{self.translations['plant_removed']}: {plant['custom_name']}")
            st.rerun()
    
    def ask_quick_question(self, question):
        st.session_state.chat_history.append({
            'role': 'user',
            'content': question
        })
        
        response = self.chatbot.get_response(question, st.session_state.user_plants)
        
        st.session_state.chat_history.append({
            'role': 'assistant',
            'content': response
        })
        
        st.rerun()
```
