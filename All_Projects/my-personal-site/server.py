from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def Hello():
    # How to render HTMl files in flask
    return render_template("form_index.html")


if __name__ == "__main__":
    app.run(debug=True)
