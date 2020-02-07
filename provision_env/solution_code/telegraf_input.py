from kafka import KafkaConsumer
import json
import sys
bootstrap_servers = ['192.168.30.101:9092']
topicName = 'input'
consumer = KafkaConsumer (topicName, bootstrap_servers = bootstrap_servers, auto_offset_reset = 'earliest')

c = 0
for message in consumer:
        message = bytes.decode(message.value);
#        json_body = {"input_topic": f'"{message}"'}
#        print(json_body)
#        print(json.dumps({"name": message}))
        print('example,tag1=%s i=102i' % message)
        c = c + 1
        if c == 10:
            break


 [[inputs.exec]]
  commands = ["/bin/python3.6 /tmp/tgf/consumer.py"]
  timeout = "5s"
  data_format = "influx"

 [[outputs.prometheus_client]]
#   ## Address to listen on
   listen = ":9273"