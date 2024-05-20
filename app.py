from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    """Root"""
    return render_template(template_name_or_list="index.html", myvalue="regex101")


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80, debug=True)
