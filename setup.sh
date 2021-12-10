# migrate tables
python manage.py migrate

# create super user
DJANGO_SUPERUSER_PASSWORD=root@123 python manage.py createsuperuser --noinput --username root --email test@test.com