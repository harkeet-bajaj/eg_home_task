from kafka import KafkaConsumer
import sys
bootstrap_servers = ['192.168.30.101:9092']
topicName = 'output'
consumer = KafkaConsumer (topicName, bootstrap_servers = bootstrap_servers, auto_offset_reset = 'earliest')

try:
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
except KeyboardInterrupt:
    sys.exit()