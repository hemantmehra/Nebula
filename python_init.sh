python3 -m venv venv
. venv/bin/activate
pip install django
django-admin startproject nebula .
python manage.py migrate
