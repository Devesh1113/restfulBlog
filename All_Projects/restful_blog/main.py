from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length, EqualTo
from flask_ckeditor import CKEditor, CKEditorField
import datetime
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from functools import wraps
from flask import g, request, redirect, url_for, abort
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_gravatar import Gravatar

now = datetime.date.today()

app = Flask(__name__)
login_manager = LoginManager()
login_manager.__init__(app)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)
Base = declarative_base()
gravatar = Gravatar(app, size=50, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE TABLE
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    comment_author = relationship("User", back_populates="comments")
    text = db.Column(db.Text, nullable=False)


db.create_all()

posts = db.session.query(BlogPost).all()
users = db.session.query(User).all()
db.session.commit()


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=20)])
    confirm_password = StringField("Confirm Password", validators=[DataRequired(), EqualTo(password)])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")


# Python Decorator
def admin_only(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        try:
            the_id = current_user.id
        except:
            print("no user")
            the_id = 0
        if the_id == 1:
            return function(*args, **kwargs)
        return abort(403)

    return decorated


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated, name=users)


@app.route("/post/<int:index>", methods=["POST", "GET"])
def show_post(index):
    form = CommentForm()
    requested_post = BlogPost.query.get(index)

    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=form.comment.data,
            comment_author=current_user,
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
    return render_template("post.html", post=requested_post, form=form, current_user=current_user)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=['POST', "GET"])
@admin_only
def new_post():
    make_new_post = CreatePostForm()
    if request.method == "POST":
        blogpost = BlogPost(
            title=request.form["title"],
            subtitle=request.form["subtitle"],
            author=current_user,
            body=request.form["body"],
            img_url=request.form["img_url"],
            date=now.strftime("%B %d,%Y")

        )
        db.session.add(blogpost)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=make_new_post, current_user=current_user)


@app.route("/edit-post/<post_id>", methods=["POST", "GET"])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if request.method == "POST":
        post.title = request.form["title"]
        post.subtitle = request.form["subtitle"]
        post.img_url = request.form["img_url"]
        post.author = request.form["author"]
        post.body = request.form["body"]
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", is_edit=True, id=post_id, form=edit_form, current_user=current_user)


@app.route("/delete/<post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if request.method == "POST":

        registered_user = User.query.filter_by(email=request.form.get('email')).first()
        print(registered_user)
        if registered_user:
            flash("You are already registered. Login instead")
            return redirect(url_for("login"))

        else:
            hashed_password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256',
                                                     salt_length=8)

            registration = User(
                name=request.form["name"],
                email=request.form["email"],
                password=hashed_password

            )
            db.session.add(registration)
            db.session.commit()
            login_user(registration)
            return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=form, logged_in=current_user.is_authenticated)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        log_user = User.query.filter_by(email=email).first()
        if not log_user:
            flash("You are not registered")
            redirect(url_for('register'))

        elif not check_password_hash(log_user.password, password):
            flash('Invalid Password. Try Again')
            redirect(url_for('login'))

        else:
            login_user(log_user)
            return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=form, logged_in=current_user.is_authenticated)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
