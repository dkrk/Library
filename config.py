import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS  = frozenset(['krkdima@gmail.com'])
SECRET_KEY = '.lS\xd8\x1a\x81\xebfR*\x9b\xb7\xefd\x94lw\x19\x13\x81%\xa6\xfd\x8f'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'db/library.db')
DATABASE_CONNECT_OPTIONS = {}


THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = '{\x90?\x9f\xf8J\xda}$\x8b\xbc\x85\x96\xe3\xb5R\xf8\xec\xb8\xac\xbb\xcc\xe4n'
