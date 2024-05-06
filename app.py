from flask import Flask, flash, render_template, request
import json
import random

app = Flask(__name__)
app.secret_key = b'secret'

stations = json.load(open("stations.json", "r"))
photos = json.load(open("photos.json", "r"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if request.form['station'] == request.form['realstation']:
            flash("Bravo! Asta-i statia!", "succes")
        else:
            flash("Asta nu-i statia...", "danger")
    photo = random.choice(photos["photos"])
    return render_template("index.html", photo=photo, stations=stations["stations"])