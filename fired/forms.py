from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

from models.user.models import User


class LoginForm(Form):
    username = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log In')


class SignupForm(Form):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name')
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                                 EqualTo('password2', message='Passwords must match')
                             ])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Length(1, 120), Email()])
    type = RadioField('Type', choices=[
        ('student', 'Student'),
        ('landlord', 'Landlord')],
        default='student', validators=[DataRequired()])

    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('This email address is already in use')

    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('This username is already taken')
