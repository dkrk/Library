# -*- coding: utf8 -*-
from itertools import chain

from flask import Blueprint, session, render_template, request, g, url_for, redirect, flash, jsonify

from library.users.decorators import requires_login
from library.books.models import Book, Author
from library.books.forms import BookForm, AuthorForm
from library import db


books_app = Blueprint('books', __name__, static_folder='static', template_folder='templates')


@books_app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and g.user:
        authors_ids = [int(i) for i in request.form.getlist('authors_delete')]
        books_ids = [int(i) for i in request.form.getlist('books_delete')]
        Book.query.filter(Book.id.in_(books_ids)).delete(synchronize_session='fetch')
        Author.query.filter(Author.id.in_(authors_ids)).delete(synchronize_session='fetch')
        db.session.commit()
        return redirect(url_for('books.index'))
    books = Book.query.all()
    authors = Author.query.all()
    return render_template("books/index.html", books=books, authors=authors)


@books_app.route('/book/<int:book_id>/')
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('books/book_details.html', book=book)


@books_app.route('/author/<int:author_id>/')
def author_details(author_id):
    author = Author.query.get_or_404(author_id)
    return render_template('books/author_details.html', author=author)


@books_app.route("/book/add/", methods=['GET', 'POST'])
@requires_login
def add_book():
    form = BookForm(request.form)
    del form.delete
    if form.validate_on_submit():
        book = Book(
            name=form.name.data,
            authors=form.authors.data,
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books.book_details', book_id=book.id))
    return render_template("books/form.html", form=form)


@books_app.route("/book/edit/<int:book_id>/", methods=['GET', 'POST'])
@requires_login
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    form = BookForm(request.form, book)
    if form.delete.data:
            db.session.delete(book)
            db.session.commit()
            return redirect(url_for('books.index'))
    if form.validate_on_submit():
        book.name = form.name.data
        book.authors = form.authors.data
        db.session.commit()
        return redirect(url_for('books.book_details', book_id=book.id))
    return render_template('books/form.html', form=form)


@books_app.route("/author/add/", methods=['GET', 'POST'])
@requires_login
def add_author():
    form = AuthorForm(request.form)
    del form.delete
    if form.validate_on_submit():
        author = Author(
            name=form.name.data,
            books=form.books.data
        )
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('books.author_details', author_id=author.id))
    return render_template('books/form.html', form=form)



@books_app.route("/author/edit/<int:author_id>/", methods=['GET', 'POST'])
@requires_login
def edit_author(author_id):
    author = Author.query.get_or_404(author_id)
    form = AuthorForm(request.form, author)
    if form.delete.data:
            db.session.delete(author)
            db.session.commit()
            return redirect(url_for('books.index'))
    if form.validate_on_submit():
        author.name = form.name.data
        author.books = form.books.data
        db.session.commit()
        return redirect(url_for('books.author_details', author_id=author.id))
    return render_template('books/form.html', form=form)


@books_app.route('/search/', methods=['GET', 'POST'])
def search():
    q = request.form.get('q', "")
    result = []
    chkBook, chkAuthor = request.form.get('chkBook', None), request.form.get('chkAuthor', None)
    session['chkBook'], session['chkAuthor'] = chkBook, chkAuthor
    if q:
        books = Book.query.filter(Book.name.ilike(u"%{}%".format(q))) if chkBook else []
        authors = Author.query.filter(Author.name.ilike(u"%{}%".format(q))) if chkAuthor else []
        result = (entry for entry in chain(books, authors))
    context = {
        'query': q,
        'result': result
    }
    return render_template('books/search_result.html', **context)

@books_app.route('/live-search/')
def live_search():
    q = request.args.get('term', "")
    result = []
    if q:
        books = Book.query.filter(Book.name.ilike(u"%{}%".format(q)))
        authors = Author.query.filter(Author.name.ilike(u"%{}%".format(q)))
        result = [entry.name for entry in chain(books, authors)]

    return jsonify(result=result)