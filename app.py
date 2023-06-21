from flask import Flask, render_template, request, jsonify
from engine.letter_guess import run

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/auto_complete_np", methods=["GET"])
def auto_complete_nep():
    user_input = request.args.get("query")
    last_char = user_input[-1]
    user_input = " ".join(user_input.split())

    return jsonify({"text": run(user_input+last_char)})


if __name__== "__main__":
    app.run()