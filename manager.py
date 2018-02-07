#!/usr/bin/env python3.6
from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
# from app.model import Posts

# The config we'll be running the app on
app = create_app('dev')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('serve', Server)
manager.add_command('shiro', MigrateCommand)


@manager.command
def test():
    # Running tests
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, Posts=Posts)


if __name__ == '__main__':
    manager.run()
