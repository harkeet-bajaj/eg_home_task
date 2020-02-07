from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import dumps
import datetime
from datetime import datetime, timezone
import prometheus_client as prom

bootstrap_servers = ['192.168.30.101:9092']
topicName = 'input'
consumer = KafkaConsumer (topicName, bootstrap_servers = bootstrap_servers, 
                            auto_offset_reset = 'earliest', 
                            enable_auto_commit=True, 
                            auto_commit_interval_ms=100,
                            group_id='consumer-group')

producer = KafkaProducer(bootstrap_servers = ['192.168.30.101:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

if __name__ == '__main__':

    counter = prom.Counter('python_evolution_consumer_counter', 'This is counter to measure no of messages sent to Kafka Broker')
    prom.start_http_server(7073)
    enum = prom.Enum('python_evolution_consumer_state', 'Description of Producer state',
        states=['starting', 'running', 'stopped'])
    enum.state('running')

    for message in consumer:
            msg = bytes.decode(message.value)
            msg = int(msg)
            msg = msg / 1000.0
            t = datetime.fromtimestamp(msg).astimezone()
            out = t.isoformat()
            # print (out)
            producer.send('output', value=out)
            counter.inc()