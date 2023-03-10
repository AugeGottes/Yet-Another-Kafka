#!/usr/bin/env python
import pika, sys, os
from pika.exchange_type import ExchangeType
from broker import broker
from broker1 import broker_message
from broker2 import broker_message
from broker3 import broker_message

topic =input("Enter topic")
if topic=="":
    topic=broker_message()
def message_received(ch,method,properties,body):
    print(f"Received message{body}")


connection_parameters=pika.ConnectionParameters('localhost')

connection=pika.BlockingConnection(connection_parameters)

channel=connection.channel()


channel.exchange_declare(exchange='routing',exchange_type=ExchangeType.direct)

queue=channel.queue_declare(queue='',exclusive=True)

channel.queue_bind(exchange='routing',queue=queue.method.queue,routing_key=topic)#topic needs to be modified (topic is decided in producer)

channel.basic_consume(queue=queue.method.queue,auto_ack=True,on_message_callback=message_received)

channel.start_consuming()


