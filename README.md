# Labper

Lab Management system

## How to Use

To use this project, follow these steps:

- Make a `.env` file having same structure as `.env.sample`

- Install pipenv using,
```bash
pip install pipenv
```

- Run pipenv shell
```bash
pipenv shell
```

- Install dependencies
```bash
pipenv install
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
