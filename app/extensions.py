# SQLAlchemy for database
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Flask-WTF for CSRF tokens
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()