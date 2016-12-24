import json

from fired import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(255))
    phone = db.Column(db.String(15))
    fired = db.Column(db.Integer(), default=0)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    def __repr__(self):
        return '<User %r>' % self.email

    def to_json(self):
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
        }
        return json.dumps(data)

    def from_json(self, source):
        if 'username' in source:
            self.username = source['username']
        if 'email' in source:
            self.email = source['email']
        if 'phone' in source:
            self.phone = source['phone']
        if 'password' in source:
            self.password = source['password']