from kafka import KafkaProducer
from time import gmtime, strftime, sleep
from json import dumps
import time
import prometheus_client as prom

producer = KafkaProducer(bootstrap_servers=['192.168.30.101:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

if __name__ == '__main__':

    counter = prom.Counter('python_evolution_producer_counter', 'This is counter to measure no of messages sent to Kafka Broker')
    prom.start_http_server(7072)
    enum = prom.Enum('python_evolution_producer_state', 'Description of Producer state',
        states=['starting', 'running', 'stopped'])
    enum.state('running')

    while True:
        eptime = int(round(time.time() * 1000))
        producer.send('input', value=eptime)
        counter.inc()
        time.sleep(1)