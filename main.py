from flask import Flask, render_template, url_for, request, jsonify
import os
from dotenv import load_dotenv
from openai import OpenAI

app = Flask(__name__)

load_dotenv()

api_key = os.getenv("GROCK_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=[
            {
                "role": "system",
                "content": "Act like a Helpful Personal assistant"
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.7,
        max_output_tokens=512
    )

    answer = response.output_text.strip()

    return jsonify({"response": answer}), 200


@app.route("/summarize", methods=["POST"])
def summarize():
    email_text = request.form.get("Email")

    prompt = f"Summarize the following email in 2-3 sentences:\n\n{email_text}"

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=[
            {
                "role": "system",
                "content": "Act like an expert email assistant"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_output_tokens=256
    )

    summary = response.output_text.strip()

    return jsonify({"response": summary}), 200


if __name__ == "__main__":
    app.run(debug=True)