import streamlit as st
from generate1 import generate_music

st.set_page_config(page_title="Tool Page", page_icon="🛠️")

st.header("Mental Health & Music Assessment Tool")

# Define mental health issues
issues = ["Anxiety", "Depression", "Relationship Issues", "Stress", "Sleep Issues"]
selected_issue = st.radio("Select an area of focus:", issues)

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
    "Relationship Issues": [
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

# Start assessment button
if st.button("Start Assessment"):
    st.session_state.selected_issue = selected_issue

# Show assessment questions if a category is selected
if st.session_state.get("selected_issue"):
    st.subheader(f"{st.session_state.selected_issue} Assessment")
    responses = [st.slider(q, 0, 4, 2) for q in questions.get(st.session_state.selected_issue, [])]

    if st.button("Next: Music Preferences"):
        st.session_state["responses"] = responses

# Show music preferences
if st.session_state.get("responses"):
    st.header("Music Preferences")
    instrument = st.selectbox("Choose an instrument:", ["Piano", "Guitar", "Violin", "Flute", "Synthesizer"])
    speed = st.slider("Select music speed:", 60, 180, 120)

    if st.button("Finalize"):
        st.session_state["instrument"] = instrument
        st.session_state["speed"] = speed
        st.session_state["music_ready"] = generate_music(instrument, speed)

# Show dummy music and feedback form after submission
if st.session_state.get("music_ready"):
    st.subheader("Here is your generated music 🎵 (Placeholder)")
    audio_file_path = "musicgen_out2.wav"  # Replace with actual file path if needed
    st.audio(audio_file_path)

    st.subheader("Feedback")
    st.write("How did you feel about the generated music?")
    feedback = st.text_area("Your thoughts...")

    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback! 🎶")
        st.session_state.clear()
