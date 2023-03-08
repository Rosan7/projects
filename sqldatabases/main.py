from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()
new_book = Book(title="Harry Potter", author="J.K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()
# read all books command down
all_books = db.session.query(Book).all()
# read a particular record by query
book = Book.query.filter_by(title="Harry Potter").first()
# update a particular record by query
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()

# update a record by Primary key
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Wizard of Oz"
db.session.commit()
# Delete a particular record by primary key
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()


@app.route("/")
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]

        }
        all_books.append(new_book)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    # db = sqlite3.connect("books-collection.db")
    # cursor = db.cursor()
    # # cursor.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar("
    # #                "250) NOT NULL, rating FLOAT NOT NULL)")
    # cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling','9.3')")
    # db.commit()

    app.run(debug=True)
