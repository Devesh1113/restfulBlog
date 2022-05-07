from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///virtual-books-collection.db'
db = SQLAlchemy(app)


class MyBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<MyBook {self.title}>"


db.create_all()

all_books = db.session.query(MyBook).all()


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = MyBook(title=request.form["name"].title(), author=request.form["author_name"].title(), rating=request.form["rating"])
        try:
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('home'))
        except IntegrityError:
            return render_template("add.html", exists=True)
    return render_template("add.html")


@app.route("/id=<num>", methods=["POST", "GET"])
def edit_rating(num):
    if request.method == "POST":
        book_to_update = MyBook.query.filter_by(id=num).first()
        book_to_update.rating = request.form["new_rating"]
        db.session.commit()
        return redirect(url_for('home'))

    book = MyBook.query.filter_by(id=num).first()
    return render_template("edit_rating.html", book=book)


if __name__ == "__main__":
    app.run(debug=True)
