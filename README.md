# Labper

Lab Management system

## How to Use

To use this project, follow these steps:

- Make a `.env` file having same structure as `.env.sample`
- Get your G_KEY and G_SKEY by creating a project on [Google Dev Console](http://console.developers.google.com/)
- Add you client key to G_KEY and client secret key to G_SKEY.

- Install requirements:

```bash
pip install -r requirements.txt
```

- Makemigrations and migrate

```bash
python manage.py makemigrations && python manage.py migrate
```

- Create superuser

```bash
python manage.py createsuperuser
```

- Run server

```bash
python manage.py runserver
```

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate
