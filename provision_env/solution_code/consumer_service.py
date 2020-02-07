from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import dumps
import datetime
from datetime import datetime, timezone
from dateutil import parser

bootstrap_servers = ['192.168.30.101:9092']
topicName = 'input'
consumer = KafkaConsumer (topicName, bootstrap_servers = bootstrap_servers, auto_offset_reset = 'earliest')
producer = KafkaProducer(bootstrap_servers = ['192.168.30.101:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
producer.send('output', b'Hello, World!')
producer.send('output', key=b'message-two', value=b'This is Kafka-Python output')


for message in consumer:
        msg = bytes.decode(message.value)
        msg = int(msg)
        msg = msg / 1000.0
        t = datetime.fromtimestamp(msg).astimezone()
        out = t.isoformat()
        print (out)
        producer.send('output', value=out)