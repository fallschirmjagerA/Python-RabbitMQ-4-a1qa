import datetime

import requests
import pika
from constant import CITIES, WEATHER_URL, WEATHER_CHANNEL_NAME, RABBIT_HOST
import time


def send_to_queue(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_HOST))
    channel = connection.channel()
    channel.basic_publish(exchange='',
                          routing_key=WEATHER_CHANNEL_NAME,
                          body=str(data))
    connection.close()


def main():
    print(f'Requests sending -- {datetime.datetime.now()}')
    for city in CITIES:
        response = requests.get(
            WEATHER_URL + f"&lat={city.get('lat')}&lon={city.get('lon')}&exclude=minutely,hourly,daily,alerts"
        )
        if response.status_code == 200:
            send_to_queue(response.json())
        else:
            pass
    print(f'Waiting new requests -- {datetime.datetime.now()}')


if __name__ == "__main__":
    while True:
        main()
        time.sleep(300)
