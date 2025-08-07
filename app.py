import streamlit as st
import google.generativeai as genai

# Replace with your Gemini API key
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

# UI setup
st.set_page_config(page_title="AI Health Assistant", layout="centered")
st.title("🩺 AI Health Assistant")
st.markdown("Hi there! 👋 I'm your AI health buddy.\n\nTell me how you're feeling today.")

user_input = st.text_area("Describe your symptoms here:")

# Greeting check
greetings = ["hi", "hello", "hey", "good morning", "good evening"]

if user_input:
    if user_input.lower().strip() in greetings:
        st.subheader("🤖 Assistant:")
        st.write("Hey there! 😊 I'm here to help with your health concerns. Could you tell me how you're feeling today?")
    else:
        with st.spinner("Analyzing your symptoms..."):
            prompt = f"You are a helpful health assistant. A user says: '{user_input}'. Reply like a caring assistant. Identify symptoms and give possible conditions (but don't give final diagnoses). Ask one follow-up question."
            response = model.generate_content(prompt)
            st.subheader("🤖 Assistant Response:")
            st.write(response.text)
