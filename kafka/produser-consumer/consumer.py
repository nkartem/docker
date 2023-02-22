from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
     bootstrap_servers=['192.168.1.5:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group-testtopic')
for message in consumer:
    print (message)
