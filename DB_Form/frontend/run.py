from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/signup")
def signup():
    return render_template("signup")