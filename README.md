<p align='center'> <img src="static/icons/lab.png" align="center" width="150"></p>

<h1 align="center">Labper</h1>
<h4 align="center">Lab performance evaluator</h4>

<p align="center">
<a href="https://travis-ci.com/aashutoshrathi/labper"><img src="https://img.shields.io/travis/com/aashutoshrathi/labper/master.svg?style=for-the-badge" align="center"></a>
<a href="https://heroku.com/deploy?template=http://github.com/aashutoshrathi/labper"><img src="https://www.herokucdn.com/deploy/button.svg" align="center"></a>
<img src="https://img.shields.io/pypi/pyversions/Django.svg?style=for-the-badge" align="center">
</p>


## How to Use

To use this project, follow these steps:

- Make a `.env` file having same structure as `.env.sample`
- Get your G_KEY and G_SKEY by creating a project on [Google Dev Console](http://console.developers.google.com/)
- Add you client key to G_KEY and client secret key to G_SKEY.
- Fill up the following entries in `.env`.

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

## Deployment to Pythonanywhere

- Take Python 3.7 app with Django 2.0.8.
- Clone the repository using:

  ```sh
    git clone https://github.com/aashutoshrathi/labper.git brutus 
  ```

- Go into project directory using:

  ```sh
  cd brutus
  ```

- Install requirements:

  ```sh
    pip3 install --user -r requirements.txt
  ```

- Makemigrations and collectstatic using:

  ```sh
    python3 manage.py makemigrations landing
    python3 manage.py migrate
    pytohn3 manage.py collectstatic
    python3 manage.py createsuperuser
  ```

## Deployment to Heroku

One click easy deployment.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=http://github.com/aashutoshrathi/labper)


## Author ✍️

[Team Labper](https://labper.herokuapp.com/about/)
