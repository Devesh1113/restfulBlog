import flask
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, jsonify
from flask_wtf import form
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

login_manager = LoginManager()
login_manager.__init__(app)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
db.create_all()

user = User()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':

        registered_user = User.query.filter_by(email=request.form.get('email')).first()

        if registered_user.email == request.form.get('email'):
            flash("You are already registered. Login instead")
            return redirect(url_for("login"))

        else:
            hashed_password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8)
            new_user = User(
                email=request.form.get('email'),
                name=request.form.get('name'),
                password=hashed_password
            )
            db.session.add(new_user)
            db.session.commit()
            return render_template("secrets.html", name=request.form.get('name').title())
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    pass


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email entered.
        log_user = User.query.filter_by(email=email).first()

        if not log_user:
            flash("That Email does not Exists. Please try again")
            redirect(url_for("login"))
        # Check stored password hash against entered password hashed.
        elif not check_password_hash(log_user.password, password):
            flash("Invalid Password")
            return redirect(url_for('login'))
        else:
            login_user(log_user)
            return redirect(url_for("secrets"))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/download/')
def download():
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)

