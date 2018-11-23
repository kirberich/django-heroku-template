# Django Heroku template

This is just my personal project template for heroku django projects.

## Setup

* Create a virtualenv
* Install dependencies via `pip install -r requirements.txt`
* Create a .env file (see .env.example)
* Run `./manage.py migrate`
* Create a superuser via `django-admin createsuperuser`
* Run `./mananage.py runserver`

## Notes

* `interfaces/admin/__init__.py` unregisters the `Group` admin by default as I rarely use groups.
* pytest.ini excludes any python classes because the example model is currently called TestModel, which confuses python.
