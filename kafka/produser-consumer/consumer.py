from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'myTopic',
     bootstrap_servers=['192.168.1.104:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group-myTopic')
for message in consumer:
    print (message)