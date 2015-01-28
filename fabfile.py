from fabric.api import env, run, require, cd
import os

env.hosts = ['jeremy@forthoseabouttorock.io']


def prod():
    env.webfaction_app_name = 'ftatr'
    env.deploy_target = 'prod'
    # env.remote_app_dir = '~/webapps/django/appname'
    # env.remote_apache_dir = '~/webapps/django/apache2'


def dev():
    env.webfaction_app_name = 'ftatr-dev'
    env.deploy_target = 'dev'


def deploy(branch):
    require('webfaction_app_name', provided_by=[prod, dev])
    require('deploy_target', provided_by=[prod, dev])

    print 'Deploying', branch, 'to', env.deploy_target

    app_base_dir = os.path.join('~/webapps', env.webfaction_app_name)
    # activate virtualenv
    with cd(app_base_dir):
        run('source .py-env/bin/activate')
    with cd(os.path.join(app_base_dir, 'ftatr')):
        # checkout specified version
        run("git fetch")
        run("git fetch --tags")
        run("git checkout %s" % branch)
        # install new requirements
        run("pip install -r requirements.txt")
        # collectstatic
        run("python manage.py collectstatic")
        # restart
        run(os.path.join(app_base_dir, 'apache2/bin/restart'))
