# Дипломный проект "Доска объявлений"

### Базовая документация к проекту


* Ubuntu 20.04 LTS
* Python 3.8
* PostgreSQL 14
* Django 3.2
* Зависимости (Python) из requirements.txt

### Инструкция по запуску:
```
git clone git@github.com:AytaDzhivanov1996/ads-online.git
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
cd skymarket
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py runserver

