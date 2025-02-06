from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import requests


load_dotenv()


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users1(db.Model):
    __tablename__ = "users1"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    

@app.route("/signup", methods=["POST"])
def sign_up():
    data = request.form
    
    if not data:
        return jsonify({"message": "Invalid JSON input"}), 400
    
    try:
        new_user = Users1(name=data["name"], email=data["email"], password=data["password"])
        db.session.add(new_user)
        db.session.commit()
    except KeyError:
        return jsonify({"message": "Invalid JSON input"}), 400
    
    return jsonify({"message": "Sign up successful"}), 200

@app.route("/login", methods=["POST"])
def login():
    data = request.form
    
    if not data:
        return jsonify({"message": "Invalid JSON input"}), 400
    
    try:
        user_record = db.session.query(Users1).filter_by(email=data["email"], password=data["password"]).first()
        if user_record:
            return jsonify({"message": "Log in successful"}), 200
    except KeyError:
        return jsonify({"message": "Invalid JSON input"}), 400
    except Exception:
        return jsonify({"message": "Unknown error occured"}), 404
    
    return jsonify({"message": "Login unsuccessful"}), 400

if __name__ == "__main__":
    app.run(port="8080", debug=True)