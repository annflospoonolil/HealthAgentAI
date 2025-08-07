import streamlit as st
import google.generativeai as genai

# --- Streamlit Page Setup ---
st.set_page_config(page_title="AI Health Assistant", layout="centered")
st.title("🩺 AI Health Assistant")
st.markdown("Hi! I'm your AI health buddy. 😊 Tell me how you're feeling today.")

# --- Gemini API Setup ---
api_key = st.secrets["GEMINI_API_KEY"] if "GEMINI_API_KEY" in st.secrets else st.text_input("🔑 Enter your Gemini API Key", type="password")

# --- Session State for conversation memory ---
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# --- Main Logic ---
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    user_input = st.text_area("📝 Describe your symptoms here:", placeholder="Eg: I have a sore throat and feel tired...")

    if st.button("🔍 Analyze Symptoms"):
        if not user_input.strip():
            st.warning("⚠️ Please describe your symptoms first.")
        else:
            with st.spinner("Analyzing your symptoms... 🤖"):
                # Construct prompt with dynamic follow-up
                prompt = f"""
                You are a friendly, agentic health assistant AI.

                The user said: "{user_input}"

                Please:
                1. Extract and summarize the symptoms.
                2. Predict 2–3 likely common illnesses (make clear it's not a medical diagnosis).
                3. Offer simple next steps (home care, hydration, or when to consult a doctor).
                4. End with a friendly, open-ended follow-up question to continue the conversation.

                Speak naturally like a caring health assistant. Use bullet points where helpful.
                """
                try:
                    response = model.generate_content(prompt)
                    response_text = response.text.strip()
                    st.session_state.conversation.append(("user", user_input))
                    st.session_state.conversation.append(("assistant", response_text))

                    st.markdown("### 🤖 Assistant Response:")
                    st.markdown(response_text)

                except Exception as e:
                    st.error(f"❌ Something went wrong: {e}")

    # --- Display previous conversation ---
    if st.session_state.conversation:
        with st.expander("🗂️ Conversation History"):
            for role, msg in st.session_state.conversation:
                if role == "user":
                    st.markdown(f"**👤 You:** {msg}")
                else:
                    st.markdown(f"**🤖 Assistant:** {msg}")

else:
    st.info("🔒 Please enter your Gemini API key to begin.")
