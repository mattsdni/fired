import json

from flask import Flask, render_template, url_for, request, redirect, flash, abort
from flask_script import Manager, Server

app = Flask(__name__)
app.config['SECRET_KEY'] = '8394g8934gho9w384hg8'

app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


manager = Manager(app)
manager.add_command("runserver", Server())

if __name__ == '__main__':
    manager.run()