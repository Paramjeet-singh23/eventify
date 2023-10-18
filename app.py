from decouple import config

# Load environment variables from .env file
SECRET_KEY = config('SECRET_KEY')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
ACCESS_TOKEN_TIME_MINUTES = config('ACCESS_TOKEN_TIME_MINUTES')
REFRESH_TOKEN_TIME_MINUTES = config('REFRESH_TOKEN_TIME_MINUTES')
DJANGO_SETTINGS_MODULE = config('DJANGO_SETTINGS_MODULE')

# Use the loaded variables in your application
print("SECRET_KEY:", SECRET_KEY)
