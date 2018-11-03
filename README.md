# Labper

Lab Management system

## How to Use

To use this project, follow these steps:

- Make a `.env` file having same structure as `.env.sample`
- Get your G_KEY and G_SKEY by creating a project on [Google Dev Console](http://console.developers.google.com/)
- Add you client key to G_KEY and client secret key to G_SKEY.
- Fill up the following entries in .env

```bash
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=YourEmail
EMAIL_HOST_PASSWORD=YourPassword
```

- You have to enable access by insecure apps in your respective email serivce provider.

- Install requirements:

```bash
pip install -r requirements.txt
```

- Makemigrations and migrate the Database to populate the table

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

One click easy deployment.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=http://github.com/aashutoshrathi/labper)
