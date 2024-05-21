from flask import Flask, render_template, request, Response, jsonify
import time
import asyncio


app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def index():
    """Root"""
    now = time.monotonic()
    return render_template(template_name_or_list="index.html", mytime=now)


@app.route("/crossword")
def crossword():
    """crossword"""
    return render_template(template_name_or_list="crossword.html")


@app.route("/handle_post", methods=['POST'])
def handle_post():
    greeting = request.json.get('greeting')
    name = request.json.get('name')

    with open('file.txt', 'w', encoding="utf-8") as f:
        f.write(f"{greeting}, {name}")

    return jsonify({'message': 'File Written!'})


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80, debug=True)
