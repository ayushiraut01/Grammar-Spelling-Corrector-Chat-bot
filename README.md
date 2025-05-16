# Grammar-Spelling-Corrector-Chat-bot

This is a simple web-based chatbot application built with Streamlit and Google Gemini AI (GenerativeModel). It takes a paragraph or story as input and returns a grammatically correct and well-spelled version of the same content.

 Features
 Easy-to-use web interface for grammar correction
 
 AI-powered corrections using Google Gemini (Gemini 2.0 Flash model)
 
Instant results with corrected text displayed alongside original

API key integration for secure usage of Google AI models

 Getting Started
1. Clone the Repository

git clone https://github.com/your-username/grammar-corrector-chatbot.git

cd grammar-corrector-chatbot

2. Install Required Packages
Make sure you have Python 3.7+ installed. Then run:

pip install streamlit google-generativeai

4. Set Up Google Generative AI
Go to Google AI Studio to get your API key.

Replace the placeholder in the script with your actual API key:

genai.configure(api_key="YOUR_API_KEY_HERE")

6. Run the App
streamlit run app.py
The app will launch in your default browser at http://localhost:8501.

 How It Works
The app collects user input through a text area.
On submission, it sends a prompt to the Gemini 2.0 Flash model to correct grammar and spelling.
The response from Gemini is parsed and shown as corrected output.

 Dependencies
streamlit
google-generativeai

You can optionally create a requirements.txt file:
streamlit
google-generativeai

License
This project is open-source and available under the MIT License.

Author
Created by Ayushi Raut 

