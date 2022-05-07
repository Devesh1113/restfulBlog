from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    username = StringField('Name')
    password = PasswordField('Password')
    submit_button = SubmitField('Submit')


app = Flask(__name__)

app.config['SECRET_KEY'] = "devesh"


@app.route("/")
def home():
    return render_template('form_index.html')


@app.route("/login")
def login():
    form = MyForm()
    return render_template("form_login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
