from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Disease")
def disease():
    return render_template("disease.html")


@app.route("/Pests")
def pest():
    return render_template("pest.html")


@app.route("/Crisis-aversion")
def panic():
    pass


@app.route("/Scanner")
def scan():
    return render_template("scan.html")


@app.route("/Scanner/Insect")
def insect():
    # streamlit run Predections/Insect/predictions.py
    pass


@app.route("/Scanner/Plant-Disease")
def plant_disease():
    # streamlit run Predections/Plant-Disease/prediction.py
    pass


@app.route("/Filter")
def filter():
    pass


if __name__ == "__main__":
    app.run(port=8080)
