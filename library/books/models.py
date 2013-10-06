from flask import url_for
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

from library import db

books_authors = db.Table('books_book_author',
    db.Column('book_id', db.Integer, db.ForeignKey('books_book.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('books_author.id'))
)


class Book(db.Model):

    __tablename__ = "books_book"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    authors = db.relationship("Author", secondary=books_authors, backref=db.backref('books', lazy='dynamic'))

    @hybrid_property
    def name_with_authors(self):
        return self.name + ' ' + ','.join([entry.name for entry in self.authors])

    def init(self, name=None, authors=None):
        self.name = name
        self.authors = authors

    def __repr__(self):
        return '<Book %r>' % (self.name,)

    def get_url(self):
        return url_for('books.book_details', book_id=self.id)

    def __unicode__(self):
        return self.name


class Author(db.Model):

    __tablename__ = "books_author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, name=None, books=None):
        self.name = name
        self.books = books

    def __repr__(self):
        return "<Author %r>" % (self.name,)

    def get_url(self):
        return url_for('books.author_details', author_id=self.id)

    def __unicode__(self):
        return self.name