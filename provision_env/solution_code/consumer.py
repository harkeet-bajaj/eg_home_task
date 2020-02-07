from kafka import KafkaConsumer
import datetime
from datetime import datetime, timezone
from dateutil import parser

bootstrap_servers = ['192.168.30.101:9092']
topicName = 'input'
consumer = KafkaConsumer (topicName, bootstrap_servers = bootstrap_servers, auto_offset_reset = 'earliest')


try:
    for message in consumer:
        msg = bytes.decode(message.value)
        msg = int(msg)
        msg = msg / 1000.0
        t = datetime.fromtimestamp(msg).astimezone()
        print (t.isoformat())

except KeyboardInterrupt:
    sys.exit()