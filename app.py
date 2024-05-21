from flask import Flask, render_template
import time
import asyncio


app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    """Root"""
    now = time.monotonic()
    return render_template(template_name_or_list="index.html", mytime=now)


@app.route("/other")
def other():
    """other"""
    return render_template(template_name_or_list="other.html")


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80, debug=True)
