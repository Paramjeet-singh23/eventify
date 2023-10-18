#!/bin/sh


# Run Django migrations
echo "Running migrations..."
python manage.py migrate

# Start the Django development server (or Gunicorn, or UWSGI, or any other server)
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
