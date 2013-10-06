# -*- coding: utf8 -*-

from flask import Blueprint, session, render_template, request, g, url_for, redirect, flash
from werkzeug.security import check_password_hash, generate_password_hash

from library import db
from library.users.models import User
from library.users.forms import LoginForm, RegisterForm
from library.users.decorators import requires_login

user_app = Blueprint('users', __name__, url_prefix='/users', static_folder="static")


@user_app.before_app_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


def login_user(user):
    session['user_id'] = user.id
    g.user = user


@user_app.route('/profile/')
@requires_login
def profile():
    return render_template('users/profile.html', user=g.user)


@user_app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are logged in as %s' % (user.name,))
            next_url = request.form.get('next', None) or url_for('users.profile')
            return redirect(next_url)
        flash('Wrong email or password', 'error-message')
    return render_template('users/login.html', form=form)

@user_app.route('/logout/', methods=['GET', 'POST'])
def logout():
    session.pop('user_id', None)
    next_url = request.args.get('next', None) or request.form.get('next', None) or '/'
    return redirect(next_url)



@user_app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(u'Вы зарегестрированы')
        return redirect(request.form.get('next', '') or url_for('users.profile'))
    return render_template('users/register.html', form=form)
