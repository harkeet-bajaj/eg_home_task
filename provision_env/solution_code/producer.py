from kafka import KafkaProducer
from time import gmtime, strftime, sleep
from json import dumps
import time

#producer = KafkaProducer(bootstrap_servers='192.168.30.101:9092')
producer = KafkaProducer(bootstrap_servers=['192.168.30.101:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
# producer.send('sample', b'Hello, World!')
# producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')

# for e in range(1000):
#     data = {'number' : e}
#     producer.send('numtest', value=data)
#     sleep(5)

# from time import gmtime, strftime
# import time
# import datetime

while True:
    eptime = int(round(time.time() * 1000))
    producer.send('input', value=eptime)
    #print(eptime)
    time.sleep(1)
