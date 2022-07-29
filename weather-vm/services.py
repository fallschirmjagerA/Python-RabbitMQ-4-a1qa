import psycopg2
import json
from constatns import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD


def execute_query(query, select=False):
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                          password=DB_PASSWORD, host=DB_HOST) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        if select:
            return cursor.fetchone()


def log_to_db(data):
    print('Data received!')
    from weather_INFO import City, WeatherInfo

    data = json.loads(data.replace("'", '"'))

    if not City.is_exist(data.get('id')):
        City(data.get('name'), data.get('id')).save()

    WeatherInfo(
        city_id=data.get('id'),
        max_temp=data.get('main').get('temp_max'),
        min_temp=data.get('main').get('temp_min'),
        pressure=data.get('main').get('pressure')
    ).save()


