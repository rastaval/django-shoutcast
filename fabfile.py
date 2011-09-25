from fabric.api import *
from fabric.contrib.console import confirm

PROJECT_DIR = '$HOME/websites/django-shoutcast/shoutcast'
PROJECT_NAME = 'shoutcast'
SERVER_NAME = 'yosfm'

env.hosts = ['webapps@fridayd.me']

def pull():
    with cd(PROJECT_DIR):
        run('git pull')

def install_packages():
    with cd(PROJECT_DIR):
        with prefix('workon %s' % PROJECT_NAME):
            run('pip install -r requirements/project.txt')

def sync_database():
    with cd(PROJECT_DIR):
        with prefix('workon %s' % PROJECT_NAME):
            run('./manage.py syncdb --noinput')

def migrate_database():
    with cd(PROJECT_DIR):
        with prefix('workon %s' % PROJECT_NAME):
            run('./manage.py migrate --noinput')

def stop_server():
    sudo('supervisorctl stop %s' % SERVER_NAME)

def start_server():
    sudo('supervisorctl start %s' % SERVER_NAME)

def restart_apache():
    sudo('apache2ctl graceful')

def restart_server():
    stop_server()
    start_server()
    restart_apache()

def collect_static():
    with cd(PROJECT_DIR):
        with prefix('workon %s' % PROJECT_NAME):
            run('./manage.py collectstatic --noinput')

def addcats():
    with cd(PROJECT_DIR):
        with prefix('workon %s' % PROJECT_NAME):
            run('./manage.py addcats')

def deploy():
    with settings():
        pull()
        install_packages()
        sync_database()
        #migrate_database()
        #collect_static()
        #restart_server()
