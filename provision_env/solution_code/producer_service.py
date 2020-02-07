from kafka import KafkaProducer
from time import gmtime, strftime, sleep
from json import dumps
import time

producer = KafkaProducer(bootstrap_servers=['192.168.30.101:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


while True:
    eptime = int(round(time.time() * 1000))
    producer.send('input', value=eptime)
    time.sleep(1)