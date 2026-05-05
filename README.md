🩺 AI Health Assistant

An AI-powered web application that analyzes user symptoms and provides possible causes, home care tips, and warning signs using LLM (Groq API).

🌐 Live Demo

https://huggingface.co/spaces/sadiaxo/healthbot

🚀 Features

💬 Chat-based medical assistant
🧠 AI symptom analysis (LLaMA 3 via Groq)
🗂 Chat history stored in database
🎤 Voice input support
⚡ Fast Flask backend
🐳 Docker support

🛠 Tech Stack

Category:	Technology
Backend:	Flask, SQLAlchemy
Frontend:	HTML, CSS, JavaScript
AI Model:	Groq (llama-3.1-8b-instant)
Database:	SQLite
Deployment:	Gunicorn, Docker

📁 Project Structure

AI-Health-Assistant/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── chat.db
│
├── templates/
│   └── index.html
│
├── static/
│   └── main.js
│
└── README.md

⚙️ Setup Instructions
1️⃣ Clone the Repository
https://github.com/sadia963/Ai_health_assistant.git
cd ai-health-assistant
2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Add Environment Variables

Create .env file:
GROQ_API_KEY=my_api_key_here

5️⃣ Run the App
python app.py

📡 API Endpoints
🔹 /history (GET)

Returns chat history

🔹 /analyze (POST)

Request: In JSON

{
  "symptoms": "fever and headache",
  "age_group": "Adult",
  "duration": "2 days"
}

Response: In JSON

{
  "reply": "Possible Causes:\n- ...\n\nHome Care:\n- ..."
}
🎤 Voice Input

Click Speak button
Uses browser Speech Recognition
Converts speech → text

🩺 Conclusion
This AI Health Assistant project is built using Flask, Groq API, SQLite, and a simple web interface. It takes user symptoms as input and uses an AI model to generate possible causes, home care tips, and warning signs in a structured format. All conversations are stored in a database to maintain chat history.
The project demonstrates how AI can be integrated into web applications to provide basic health guidance. It is designed for educational purposes and is not a replacement for professional medical advice.
