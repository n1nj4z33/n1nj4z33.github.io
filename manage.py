# -*- coding: utf-8 -*-
"""Management commands."""

import os
import shutil

from flask.ext.script import Manager
from n1nj4z33.main import app, freezer

manager = Manager(app)
build_dir = app.config['FREEZER_DESTINATION']

HERE = os.path.dirname(os.path.abspath(__file__))

@manager.command
def install():
    '''Installs all required packages.'''
    os.system('pip install -U -r requirements.txt')

@manager.command
def build():
    """Builds the static files."""
    print "Freezing..."
    freezer.freeze()
    print "Copying CNAME..."
    cname = os.path.join(HERE, "CNAME")
    shutil.copyfile(cname, os.path.join(build_dir, "CNAME"))
    print "...done"


@manager.command
def deploy(push=True):
    '''Deploys the site to GitHub Pages.'''
    build()
    print'Deploying to GitHub pages...'
    command = 'ghp-import -b master -m "[deploy] Build" '
    if push:
        command += '-p '
    command += build_dir
    os.system(command)
    print '...done'

if __name__ == '__main__':
    manager.run()
