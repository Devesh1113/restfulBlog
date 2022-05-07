# # it is preinstalled just need to import it
# import sqlite3
#
# # to create a new database
# db = sqlite3.connect("books-collection.db")
#
# # to create a cursor to move
# cursor = db.cursor()
#
# # execute: This method will tell the cursor to execute an action.
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) "
#                "NOT NULL, rating FLOAT NOT NULL)")
#
# # adding data to our database
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


db.create_all()


# Creating a new record
# new_book = Book(id=1, title="Learn to earn", author="Peter Lynch", rating=9.4)
# db.session.add(new_book)
# db.session.commit()

# new_book = Book(title="Harry Porter", author="Devesh", rating=8.4)
# db.session.add(new_book)
# db.session.commit()

# reading all records
all_books = db.session.query(Book).all()
print(all_books)
#
# # Read A Particular Record By Query
# book = Book.query.filter_by(title="Learn to earn").first()
# print(book)
#
# # Update A Particular Record By Query
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()
#
# # Update A Record By PRIMARY KEY
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()
#
# # Delete A Particular Record By PRIMARY KEY
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()

