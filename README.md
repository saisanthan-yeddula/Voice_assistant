# Voice Assistant

This project is a Python-based **Voice Assistant** that helps users perform various tasks using voice commands. It integrates speech recognition, text-to-speech synthesis, web automation, Wikipedia searches, email functionality, and AI-generated responses.

## Features

### 🎧 Speech Recognition & Text-to-Speech  
- Listens to voice commands using a microphone.  
- Converts recognized speech into text.  
- Provides spoken responses using text-to-speech synthesis.

### 🔍 Smart Search & Information Retrieval  
- Searches Wikipedia for user queries and provides a brief summary.  
- Opens websites such as **Google**, **Spotify**, and **ChatGPT**.  
- Performs a Google search when information is not found on Wikipedia.

### 🎵 Media Control  
- Plays music or videos from **YouTube** using `pywhatkit`.

### 🕒 Time & Date Retrieval  
- Provides the current time and date.

### 📧 Email Sending  
- Allows sending emails via **SMTP** (Gmail).  
- Requires user to enter email credentials.

### 🤖 AI-Powered Responses  
- Uses **OpenAI API** to generate AI-based answers.  
- Supports general chat-based interaction.

### 🔐 User Commands & Exit Functionality  
- Supports commands like **"exit"**, **"stop"**, and **"no"** to terminate the assistant gracefully.  
- Re-prompts the user for further assistance after each command.

## Installation & Setup

1. Install the required Python packages using:
   ```bash
   pip install speechrecognition pyttsx3 pywhatkit wikipedia smtplib openai requests
   ```
2. Set up the **OpenAI API Key** as an environment variable:
   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```
3. Run the script:
   ```bash
   python Voice_assistant.py
   ```

## Usage

1. Start the assistant and give voice commands like:
   - **"Play Shape of You"** → Plays the song on YouTube.
   - **"What is Python?"** → Fetches a Wikipedia summary.
   - **"Open Google"** → Opens the Google website.
   - **"Send an email"** → Sends an email using SMTP.
   - **"What time is it?"** → Provides the current time.

2. Say **"exit"**, **"stop"**, or **"no"** to end the session.

## Future Improvements  
- Enhance voice recognition accuracy.  
- Implement authentication for email sending.  
- Expand AI response capabilities.

## License  
This project is open-source and can be freely modified.

---
👨‍💻 Developed using **Python** | 🎤 Speech Recognition | 🤖 AI-Powered Responses

