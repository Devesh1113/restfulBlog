from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def render():
    # we can pass over any variable into our html by assigning a variable in render template code.
    random_number = random.randint(1, 10)
    my_time = datetime.now().year
    # this variable has to be passed in our html file where we want to get it.
    return render_template("form_index.html", num=random_number, year=my_time)


@app.route("/<name>")
def guess_gender(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    data = response.json()
    return render_template("guess_gender.html", user_name=data["name"].title(), user_gender=data["gender"])


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/82975389c85afb34e389"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
