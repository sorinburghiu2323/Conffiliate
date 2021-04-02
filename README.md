# Conffiliate

## 📖 About

Conffiliate is an affiliate marketing platform where we aim to connect influencers and businesses together to 
collaborate and grow together.

## 🤝 Workspaces

**NOTE:** Send Sorin your trello account name and google email to add you to it.

[Trello board for tasks](https://trello.com/b/UhVmO3EG/conffiliate)

[Shared Google drive](https://drive.google.com/drive/u/0/folders/1lA9QxlAJ3Zp1EZhXGPswerR02fl9SWU5)

[Discord server](https://discord.gg/Z5tsExZhH5)

## 🛠️ Setup

First set up your python virtual environment.

```
python -m venv .venv
```

Then activate it with:

```
.venv\Scripts\activate.bat      # Windows
.venv\bin\activate              # Linux
```

Install python dependencies:
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

Watches for any changes in the filetree and recompiles when detects a change:
```
npm run watch
npm run serve
```

Compiles and minifies for production
```
npm run build
```

### Having a migration error?

This may be due to a database update. Simply drop you current database and create a new one as follows:
1. Delete `db.sqlite3` file
2. Run `python manage.py migrate`
