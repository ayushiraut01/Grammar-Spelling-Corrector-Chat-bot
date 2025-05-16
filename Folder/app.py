import streamlit as st
import google.generativeai as genai
# Configure API key (replace with your real key)
genai.configure(api_key=" ")
# Use a valid model name from the list_models() output
model = genai.GenerativeModel(model_name="gemini-2.0-flash")
st.set_page_config(page_title="Grammar Corrector Chatbot", page_icon=":memo:")
st.markdown("<h1 style='text-align: center;'>Grammar & Spelling Corrector Chat bot</h1>", unsafe_allow_html=True)
st.markdown(":wave: Hello! I’m your grammar bot. Submit a story or paragraph, and I will correct it for you.")
user_input = st.text_area(":writing_hand: Write your story or paragraph here:", height=200)
if st.button(":white_check_mark: Submit & Correct"):
    if user_input.strip() == "":
        st.warning(":warning: Please enter some text to correct.")
    else:
        with st.spinner(":mag: Checking grammar and spelling..."):
            prompt = f"Correct the grammar and spelling of the following text:\n\n{user_input}"
            response = model.generate_content(prompt)
            corrected_text = response.text
        st.subheader(":page_facing_up: Original Text")
        st.write(user_input)
        st.subheader(":white_check_mark: Corrected Text")
        st.success(corrected_text)
