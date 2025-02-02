from flask import Flask, request, render_template
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route("/helloworld", methods=["GET"])
def index():
    username = request.args.get('name')
    arg = request.args.get('arg')
    return f"Hello {username} " + arg

@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e

    return render_template("500_generic.html", e=e), 500

if __name__ == "__main__":
    app.run(debug=True)