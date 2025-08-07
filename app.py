import streamlit as st

st.set_page_config(page_title="AI Health Assistant", layout="centered")

st.title("🩺 AI Health Assistant")
st.markdown("Hi there! 👋 I'm your AI health buddy.\n\nTell me how you're feeling today.")

user_input = st.text_area("Describe your symptoms here:")

if user_input:
    # Simulate AI response (you can replace this with Gemini/GPT API later)
    st.subheader("🤖 Assistant Response:")
    st.write(f"Based on your symptoms: '{user_input}'")
    st.write("You may be experiencing a common condition such as fatigue, headache, or cold.")
    st.write("For a proper diagnosis, please consult a doctor. 🩺")
