#!/usr/bin/env python
import pika, sys, os
from pika.exchange_type import ExchangeType
# from consumer import message_received

connection_parameters=pika.ConnectionParameters('localhost')

connection=pika.BlockingConnection(connection_parameters)

channel=connection.channel()


channel.exchange_declare(exchange='routing',exchange_type=ExchangeType.direct)

queue=channel.queue_declare(queue='',exclusive=True)

def broker():
    return 'test'
