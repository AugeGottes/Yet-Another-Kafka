#!/usr/bin/env python
import pika, sys, os
from pika.exchange_type import ExchangeType


connection_parameters=pika.ConnectionParameters('localhost')

connection=pika.BlockingConnection(connection_parameters)

channel=connection.channel()

#creating the channel

channel.exchange_declare(exchange='routing',exchange_type=ExchangeType.direct)
#we are using the direct exchange type

message=input("Enter message")

topic=input("Enter topic")

channel.basic_publish(exchange='routing',routing_key=topic,body=message)
