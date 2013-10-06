from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_fount(error):
    return render_template('404.html'), 404

from library.users.views import user_app as usersModule
from library.books.views import books_app as booksModule

app.register_blueprint(usersModule)
app.register_blueprint(booksModule)