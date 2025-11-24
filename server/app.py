from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

# Load API key
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash-lite")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")

    try:
        response = model.generate_content(user_msg)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "Flask server running!"

if __name__ == "__main__":
    app.run(debug=True)
