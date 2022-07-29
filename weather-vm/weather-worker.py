import pika
from services import log_to_db
from constatns import RABBIT_HOST, QUEUE_NAME


def callback(ch, method, properties, body):
    log_to_db(body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBIT_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

    channel.start_consuming()

if __name__=="__main__":
    main()
