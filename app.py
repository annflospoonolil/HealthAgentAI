import streamlit as st
import random

# Page setup
st.set_page_config(page_title="AI Health Assistant", layout="centered")
st.title("🩺 AI Health Assistant")
st.markdown("Hi there! 👋 I'm your AI health buddy. Tell me how you're feeling today.")

# Friendly greetings
greetings = [
    "Hope you're having a good day!",
    "I'm here to help you feel better.",
    "Tell me anything – I'm listening! 😊",
    "Ready when you are 💬"
]
st.write(random.choice(greetings))

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("You:", key="input")

if user_input:
    # Save user message
    st.session_state.chat_history.append(("user", user_input))

    # Simulate AI logic (replace this with Gemini API if needed)
    ai_response = f"Thanks for sharing. Based on what you said: \"{user_input}\", you might be having a mild condition like fatigue, a cold, or stress."

    # Add AI response
    st.session_state.chat_history.append(("ai", ai_response))

    # Add follow-up question
    follow_up = "Could you tell me if you also have a fever, pain, or any unusual symptoms?"
    st.session_state.chat_history.append(("ai", follow_up))

# Show the full conversation
st.subheader("🧠 Conversation")
for role, message in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"**👤 You:** {message}")
    else:
        st.markdown(f"**🤖 Assistant:** {message}")

# Optional: Clear chat button
if st.button("🔄 Restart Conversation"):
    st.session_state.chat_history = []
    st.experimental_rerun()
