import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

from . import settings

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = settings.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(settings.DB_USER, settings.DB_PASS,settings.DB_URL, settings.DB_NAME)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False  # prevent annoying debug thing from breaking links
db = SQLAlchemy(app)

# Configure Authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"  # tells flask where to redirect if you try to access a restricted page
login_manager.init_app(app)

# Load debug toolbar
# toolbar = DebugToolbarExtension(app)

# make timestamps look pretty
moment = Moment(app)

import models
import views
