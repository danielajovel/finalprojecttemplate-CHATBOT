from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)  # Allow frontend and backend to communicate across ports

# Route for the root URL
@app.route("/")
def home():
    return "Welcome to the Chatbot Backend!"

# API endpoint for chatbot responses
@app.route("/api/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")

    # Example: Basic response logic (you can replace this!)
    bot_response = f"You said: {user_message}. Customize me!"

    # Return the bot's response
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
