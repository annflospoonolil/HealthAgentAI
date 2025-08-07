import streamlit as st
import google.generativeai as genai

# --- Setup ---
st.set_page_config(page_title="AI Health Assistant", layout="centered")
st.title("🩺 AI Health Assistant")
st.markdown("Hi! I'm your AI health buddy. How are you feeling today?")

# --- Gemini API Setup ---
api_key = st.secrets["GEMINI_API_KEY"] if "GEMINI_API_KEY" in st.secrets else st.text_input("Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # --- User Input ---
    user_input = st.text_area("Describe your symptoms here:", placeholder="Eg: I have a sore throat and feel tired...")

    if st.button("Analyze Symptoms"):
        if not user_input.strip():
            st.warning("Please describe your symptoms.")
        else:
            with st.spinner("Analyzing your symptoms..."):
                prompt = f"""
                You are a friendly and helpful AI health assistant.

                The user said: "{user_input}"

                1. Extract the symptoms.
                2. Predict 2–3 likely common illnesses (not a diagnosis).
                3. Suggest next steps (home care or when to see a doctor).
                4. Be friendly and conversational.
                """
                try:
                    response = model.generate_content(prompt)
                    st.markdown("### 🤖 Assistant Response:")
                    st.markdown(response.text.strip())
                except Exception as e:
                    st.error(f"Something went wrong: {e}")
else:
    st.info("Please enter your Gemini API key to begin.")
