# This to investigate the failing test

Failing test with `CustomUser` model, `email` field and `django.contrib.auth.views.login` view.

On the running app, everything works as expected, but test is failing. Truly want to understand why.

# How to check
1. git clone git@github.com:almazkun/django_account.git
1. cd django_account
1. pipenv install
1. pipenv run python manage.py migrate
1. pipenv run python manage.py test 
1. pipenv run python manage.py runserver

Also, demo app is available at: https://account.akun.dev/

