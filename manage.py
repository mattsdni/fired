#! /usr/bin/env python

from fired import app, db
from flask_script import Manager, prompt_bool

from fired.models.user.models import User
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to delete the whole database?"):
        db.drop_all()
        print 'Database deleted'


if __name__ == '__main__':
    manager.run()
