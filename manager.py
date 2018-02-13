#!/usr/bin/env python3.6
from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import Blog, User

# The config we'll be running the app on
app = create_app('dev')
app = create_app('prod')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('d', Server)
# Remember to be resetting the alembic version if you get target data base is not up to date
manager.add_command('r', MigrateCommand)


@manager.command
def test():
    # Running tests
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Blog=Blog)


if __name__ == '__main__':
    manager.run()
