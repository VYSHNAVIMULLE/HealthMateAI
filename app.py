from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Smart-like fake medical chatbot replies for demo
def generate_bot_reply(user_input):
    user_input = user_input.lower()
    
    if "fever" in user_input:
        return "It seems like you might have an infection. Stay hydrated and monitor your temperature."
    elif "headache" in user_input:
        return "Try to rest and avoid screen time. If the headache persists, consult a doctor."
    elif "back pain" in user_input:
        return "Maintain good posture and try light stretching. If pain worsens, seek medical advice."
    elif "cold" in user_input or "cough" in user_input:
        return "It sounds like a common cold. Drink warm fluids and rest well."
    elif "thank" in user_input:
        return "You're welcome! Stay healthy, Vyshnavi 😊"
    else:
        return "Please describe your symptoms in detail. I'm here to help with basic medical advice."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    data = request.get_json()
    user_message = data["message"]
    
    reply = generate_bot_reply(user_message)
    
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
