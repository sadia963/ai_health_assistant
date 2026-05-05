 AI Health Assistant
An AI-powered web application that analyzes user symptoms and provides possible causes, home care tips, and warning signs using LLM (Groq API).)
Live Demo

link deployment: https://huggingface.co/spaces/sadiaxo/healthbot

Features
💬 Chat-based medical assistant
🧠 AI symptom analysis (LLaMA 3 via Groq)
🗂 Chat history stored in database
🎤 Voice input support
⚡ Fast Flask backend
🐳 Docker support

🛠 Tech Stack
Category: Technology
Backend: Flask, SQLAlchemy
Frontend: HTML, CSS, JavaScript
AI Model: Groq (llama-3.1-8b-instant)
Database: SQLite
Deployment: Gunicorn, Docker

📁 Project Structure

AI-Health-Assistant/
├── app.py
├── requirements.txt
├── Dockerfile
├── chat.db
├── templates/
│   └── index.html
├── static/
│   └── main.js
t└── README.md

⚙️ Setup Instructions
1️⃣ Clone the Repository
Bash
git clone https://github.com/your-username/ai-health-assistant.git
cd ai-health-assistant
2️⃣ Create Virtual Environment
Bash
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
Bash
pip install -r requirements.txt
4️⃣ Add Environment Variables
Create .env file:
Environment
GROQ_API_KEY=your_api_key_here
5️⃣ Run the App
Bash
python app.py
Open in browser:

http://localhost:7860

🐳 Docker Usage
Build
Bash
docker build -t ai-health-app .
Run
Bash
docker run -p 7860:7860 ai-health-app
📡 API Endpoints
🔹 /history (GET)
Returns chat history
🔹 /analyze (POST)
Request:
JSON
{
  "symptoms": "fever and headache",
  "age_group": "Adult",
  "duration": "2 days"
}
Response:
JSON
{
  "reply": "Possible Causes:\n- ...\n\nHome Care:\n- ..."
}
🎤 Voice Input
Click Speak button
Uses browser Speech Recognition
Convert speech into text 
