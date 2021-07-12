from flask import Flask
from get_weaknesses import task

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello from Microsoft!"

@app.route("/pokemon_weaknesses")
def pokemon_weaknesses():
    return task()