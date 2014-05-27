from fabric.api import lcd, local


DEV_ROOT = '/home/shoeree/projects/vla/'
APP_ROOT = '/app/django.vancouverlifeguards.com/vla/'
GIT_URL  = 'https://github.com/shoeree/vla.git'

def prepare_deployment():
    with lcd(DEV_ROOT):
        local('python manage.py test vla')
        local('git add -p && git commit')

def start_uwsgi():
    with lcd(APP_ROOT):
        local('uwsgi --ini uwsgi.ini')

def reload_uwsgi():
    with lcd(APP_ROOT):
        uwsgi_ini = open('uwsgi.ini')
        pid_file = [line.split('=')[1] for line in uwsgi_ini.readlines() if line.startswith('pidfile')][0]
        local('kill -HUP $(cat %s)' %pid_file)

def deploy():
    with lcd(APP_ROOT):
        # pull most recent commits
        local('git pull')
        local('cp %s/vla/secret_settings.py %s/vla/' % (DEV_ROOT, APP_ROOT))
        local('python manage.py migrate volition')
        local('python manage.py test volition')
        reload_uwsgi()
        reload_webserver()

def reload_webserver():
    local('kill -HUP $(cat /var/run/nginx.pid)')

