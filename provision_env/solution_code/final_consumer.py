from kafka import KafkaConsumer
import datetime
from datetime import datetime, timezone
from dateutil import parser

bootstrap_servers = ['192.168.30.101:9092']
topicName = 'input'
consumer = KafkaConsumer (topicName, bootstrap_servers = bootstrap_servers, auto_offset_reset = 'earliest')
producer = KafkaProducer(bootstrap_servers = bootstrap_servers,
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for message in consumer:
        msg = bytes.decode(message.value)
        msg = int(msg)
        msg = msg / 1000.0
        t = datetime.fromtimestamp(msg).astimezone()
        out = t.isoformat()
        print (out)
        producer.send('input', value=out)