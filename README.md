# PathEditor

Django based server-tool to manage historic map data.

## Requirements
* Django
* Python 3
* pip3 Paket manager
* Postgresql database + user

## First setup
1. start postgres: `systemctl start postgres` and create a user owning a databace
2. in OHDM/settings.py search for `DATABASES` and change the USER- and NAME-field to match your database.
Finally replace the ENGINE-value with `django.db.backends.postgresql`
3. Replace the path inside `STATICFILES_DIRS` to amtch the servers architecture.
4. Use `manage.py` to populate the databse and migrate the changes.
--1. `manage.py makemigrations`
--2. `manage.py migrate`
5. Finally start the server with `manage.py runserver`

## Web UI Navigation
The three datatypes cann be accessed via the top-bar menu, which forwards to a complete list of items.
The main-URLs resolve as followed:
* `/geom/` lists Geometries
* `/obg/` lists Geometry Objects
* `/path/` lists Paths

## Further Information
can be fond in the pdf-file within the repository. It explains the API and shows example diagrams.
* https://www.postgresql.org/docs/11/index.html               Postgres Help
* https://docs.djangoproject.com/en/2.1/                      Django Help
* https://packaging.python.org/tutorials/installing-packages/ Pip Help
