# -*- coding: utf8 -*-

from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, EqualTo, Email, Length
from wtforms.ext.sqlalchemy.validators import Unique

from library import db

from library.users.models import User


class LoginForm(Form):
    email = TextField(u'Email', [Required(), Email()])
    password = PasswordField(u'Пароль', [Required()])


class RegisterForm(Form):
    name = TextField(u'Имя', [Required(), Length(max=50)])
    email = TextField(u'Email', [Required(),
                                 Length(max=(120)),
                                 Email(), Unique(db.session, User, User.email,
                                                                    u"Этот адрес уже используется")])
    password = PasswordField(u'Пароль', [Required(),
                                         Length(max=120)])
    confirm = PasswordField(u'Повторите пароль', [
        Required(),
        EqualTo('password', message=u'Пароли не сходятся')
        ])