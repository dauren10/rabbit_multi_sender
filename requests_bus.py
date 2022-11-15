from time import sleep
import pika
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
for i in range(10):
    channel.basic_publish(exchange='', routing_key='hello', body='{"id":"222222"}')
    print(" [x] Sent 'Hello World from bus!'")
    sleep(3)
connection.close()