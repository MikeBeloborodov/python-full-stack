from flask import Flask, render_template
import templates
import database_interaction

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/notes")
def send_all_notes():
    return render_template('notes.html')

