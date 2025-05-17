import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Melody Matrix - AI Music Creator for Mental Wellness",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #7C4DFF;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(90deg, #7C4DFF, #FF4081);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .sub-header {
        font-size: 1.5rem;
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
    .card-title {
        font-size: 1.5rem;
        font-weight: 500;
        color: #7C4DFF;
        margin-bottom: 0.5rem;
    }
    .card-description {
        font-size: 1rem;
        color: #616161;
        margin-bottom: 1rem;
        line-height: 1.5;
    }
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        color: #7C4DFF;
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
    .intro-box {
        padding: 1.5rem;
        background-color: rgba(124, 77, 255, 0.05);
        border-radius: 12px;
        border-left: 4px solid #7C4DFF;
        margin-bottom: 2rem;
    }
    .intro-text {
        font-size: 1.2rem;
        line-height: 1.6;
        color: #424242;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1.5rem;
        background-color: rgba(124, 77, 255, 0.05);
        border-radius: 12px;
        color: #757575;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown('<h1 class="main-header">Melody Matrix</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered Music Therapy for Mental Wellness</p>', unsafe_allow_html=True)

# Logo and introduction
col1, col2 = st.columns([1, 2])
with col1:
    st.image("MM.png", width=200)
with col2:
    st.markdown("""
    <div class="intro-box">
        <p class="intro-text">
            Welcome to Melody Matrix, where AI meets mental wellness through personalized music therapy. 
            Our platform creates custom soundscapes designed to help you manage stress, anxiety, and emotional challenges.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Feature cards
st.markdown("## How Melody Matrix Can Help You")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="feature-icon">🧠</div>
        <div class="card-title">Personalized Assessment</div>
        <div class="card-description">
            Our AI analyzes your mental wellness needs through a simple questionnaire to create music tailored to your emotional state.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="feature-icon">🎵</div>
        <div class="card-title">AI-Generated Music</div>
        <div class="card-description">
            Experience unique soundscapes created specifically for your emotional needs, using advanced AI music generation technology.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="feature-icon">💆</div>
        <div class="card-title">Therapeutic Benefits</div>
        <div class="card-description">
            Reduce stress, improve mood, enhance focus, and promote relaxation through scientifically designed musical experiences.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Call to action sections
st.markdown("## Get Started with Melody Matrix")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">Begin Your Musical Journey</div>
        <div class="card-description">
            Take our mental wellness assessment and receive personalized AI-generated music to support your emotional well-being.
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Assessment", key="start_assessment"):
        st.switch_page("pages/1_Tools.py")

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">Learn More About Us</div>
        <div class="card-description">
            Discover the science behind music therapy and how Melody Matrix is revolutionizing mental wellness support.
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("About Melody Matrix", key="about"):
        st.switch_page("pages/2_About_Me.py")

# Footer
st.markdown("""
<div class="footer">
    <p>
        Melody Matrix | AI Music Therapy for Mental Wellness | © 2025
    </p>
</div>
""", unsafe_allow_html=True)
