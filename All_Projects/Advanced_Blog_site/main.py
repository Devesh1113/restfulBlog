from flask import Flask, render_template, flash, redirect, url_for
import requests
from login import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "Haunted97"

response = requests.get(url=" https://api.npoint.io/67b2e43e59e5396bb388")
data = response.json()


@app.route("/")
def home_page():
    return render_template("index_upgraded.html", posts=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<num>")
def post(num):
    return render_template("post.html", num=int(num), post=data)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account Created for {form.username.data}", "success")
        return redirect(url_for("home_page"))
    return render_template("register.html", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
