from flask import Flask, render_template, request, session, redirect
import requests
from markupsafe import Markup


app = Flask(__name__)
app.secret_key = "12345"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        req = request.form
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post("http://127.0.0.1:8080/signup", data=req, headers=headers)

        # Ensure the response is valid
        if response.status_code == 200:
            session['result'] = response.json().get("message", "Signup successful!")
            return redirect("/createsuccess")
        else:
            return "Error in external API request", response.status_code
    return render_template("signup.html")

@app.route("/createsuccess", methods=["GET", "POST"])
def signup_success():
    data = Markup(session.pop("result"))
    return render_template("createsuccess.html", result=data)

@app.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        req = request.form
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post("http://127.0.0.1:8080/login", data=req, headers=headers)

        if response.status_code == 200:
            session['result'] = response.json().get("message", "Signup successful!")
            return redirect("/loginsuccess")
        else:
            return "Error in external API request", response.status_code
    return render_template("login.html")

@app.route("/loginsuccess", methods=["GET", "POST"])
def login_success():
    data = Markup(session.pop("result"))
    return render_template("loginsuccess.html", result=data)

        
        
        



if __name__ == "__main__":
    app.run(port="3000", debug=True)