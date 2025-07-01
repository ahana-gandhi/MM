import streamlit as st
from generate1 import create_and_compose
import time

# Set page configuration
st.set_page_config(
    page_title="Melody Matrix - Assessment",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #7C4DFF;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(90deg, #7C4DFF, #FF4081);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #424242;
        text-align: center;
        margin-bottom: 2rem;
    }
    .card {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid rgba(124, 77, 255, 0.1);
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(124, 77, 255, 0.15);
    }
    .question-box {
        background-color: rgba(124, 77, 255, 0.05);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border-left: 4px solid #7C4DFF;
    }
    .question-text {
        font-size: 1.2rem;
        color: #424242;
        margin-bottom: 1rem;
        line-height: 1.5;
    }
    .stRadio > label {
        color: #616161;
        font-size: 1.1rem;
    }
    .stRadio > div {
        margin-bottom: 0.5rem;
    }
    .stButton>button {
        background-color: #7C4DFF;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #6A3FD9;
        box-shadow: 0 4px 8px rgba(124, 77, 255, 0.3);
    }
    .result-box {
        background-color: rgba(124, 77, 255, 0.05);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        border: 1px solid rgba(124, 77, 255, 0.2);
    }
    .result-title {
        font-size: 1.5rem;
        color: #7C4DFF;
        margin-bottom: 1rem;
        font-weight: 500;
    }
    .result-text {
        font-size: 1.1rem;
        color: #424242;
        line-height: 1.6;
    }
    .chart-container {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin: 1.5rem 0;
    }
    .instrument-card {
        background-color: #FFFFFF;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid rgba(124, 77, 255, 0.1);
    }
    .instrument-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(124, 77, 255, 0.15);
    }
    .instrument-card.selected {
        background-color: rgba(124, 77, 255, 0.1);
        border: 2px solid #7C4DFF;
        box-shadow: 0 4px 12px rgba(124, 77, 255, 0.2);
    }
    .instrument-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
        color: #7C4DFF;
    }
    .instrument-card.selected .instrument-icon {
        color: #FF4081;
    }
    .instrument-name {
        font-weight: 500;
        color: #424242;
        margin-bottom: 0.5rem;
    }
    .instrument-card.selected .instrument-name {
        color: #7C4DFF;
        font-weight: 600;
    }
    .instrument-description {
        font-size: 0.9rem;
        color: #757575;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'selected_issue' not in st.session_state:
    st.session_state.selected_issue = None
if 'responses' not in st.session_state:
    st.session_state.responses = []
if 'instrument' not in st.session_state:
    st.session_state.instrument = None
if 'speed' not in st.session_state:
    st.session_state.speed = 120
if 'music_ready' not in st.session_state:
    st.session_state.music_ready = False

# Header
st.markdown('<h1 class="main-header">Mental Wellness Assessment</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Answer a few questions to receive your personalized AI-generated music therapy</p>', unsafe_allow_html=True)

# Progress bar
progress = (st.session_state.step - 1) / 3
st.markdown(f"""
<div class="progress-container">
    <div class="progress-bar" style="width: {progress * 100}%;"></div>
</div>
""", unsafe_allow_html=True)

# Step 1: Select Mental Health Issue
if st.session_state.step == 1:
    st.markdown("""
    <div class="content-card">
        <h2>Step 1: Select Your Area of Focus</h2>
        <p>Please select the mental wellness area you'd like to address with personalized music therapy.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Define mental health issues with descriptions
    issues = {
        "Anxiety": "For feelings of nervousness, worry, panic, or restlessness",
        "Depression": "For low mood, sadness, lack of motivation, hopelessness, or fatigue",
        "Relationship": "For challenges in personal or professional relationships",
        "Stress": "For overwhelming pressure or difficulty coping",
        "Sleep Issues": "For difficulty falling asleep, staying asleep, night waking, or insomnia"
    }
    
    # Display issues as cards
    cols = st.columns(len(issues))
    for i, (issue, description) in enumerate(issues.items()):
        with cols[i]:
            st.markdown(f"""
            <div class="instrument-card {'selected' if st.session_state.selected_issue == issue else ''}">
                <div class="instrument-icon">
                    {'😰' if issue == 'Anxiety' else 
                     '😔' if issue == 'Depression' else 
                     '👥' if issue == 'Relationship' else 
                     '😫' if issue == 'Stress' else 
                     '😴'}
                </div>
                <h3>{issue}</h3>
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(issue, key=issue, use_container_width=True):
                st.session_state.selected_issue = issue
                st.session_state.step = 2
                st.rerun()
    
    # Back button
    if st.button("Back to Home", key="back_to_home"):
        st.switch_page("Home.py")

# Step 2: Answer Assessment Questions
elif st.session_state.step == 2:
    st.markdown(f"""
    <div class="content-card">
        <h2>Step 2: Mental Wellness Assessment</h2>
        <p>Please answer the following questions about your experience with {st.session_state.selected_issue.lower()}.</p>
        <p>Your responses will help our AI create music tailored to your specific needs.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Define questions for each category
    questions = {
        "Anxiety": [
            "How strongly do you feel nervous, anxious, or on edge?",
            "How much trouble do you have stopping or controlling your worries?",
            "How much do you worry about various things?",
            "How difficult is it for you to relax?",
            "How strongly do you feel afraid, as if something awful might happen?"
        ],
        "Depression": [
            "Do you feel sad, hopeless, helpless, or worthless?",
            "Do you feel guilty or blame yourself for things in your life?",
            "Have you found it difficult to engage in work, hobbies, or daily activities?",
            "Have you been experiencing trouble sleeping?",
            "Do you feel tense, worried, or anxious about things, even minor matters?"
        ],
        "Relationship": [
            "How supported do you feel by important people in your life?",
            "How often do you experience conflict or tension in your relationships?",
            "How valued or respected do you feel in your relationships?",
            "How comfortable do you feel communicating openly and honestly?",
            "How much distress do your relationship challenges cause you?"
        ],
        "Stress": [
            "How overwhelmed do you feel by your responsibilities or workload?",
            "How difficult is it for you to manage your time and prioritize tasks effectively?",
            "How much has stress affected your physical or mental health?",
            "How difficult is it for you to maintain a work-life balance?",
            "How much distress or frustration does your current level of stress cause you?"
        ],
        "Sleep Issues": [
            "How much difficulty do you have falling asleep?",
            "How often do you wake up during the night?",
            "How refreshed or rested do you feel when you wake up?",
            "How much do your sleep problems interfere with your daily functioning?",
            "How distressed or frustrated are you by your sleep problems?"
        ]
    }
    
    # Display questions with sliders
    responses = []
    for i, question in enumerate(questions.get(st.session_state.selected_issue, [])):
        st.markdown(f"""
        <div class="question-card">
            <p class="slider-label">{question}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Create slider with custom styling
        response = st.slider(
            "", 
            0, 4, 2,
            key=f"q{i}",
            label_visibility="collapsed",
            help="0 = Not at all, 4 = Extremely"
        )
        responses.append(response)
        
        # Add labels below slider
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.markdown("<p style='text-align:center;font-size:0.8rem;'>Not at all</p>", unsafe_allow_html=True)
        with col3:
            st.markdown("<p style='text-align:center;font-size:0.8rem;'>Moderately</p>", unsafe_allow_html=True)
        with col5:
            st.markdown("<p style='text-align:center;font-size:0.8rem;'>Extremely</p>", unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("Back", key="back_to_step1"):
            st.session_state.step = 1
            st.rerun()
    with col3:
        if st.button("Next: Music Preferences", key="next_to_step3"):
            st.session_state.responses = responses
            st.session_state.step = 3
            st.rerun()

# Step 3: Music Preferences
elif st.session_state.step == 3:
    st.markdown("""
    <div class="content-card">
        <h2>Step 3: Customize Your Music</h2>
        <p>Select your preferred instrument and tempo for your personalized therapeutic music.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Instrument selection
    st.markdown("<h3>Choose Your Instrument</h3>", unsafe_allow_html=True)
    instruments = {
        "Piano": "Calming, versatile, and expressive, perfect for deep relaxation and reflection",
        "Guitar": "Warm, soothing, and resonant, great for stress relief and comfort",
        "Violin": "Emotional and expressive, ideal for processing feelings and enhancing mood",
        "Flute": "Light, airy, and delicate, helpful for easing anxiety and tension",
        "Synthesizer": "Modern, ambient, and immersive, good for improved focus"
    }
    
    # Display instruments as cards
    cols = st.columns(len(instruments))
    for i, (instrument, description) in enumerate(instruments.items()):
        with cols[i]:
            is_selected = st.session_state.instrument == instrument
            st.markdown(f"""
            <div class="instrument-card {'selected' if is_selected else ''}">
                <div class="instrument-icon">
                    {'🎹' if instrument == 'Piano' else 
                     '🎸' if instrument == 'Guitar' else 
                     '🎻' if instrument == 'Violin' else 
                     '🪈' if instrument == 'Flute' else 
                     '🎹'}
                </div>
                <div class="instrument-name">{instrument}</div>
                <div class="instrument-description">{description}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(instrument, key=instrument, use_container_width=True):
                st.session_state.instrument = instrument
                st.rerun()
    
    # Tempo selection
    st.markdown("<h3>Select Your Preferred Tempo</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="content-card">
        <p>Slower tempos (60-80 BPM) are ideal for relaxation and sleep.</p>
        <p>Medium tempos (80-120 BPM) are good for stress relief and emotional balance.</p>
        <p>Faster tempos (120-180 BPM) can help with focus and motivation.</p>
    </div>
    """, unsafe_allow_html=True)
    
    tempo = st.slider("Tempo (Beats Per Minute)", 60, 180, st.session_state.speed, 
                     help="60 = Very Slow, 180 = Very Fast")
    st.session_state.speed = tempo
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("Back", key="back_to_step2"):
            st.session_state.step = 2
            st.rerun()
    with col3:
        if st.button("Generate My Music", key="generate_music"):
            if st.session_state.instrument:
                # Create a nice loading experience
                progress_container = col2.container()
                with progress_container:
                    col2.markdown("""
                    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                            border-radius: 15px; color: white; margin: 1rem 0;">
                        <h2 style="margin-bottom: 1rem;">🎵 Creating Your Therapeutic Music</h2>
                        <p style="opacity: 0.9;">Analyzing your preferences and composing your personalized track...</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Progress bar with status
                    progress_bar = col2.progress(0)
                    status_text = col2.empty()
                    
                    steps = [
                        "🎼 Analyzing your mental wellness assessment...",
                        "🎹 Selecting optimal musical elements...",
                        "🎵 Composing with therapeutic frequencies...",
                        "🎶 Fine-tuning tempo and harmony...",
                        "✨ Adding personalized touches...",
                        "🎧 Finalizing your therapeutic track..."
                    ]
                    
                    for i, step in enumerate(steps):
                        status_text.info(step)
                        progress_bar.progress((i + 1) / len(steps))
                        time.sleep(5)
                    
                    # Generate actual music
                    st.session_state.music_ready = create_and_compose(f"30 seconds soothing song using {st.session_state.instrument}")
                    
                    status_text.success("🎉 Your personalized music is ready!")
                    time.sleep(1)
                
                # Clear loading UI
                progress_container.empty()
                
                # Show success and proceed
                st.balloons()
                st.success("🎶 Your therapeutic music has been created! Scroll down to listen.")
                st.session_state.step = 4
                st.rerun()
            else:
                st.error("Please select an instrument before generating music.")

# Step 4: Music Results
elif st.session_state.step == 4:
    st.markdown("""
    <div class="content-card">
        <h2>Your Personalized Therapeutic Music</h2>
        <p>Based on your assessment, we've created a unique musical experience designed to support your mental wellness journey.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display music player
    st.markdown("""
    <div class="content-card">
        <h3>Listen to Your Music</h3>
        <p>Find a quiet space, put on headphones if possible, and take a few deep breaths before listening.</p>
    </div>
    """, unsafe_allow_html=True)
    
    audio_file_path = "composed_track.mp3"  # Path to the generated audio file
    st.audio(audio_file_path)
    
    # Feedback section
    st.markdown("""
    <div class="content-card">
        <h3>How did this music make you feel?</h3>
        <p>Your feedback helps us improve our AI music generation for future sessions.</p>
    </div>
    """, unsafe_allow_html=True)
    
    feedback = st.text_area("Share your experience with this music...", 
                           placeholder="Did it help you relax? Did it match your emotional state? What would you change?")
    
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback! Your input helps us create better therapeutic music experiences.")
        st.session_state.clear()
        st.switch_page("Home.py")
    
    # Option to generate new music
    if st.button("Generate Different Music"):
        st.session_state.step = 3
        st.rerun()
    
    # Back to home
    if st.button("Back to Home"):
        st.session_state.clear()
        st.switch_page("Home.py")

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 1rem; background-color: #F5F5F5; border-radius: 8px;">
    <p style="color: #757575; font-size: 0.9rem;">
        Melody Matrix | AI Music Therapy for Mental Wellness | © 2025
    </p>
</div>
""", unsafe_allow_html=True)