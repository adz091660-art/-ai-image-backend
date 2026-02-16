from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/generate", methods=["POST"])
def generate_image():
    data = request.json
    prompt = data.get("prompt")

    response = requests.post(
        "https://api.openai.com/v1/images",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-image-1",
            "prompt": prompt,
            "size": "1024x1024"
        }
    )

    return jsonify(response.json())

if __name__ == "__main__":
    app.run()
