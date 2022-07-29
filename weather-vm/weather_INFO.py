from datetime import datetime
from services import execute_query

class City:
    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id

    def save(self):
        execute_query(f"insert into city(id, name) values({self.id}, '{self.name}');")


    @staticmethod
    def is_exist(id: int):

        return bool(execute_query(f'select * from city where id={id}', select=True))



class WeatherInfo:
    def __init__(self, city_id, min_temp, max_temp, pressure):
        self.city_id = city_id
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.pressure = pressure
        self.current_time = None

    def save(self):
        execute_query(
            f"INSERT INTO weather (city_id, min_temp, max_temp, pressure, added_time)"
            f"VALUES({self.city_id},{self.min_temp},{self.max_temp},{self.pressure},TIMESTAMP '{datetime.now()}')"
        )


