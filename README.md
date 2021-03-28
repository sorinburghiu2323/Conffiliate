# Conffiliate

## About

Conffiliate is an affiliate marketing platform where we aim to connect influencers and businesses together to 
collaborate and grow together.

## Workspaces

**NOTE:** Send Sorin your trello account name and google email to add you to it.

Trello board for tasks: https://trello.com/b/UhVmO3EG/conffiliate

Google drive: https://drive.google.com/drive/u/0/folders/1lA9QxlAJ3Zp1EZhXGPswerR02fl9SWU5

Discord server: https://discord.gg/Z5tsExZhH5

## Setup

First set up you python virtual environment and activate it.

```bash
$ python -m venv .venv

$ .venv\Scripts\activate.bat      # Windows
$ .venv\bin\activate              # Linux
```

Then install python dependencies:
```
pip install -r requirements.txt
```

Do your migrations (create your development database):
```
python manage.py migrate
```

Run the django server using:
```
python manage.py runserver
```

### Next install the VueJS frontend dependencies:

```
cd frontend
npm install
```
**NOTE:** When you pull changes that others have made, you may want to do `npm install` again to ensure any additional dependencies have been added.

Now to build the frontend, there are two ways:

Watches for any changes in the filetree and recompiles when detects a change
```
npm run watch
```

Compiles and minifies for production
```
npm run build
```

## Having a migration error?

This may be due to a database update. Simply drop you current database and create a new one as follows:
1. Delete `db.sqlite3` file
2. Run `python manage.py migrate`
