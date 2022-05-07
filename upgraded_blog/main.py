from flask import Flask, render_template, request
import requests
import smtplib

OWN_PASSWORD = "Haunted97"
OWN_EMAIL = "mr5527579@gmail.com"

app = Flask(__name__)

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


@app.route("/login-entry", methods=['POST'])
def send_email():
    name = request.form["username"]
    email = request.form["email"]
    number = request.form["number"]
    message = request.form["message"]

    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {number}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

    return "<h1>Successfully sent your message</h1>"


if __name__ == "__main__":
    app.run(debug=True)
