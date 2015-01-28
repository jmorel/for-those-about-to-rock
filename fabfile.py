from fabric.api import env, run, require, cd, prefix
import os

env.hosts = ['jeremy@forthoseabouttorock.io']


def prod():
    env.webfaction_app_name = 'ftatr'
    env.deploy_target = 'prod'
    # env.remote_app_dir = '~/webapps/django/appname'
    # env.remote_apache_dir = '~/webapps/django/apache2'


def dev():
    env.webfaction_app_name = 'ftatr_dev'
    env.deploy_target = 'dev'


def deploy(branch):
    require('webfaction_app_name', provided_by=[prod, dev])
    require('deploy_target', provided_by=[prod, dev])

    print 'Deploying', branch, 'to', env.deploy_target

    app_base_dir = os.path.join('~/webapps', env.webfaction_app_name)

    # checkout specified version
    with cd(os.path.join(app_base_dir, 'ftatr')):
        run("git fetch")
        run("git fetch --tags")
        run("git checkout %s" % branch)
        run("git pull origin %s" % branch)
        run("git submodule update --init --recursive")

    with cd(app_base_dir), prefix('source .py-env/bin/activate'):
        # install new requirements
        run("pip install -r ftatr/requirements.txt")
        # collectstatic
        run("python ftatr/manage.py collectstatic --noinput")
        # restart
        run(os.path.join(app_base_dir, 'apache2/bin/restart'))
