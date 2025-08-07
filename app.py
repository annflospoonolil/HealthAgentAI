import streamlit as st
import google.generativeai as genai

# --- Page Config ---
st.set_page_config(page_title="AI Health Assistant", layout="centered")
st.title("🩺 AI Health Assistant")
st.markdown("Hi! I'm your AI health buddy. How are you feeling today?")

# --- API Key ---
api_key = st.secrets["GEMINI_API_KEY"] if "GEMINI_API_KEY" in st.secrets else st.text_input("🔑 Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # --- Chat History ---
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # --- User Input ---
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("💬 Your message:", placeholder="Eg: I have a sore throat and feel tired...")
        submitted = st.form_submit_button("🚀 Send")

    if submitted and user_input.strip():
        # Append user message
        st.session_state.chat_history.append({"role": "user", "parts": [user_input]})

        with st.spinner("Analyzing your symptoms..."):
            try:
                # Generate reply with full history
                response = model.generate_content(st.session_state.chat_history)
                # Append assistant reply
                st.session_state.chat_history.append({"role": "model", "parts": [response.text.strip()]})
            except Exception as e:
                st.error(f"❌ Error: {e}")

    # --- Display Chat ---
    if st.session_state.chat_history:
        st.markdown("### 💬 Chat")
        for turn in st.session_state.chat_history:
            if turn["role"] == "user":
                st.markdown(f"**👤 You:** {turn['parts'][0]}")
            else:
                st.markdown(f"**🤖 Assistant:** {turn['parts'][0]}")

    # --- Clear Chat Option ---
    if st.button("🧹 Clear Conversation"):
        st.session_state.chat_history = []
        st.rerun()
else:
    st.info("🔐 Please enter your Gemini API key to begin.")
