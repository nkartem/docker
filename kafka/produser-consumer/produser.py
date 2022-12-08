from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['192.168.1.104:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
for e in range(7):
    data = {'Message TEST' : e}
    producer.send('myTopic', value=data)
    print (data)
    sleep(2)