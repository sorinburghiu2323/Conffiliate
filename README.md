# Affiliate

## To use
Pre-requisites:
1. Python at least 3.8.3
2. Django at least 3.1

## How to use
To create a new database (migrate) - There shouldn't be need for this as there
is already a database:
```
python manage.py migrate
```

A superuser is created in the current database 'db.sqlite3', but if this is to be
deleted, another superuser should be created with:
```
python manage.py createsuperuser
```
Go into the file path of the first Affiliate folder with all the content.
To run the server:
```
python manage.py runserver
```

## Experiencing migration errors
If you are getting any kind of migration/table missing error, you might need to
drop the current database and create a new one.

Do not do this without checking with someone in production.

To drop your database, simply delete 'db.sqlite3' file.
Then run:
```
python manage.py migrate
```