import streamlit as st
import google.generativeai as genai

# --- Page Configuration ---
st.set_page_config(page_title="AI Health Assistant", layout="centered")
st.title("🩺 AI Health Assistant")
st.markdown("Hi! I'm your AI health buddy. How are you feeling today?")

# --- API Key Input (Secure or Manual) ---
api_key = st.secrets["GEMINI_API_KEY"] if "GEMINI_API_KEY" in st.secrets else st.text_input("🔑 Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # --- Initialize Chat History ---
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # --- User Input Field ---
    user_input = st.text_input("💬 Your message:", placeholder="Eg: I have a sore throat and feel tired...")

    col1, col2 = st.columns([1, 5])
    with col1:
        send_clicked = st.button("🚀 Send")
    with col2:
        clear_clicked = st.button("🧹 Clear Chat")

    # --- Clear Conversation ---
    if clear_clicked:
        st.session_state.chat_history = []

    # --- On Send ---
    if send_clicked and user_input.strip():
        # Add user input to chat history
        st.session_state.chat_history.append({"role": "user", "parts": [user_input]})

        with st.spinner("Analyzing your symptoms..."):
            try:
                # Send entire chat history for context
                response = model.generate_content(st.session_state.chat_history)
                # Add assistant's response to history
                st.session_state.chat_history.append({"role": "model", "parts": [response.text.strip()]})
            except Exception as e:
                st.error(f"❌ Error: {e}")

    # --- Display Chat History ---
    if st.session_state.chat_history:
        st.markdown("### 💬 Chat")
        for turn in st.session_state.chat_history:
            if turn["role"] == "user":
                st.markdown(f"**👤 You:** {turn['parts'][0]}")
            else:
                st.markdown(f"**🤖 Assistant:** {turn['parts'][0]}")
else:
    st.info("🔐 Please enter your Gemini API key to begin.")
