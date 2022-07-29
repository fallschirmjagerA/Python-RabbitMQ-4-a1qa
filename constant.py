from dotenv import load_dotenv
import os


load_dotenv()


API_KEY = os.environ.get('API_KEY')

CITIES = [
    {"lat": 53.9, "lon": 27.5667},  # Minsk
    {"lat": 53.9139, "lon": 30.3364},  # Mogilev
    {"lat": 55.7522, "lon": 37.6156},  # Moscow
]

WEATHER_URL = f'https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}'

WEATHER_CHANNEL_NAME = 'WEATHER_INFO'
RABBIT_HOST = os.environ.get('RABBIT_HOST')
