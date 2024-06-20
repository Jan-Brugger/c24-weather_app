# Weather-App
Application that stores weather information and make it accessible over HTTP REST

## Getting started

These instructions will get you a copy of the project up and running on your local machine

### Requirements

* python 3.12
* Docker

### Installing

Use proper python version:

    pyenv local 3.12

Create virtual environment:

    python3 -m venv ./venv

Activate virtual environment:

    source ./venv/bin/activate

Install dependencies

    pip install --upgrade pip
    pip install -r requirements/requirements-dev.txt

Install pre-commit hooks

    pre-commit install


### Run application

Start database

    docker compose up -d

Migrate tables

     python manage.py makemigrations && python manage.py migrate

Run application

    python manage.py runserver 8001
