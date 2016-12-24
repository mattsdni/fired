import flask_login
from flask import render_template, url_for, request, redirect, flash, abort
from flask import session
from flask_login import login_user, logout_user


from . import app, db, login_manager
from . import settings
from forms import LoginForm, SignupForm
from models.user.routes import *
from models.user.models import User


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()
    return render_template('index.html', title='Fired', login_form=login_form, full_width=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.get_by_email(login_form.username.data)
        if user is not None and user.check_password(login_form.password.data):
            login_user(user, login_form.remember_me.data)
            if not user.confirmed:
                return redirect('unconfirmed')
            flash("Logged in successfully as {} {}.".format(user.fname, user.lname), 'success')
            return redirect(request.args.get('next') or url_for('index'))
        flash('Incorrect username or password.', 'danger')
    return render_template("login.html", login_form=login_form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    login_form = LoginForm()
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        user = User()
        for field in signup_form:
            if hasattr(user, field.name):
                setattr(user, field.name, field.data)
        user.password = signup_form.password.data
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('account'))
    return render_template("signup.html", login_form=login_form, signup_form=signup_form)


@app.route("/test", methods=['GET'])
def test():
    form = LoginForm()
    return render_template("test.html", login_form=form)


@app.errorhandler(400)
def bad_request(e):
    return render_template('errors/400.html'), 400


@app.errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(429)
def too_many_requests(e):
    return render_template('errors/429.html'), 429


@app.errorhandler(500)
def server_error(e):
    return render_template('errors/500.html'), 500
