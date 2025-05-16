#Overview

The Grammar & Spelling Corrector Chatbot is a simple and interactive web tool that helps users improve the grammatical quality and spelling of their text. It leverages Google’s Gemini AI (GenerativeModel) to process and return corrected versions of paragraphs or stories entered by the user. This tool is ideal for writers, students, and anyone who wants to polish their writing.

#Features

Accepts free-form text input (paragraphs, stories, etc.)

Checks and corrects grammar and spelling mistakes

Provides original and corrected versions side-by-side

Clean and responsive web interface using Streamlit

AI-powered backend using Gemini 2.0 Flash model

#Technologies Used
Python for backend logic

Streamlit for the web interface

Google Generative AI (Gemini) for text processing

#Installation
Clone the repository:


git clone https://github.com/ayushiraut01/Grammar-Spelling-Corrector-Chat-bot

cd grammar-corrector-chatbot

#Create and activate a virtual environment:


python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
#Install dependencies:

pip install -r requirements.txt

#Set up your Google API key:

#Open the app.py file and replace:


genai.configure(api_key="YOUR_API_KEY_HERE")
with your actual Google Generative AI API key.

#Usage
Run the Streamlit app:


streamlit run app.py
#Use the web interface:

Enter a story or paragraph into the text area.

Click on "Submit & Correct".

View both the original and corrected text in the interface.

#Future Enhancements
Downloadable corrected text

Multi-language support

Correction history log

Grammar explanation tooltips

Mobile-friendly UI

#Contributing
Contributions are welcome!
Feel free to fork the repository and submit a pull request with new features or bug fixes.

#License
This project is licensed under the MIT License.

#Author
Ayushi Raut 
GitHub Repository:[ https://github.com/your-username/grammar-corrector-chatbot](https://github.com/ayushiraut01/Grammar-Spelling-Corrector-Chat-bot)
