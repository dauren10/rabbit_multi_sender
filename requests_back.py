from time import sleep
import pika
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
for i in range(10):
    channel.basic_publish(exchange='', routing_key='hello2', body='{"id":"111111"}')
    print(" [x] Sent 'Hello World from back!'")
    sleep(3)
connection.close()