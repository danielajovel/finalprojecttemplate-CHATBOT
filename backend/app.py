from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)  # Allow frontend and backend to communicate across ports

# Route for the root URL
@app.route("/")
def home():
    return "Welcome to the Chatbot Backend!"

# Chatbot Logic
def chatbot_logic(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    return response['choices'][0]['message']['content']

# API Endpoint for chatbot
@app.route("/api/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    bot_response = chatbot_logic(user_message)  # Call the function
    return jsonify({"response": bot_response})
# API endpoint for chatbot responses
@app.route("/api/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")

   import openai
    openai.api_key = "your_openai_api_key"

    def chatbot_logic(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    app.run(debug=True)
