from flask import Flask, render_template

import requests

app = Flask(__name__)


@app.route("/")
def get_posts():
    response = requests.get(url="https://api.npoint.io/82975389c85afb34e389")
    posts = response.json()
    return render_template("form_index.html", posts=posts)


@app.route("/blog/<num>")
def post(num):
    response = requests.get(url="https://api.npoint.io/82975389c85afb34e389")
    data = response.json()
    return render_template("post.html", post=data, num=int(num))


if __name__ == "__main__":
    app.run(debug=True)
