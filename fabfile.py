from fabric.api import lcd, local


DEV_ROOT = '/home/shoeree/projects/vla/'
APP_ROOT = '/app/django.vancouverlifeguards.com/vla/'
GIT_URL  = 'git@github.com:shoeree/vla.git'

def update_dev():
    with lcd(DEV_ROOT):
        try:
            local('git checkout dev')
        except:
            pass
        local('git pull origin -- dev')

def prepare():
    with lcd(DEV_ROOT):
        local('python manage.py test vla')
        try:
            local('git add -p && git commit')
            local('git push origin -- dev')
        except:
            print "*** Commit is unnecessary."
            pass # do nothing if commit is not needed
        local('git checkout master')
        local('git merge dev')
        local('python manage.py test vla')

def start_uwsgi():
    with lcd(APP_ROOT):
        local('uwsgi --ini uwsgi.ini')

def stop_uwsgi():
    with lcd(APP_ROOT):
        uwsgi_ini = open('uwsgi.ini')
        pid_file = [line.split('=')[1] for line in uwsgi_ini.readlines() if line.startswith('pidfile')][0]
        local('uwsgi --stop %s' % pid_file)
        uwsgi_ini.close()

def reload_uwsgi():
    with lcd(APP_ROOT):
        uwsgi_ini = open('uwsgi.ini')
        pid_file = [line.split('=')[1] for line in uwsgi_ini.readlines() if line.startswith('pidfile')][0]
        local('kill -HUP $(cat %s)' %pid_file)
        uwsgi_ini.close()

def reload_webserver():
    local('kill -HUP $(cat /var/run/nginx.pid)')

def deploy():
    with lcd(DEV_ROOT):
        local('git checkout master')
        local('git push origin -- master')

    with lcd(APP_ROOT):
        # pull most recent commits
        local('git pull origin -- master')
        local('cp %s/vla/secret_settings.py %s/vla/' % (DEV_ROOT, APP_ROOT))
        try:
            local('python manage.py schemamigration volition --auto')
            local('python manage.py migrate volition')
        except:
            pass
        local('python manage.py test volition')
        reload_uwsgi()
        reload_webserver()
