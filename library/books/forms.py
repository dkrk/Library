# -*- coding:utf8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required, Length
from wtforms.ext.sqlalchemy.validators import Unique
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from wtforms.ext.sqlalchemy.orm import model_form

from library import db

from library.books import models

BookForm = model_form(models.Book, Form)


class BookForm(Form):
    name = TextField(u"Название книжки", [Required(message=u"Заполните это поле"),
                                          Length(max=100, message=u"Название должно быть меньше 100 символов")])
    authors = QuerySelectMultipleField(u"Авторы",
                                       query_factory=lambda: models.Author.query.all(),
                                       allow_blank=True)
    delete = BooleanField(u"Удалить")


class AuthorForm(Form):
    name = TextField(u"Имя Автора", [Required(message=u"Заполните это поле"),
                                     Length(max=100, message=u"Название должно быть меньше 100 символов"),
                                     Unique(db.session, models.Author, models.Author.name,
                                            u"Уже существует автор с таким именем")])
    books = QuerySelectMultipleField(u"Книги",
                                     query_factory=lambda: models.Book.query.all(),
                                     allow_blank=True)
    delete = BooleanField(u"Удалить")
