import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="About Melody Matrix",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #6200EE;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #E0E0E0;
    }
    .content-card {
        background-color: #FFFFFF;
        border-radius: 8px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
    }
    .highlight-text {
        color: #6200EE;
        font-weight: 500;
    }
    .quote-box {
        background-color: #F5F5F5;
        border-left: 4px solid #6200EE;
        padding: 1rem;
        margin: 1rem 0;
        font-style: italic;
    }
    .team-member {
        text-align: center;
        margin-bottom: 1rem;
    }
    .team-member img {
        border-radius: 50%;
        width: 120px;
        height: 120px;
        object-fit: cover;
        margin-bottom: 0.5rem;
    }
    .back-button {
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="section-header">About Melody Matrix</h1>', unsafe_allow_html=True)

# Introduction
st.markdown("""
<div class="content-card">
    <h2>Our Mission</h2>
    <p>
        Melody Matrix was created from a passion for both music and mental health awareness. Our mission is to provide 
        accessible, personalized music therapy experiences to help individuals manage stress, anxiety, and emotional well-being 
        through the power of AI-generated music.
    </p>
    <div class="quote-box">
        "Music can heal the wounds which medicine cannot touch." - Debasish Mridha, MD
    </div>
</div>
""", unsafe_allow_html=True)

# The Science Behind Music Therapy
st.markdown("""
<div class="content-card">
    <h2>The Science Behind Music Therapy</h2>
    <p>
        Music therapy is a well-established clinical intervention that uses music to address physical, emotional, cognitive, 
        and social needs. Research has shown that music can:
    </p>
    <ul>
        <li>Reduce stress and anxiety by lowering cortisol levels</li>
        <li>Improve mood by increasing dopamine and serotonin production</li>
        <li>Enhance focus and concentration</li>
        <li>Promote better sleep quality</li>
        <li>Support emotional processing and expression</li>
    </ul>
    <p>
        At Melody Matrix, we combine these proven benefits with cutting-edge AI technology to create personalized 
        musical experiences that adapt to your specific emotional needs.
    </p>
</div>
""", unsafe_allow_html=True)

# How Our AI Works
st.markdown("""
<div class="content-card">
    <h2>How Our AI Music Generation Works</h2>
    <p>
        Our platform uses advanced AI models trained on millions of musical compositions to generate unique soundscapes 
        tailored to your emotional state. The process involves:
    </p>
    <ol>
        <li><span class="highlight-text">Assessment:</span> Understanding your current emotional state through our questionnaire</li>
        <li><span class="highlight-text">Analysis:</span> Processing your responses to determine the most beneficial musical elements</li>
        <li><span class="highlight-text">Generation:</span> Creating a unique musical composition with tempo, instruments, and mood optimized for your needs</li>
        <li><span class="highlight-text">Delivery:</span> Providing you with a personalized audio experience you can listen to anytime</li>
    </ol>
    <p>
        The AI considers factors such as tempo, rhythm, harmony, and instrumentation to create music that promotes 
        relaxation, focus, or emotional processing depending on your needs.
    </p>
</div>
""", unsafe_allow_html=True)

# Our Team
st.markdown("""
<div class="content-card">
    <h2>Our Team</h2>
    <p>
        Melody Matrix was founded by a team of music therapists, AI researchers, and mental health professionals 
        dedicated to making therapeutic music accessible to everyone.
    </p>
    <div class="row">
        <div class="col-md-4">
            <div class="team-member">
                <img src="https://randomuser.me/api/portraits/women/44.jpg" alt="Team Member">
                <h3>Dr. Sarah Chen</h3>
                <p>Music Therapist & Founder</p>
            </div>
        </div>
        <div class="col-md-4">
            <div class="team-member">
                <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="Team Member">
                <h3>Dr. James Rodriguez</h3>
                <p>AI Research Director</p>
            </div>
        </div>
        <div class="col-md-4">
            <div class="team-member">
                <img src="https://randomuser.me/api/portraits/women/68.jpg" alt="Team Member">
                <h3>Dr. Priya Patel</h3>
                <p>Clinical Psychologist</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Contact Information
st.markdown("""
<div class="content-card">
    <h2>Contact Us</h2>
    <p>
        We'd love to hear from you! Whether you have questions about our technology, feedback on your experience, 
        or ideas for improvement, our team is here to help.
    </p>
    <p>
        <strong>Email:</strong> support@melodymatrix.com<br>
        <strong>Phone:</strong> (555) 123-4567<br>
        <strong>Address:</strong> 123 Wellness Way, San Francisco, CA 94105
    </p>
</div>
""", unsafe_allow_html=True)

# Back to Home button
if st.button("Back to Home", key="back_to_home"):
    st.switch_page("Home.py")

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 1rem; background-color: #F5F5F5; border-radius: 8px;">
    <p style="color: #757575; font-size: 0.9rem;">
        Melody Matrix | AI Music Therapy for Mental Wellness | © 2025
    </p>
</div>
""", unsafe_allow_html=True)