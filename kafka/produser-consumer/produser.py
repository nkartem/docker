from time import sleep
from json import dumps
from kafka import KafkaProducer
from datetime import datetime

dt = datetime.now() # current date and time
dt1 = dt.strftime("%d-%m-%Y, %H:%M:%S")
print (dt1)
print (type(dt1))
my_dt1_as_bytes = str.encode(dt1)


producer = KafkaProducer(bootstrap_servers=['192.168.1.5:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
for e in range(7):
    data = {'Message TEST1' : e}
    DataHeaders =  [("Header Key", my_dt1_as_bytes)] 
    producer.send('test-topic', headers=DataHeaders, value=data )
    print (data)
    sleep(1)