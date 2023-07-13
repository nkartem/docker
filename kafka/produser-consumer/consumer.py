from kafka import KafkaConsumer
import ssl
import time

# SSL Configuration
ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ssl_context.load_cert_chain(certfile='C:\\Users\username\\Documents\\GitHub\\docker\\kafka\\produser-consumer\\ssl-pem\\kafka.broker.cert.pem', keyfile='C:\\Users\\username\\Documents\\GitHub\\docker\\kafka\\produser-consumer\\ssl-pem\\kafka.broker.key.pem', password='123456')
ssl_context.load_verify_locations(cafile='C:\\Users\\username\\Documents\\GitHub\\docker\\kafka\\produser-consumer\\ssl-pem\\ca.cert.pem')
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
ssl_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 # Disable old TLS versions
#ssl_context.options |= ssl.OP_CIPHER_SERVER_PREFERENCE  # Prefer the server's choice of ciphers
ssl_context.set_ciphers("HIGH:!aNULL:!eNULL:!EXPORT:!DES:!MD5:!PSK:!RC4:!CAMELLIA:!SEED:!IDEA:!3DES")  # Set a strong cipher suite
ssl_context.ssl_version = ssl.PROTOCOL_TLSv1_2 


consumer = KafkaConsumer(
    'test-topic',
     bootstrap_servers=['192.168.11.154:9094'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     ####### SECURITY SSL #########
     security_protocol = 'SSL',
     ssl_context=ssl_context,
     #############################
     group_id='my-group-testtopic')
timeout = 5  # Timeout in seconds
start_time = time.time()

while True:
    records = consumer.poll(timeout_ms=1000)
    if records:
        for tp, messages in records.items():
            for message in messages:
                print(message)

    elapsed_time = time.time() - start_time
    if elapsed_time >= timeout:
        break

consumer.close()