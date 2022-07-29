import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_NAME = os.environ.get('DB_NAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

RABBIT_HOST = os.environ.get('RABBIT_HOST')
QUEUE_NAME = 'WEATHER_INFO'
