# This to investigate the failing test

Failing test with `CustomUser` model, `email` field and `django.contrib.auth.views.login` view.

On the running app, everything works as expected, but tests are failing. Truly want to understand why.

# How to check
1. git clone git@github.com:almazkun/django_account.git
1. cd django_account
1. pipenv install --dev
1. pipenv run python manage.py test 
1. pipenv run python manage.py runserver

Also, demo app is available at: https://account.akun.dev/


# django_template
This is a django started template

## Changes
1. Docker Compose dev and prod setup
1. Templates 
1. Bootstrap 5
1. Logging
1. Pipenv for environment
1. .env file
1. Static files 


## Install
1. `git clone https://github.com/almazkun/django_template.git`
2. `pipenv install`
3. `pipenv shell`
4. `python manage.py startapp <app_name>`
5. `python manage.py makemigrations`
6. `python manage.py migrate`
7. `python manage.py runserver`
