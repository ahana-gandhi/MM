import streamlit as st

st.set_page_config(
    page_title="Melody Matrix - AI Music Creator for Mental Wellness",
    page_icon="🎵",
    layout="wide"
)
col = st.columns([3, 2, 4, 3])
col[1].image("MM.png", width=250)

col[2].markdown("""
    <div style="text-align:center;">
        <h1>Melody Matrix</h1>
        
    </div>
""", unsafe_allow_html=True)


def render_section(title, description, button_text, page):
    st.markdown(f"""
        <div style="background-color:#b0e0e6; padding:20px; border-radius:10px; margin-bottom:20px; text-align:center;">
            <h3>{title}</h3>
            <p>{description}</p>
    """, unsafe_allow_html=True)


    button_placeholder = st.empty()
    if button_placeholder.button(button_text, key=title):
        st.switch_page(f"pages/{page}.py")

    st.markdown("</div>", unsafe_allow_html=True)

# Render Sections with Functional Buttons
render_section("About", "Melody Matrix is designed to enhance mental wellness through personalized AI-generated music.", "About Me", "2_About_Me")
render_section("How it Works", "Answer a few mental wellness questions, customize music preferences, and generate music tailored for relaxation and healing.", "Start Assessment", "1_Tool_Page")
render_section("Why Melody Matrix?", "Our AI-driven approach helps create a unique musical journey designed for your emotional well-being.", "Learn More", "2_About_Me")
