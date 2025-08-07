import streamlit as st

st.set_page_config(page_title="AI Health Assistant", layout="centered")

st.title("🩺 AI Health Assistant")
st.markdown("Hi there! 👋 I'm your AI health buddy.\n\nTell me how you're feeling today.")

# Initialize session state
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "response" not in st.session_state:
    st.session_state.response = ""

def handle_submit():
    user_input = st.session_state.user_input.strip().lower()

    if user_input in ["hey", "hello", "hi"]:
        response = "🤖 Assistant: Hello there! 👋 How are you feeling today? Please describe any symptoms you're experiencing."
    elif len(user_input.split()) <= 2:
        response = f"🤖 Assistant: I need a bit more detail to help. Could you describe how you're feeling?"
    else:
        response = f"""
🤖 Assistant: Thanks for sharing. Based on what you said: "{user_input}", you might be having a mild condition like fatigue, a cold, or stress.

🤖 Assistant: Could you tell me if you also have a fever, pain, or any unusual symptoms?
"""
    st.session_state.response = response
    st.session_state.user_input = ""
    st.session_state.submitted = True

st.text_area("Describe your symptoms here:", key="user_input", on_change=handle_submit)

if st.session_state.submitted and st.session_state.response:
    st.subheader("Assistant Response:")
    st.write(st.session_state.response)
    st.session_state.submitted = False
