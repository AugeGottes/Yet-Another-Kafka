
import pika, sys, os
from pika.exchange_type import ExchangeType
import time
import os
import json

def broker_message():
    return 'test'
def main():
    connection_parameters=pika.ConnectionParameters('localhost')

    connection=pika.BlockingConnection(connection_parameters)

    channel=connection.channel()


    channel.exchange_declare(exchange='routing',exchange_type=ExchangeType.direct)

    queue=channel.queue_declare(queue='',exclusive=True)
    while True:
        time.sleep(1)
        print("in broker1")


    
        

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        os.remove('bk1.txt')
        os.system('python zookeeper.py')