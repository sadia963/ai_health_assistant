from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from groq import Groq
from dotenv import load_dotenv
import os
import json
from datetime import datetime

load_dotenv()

app = Flask(__name__)

# DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chat.db"
db = SQLAlchemy(app)

# AI CLIENT
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# =====================
# DATABASE MODEL
# =====================
class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(10))  # user / bot
    message = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


# =====================
# AI FUNCTION
# =====================
def get_ai_response(symptoms, age_group, duration):

    prompt = f"""
You are a strict medical AI assistant.

RULES:
1. If user input is NOT a real medical symptom (like: hi, hello, nice, ok, random words)
   → return ONLY this JSON:
   {{
     "message": "No medical symptoms detected. Please enter your health problem."
   }}

2. If input IS medical symptoms only then return JSON:
{{
  "causes": ["cause1", "cause2", "cause3"],
  "home_care": ["tip1", "tip2", "tip3", "tip4"],
  "warning_signs": ["warning1", "warning2", "warning3"]
}}

User input: {symptoms}
"""

    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return res.choices[0].message.content


# =====================
# ROUTES
# =====================
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/history")
def history():
    chats = Chat.query.order_by(Chat.id).all()

    return jsonify([
        {
            "sender": c.sender,
            "message": c.message,
            "time": c.timestamp.strftime("%H:%M")
        }
        for c in chats
    ])


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    text = data.get("symptoms", "")
    age = data.get("age_group", "")
    duration = data.get("duration", "")

    db.session.add(Chat(sender="user", message=text))

    try:
        result = get_ai_response(text, age, duration)
        parsed = json.loads(result)

        # simple message (non-medical input)
        if "message" in parsed:
            reply = parsed["message"]
        else:
            reply = f"""Possible Causes:
- {chr(10).join(parsed.get('causes', []))}

Home Care:
- {chr(10).join(parsed.get('home_care', []))}

Warning Signs:
- {chr(10).join(parsed.get('warning_signs', []))}"""

        db.session.add(Chat(sender="bot", message=reply))
        db.session.commit()

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 7860)))