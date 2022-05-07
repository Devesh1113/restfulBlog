from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config["SECRET_KEY"] = "Haunted97"


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email(), Length(min=10), InputRequired("invalid email "
                                                                                                   "address")])

    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=16), InputRequired("Field must "
                                                                                                          "be atleast"
                                                                                                          " 8 "
                                                                                                          "characters "
                                                                                                          "long")])
    remember = BooleanField("Remember Me")
    submit = SubmitField("SignUp")


@app.route("/")
def home():
    return render_template("form_index.html")


@app.route('/login', methods=["POST", "GET"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "deveshk237@gmail.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("form_login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
