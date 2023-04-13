from flask import Flask, render_template, request, redirect, url_for
import requests
import pyttsx3
import openai
from main import generate_response  

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        chatbot_response = generate_response(user_input)
        return render_template("index.html", user_input=user_input, chatbot_response=chatbot_response)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
