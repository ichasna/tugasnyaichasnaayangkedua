release: sh -c 'python manage.py migrate && python manage.py loaddata initial_data_watchlist.json'
web: gunicorn project_django.wsgi --log-file -