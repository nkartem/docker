from time import sleep
from json import dumps
from kafka import KafkaProducer
from datetime import datetime
import ssl


dt = datetime.now() # current date and time
dt1 = dt.strftime("%d-%m-%Y, %H:%M:%S")
print (dt1)
print (type(dt1))
my_dt1_as_bytes = str.encode(dt1)


# SSL Configuration
ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ssl_context.load_cert_chain(certfile='C:\\Users\\username\\Documents\\GitHub\\docker\\kafka\\produser-consumer\\ssl-pem\\kafka.broker.cert.pem', keyfile='C:\\Users\\username\\Documents\\GitHub\\docker\\kafka\\produser-consumer\\ssl-pem\\kafka.broker.key.pem', password='123456')
ssl_context.load_verify_locations(cafile='C:\\Users\\username\\Documents\\GitHub\\docker\\kafka\\produser-consumer\\ssl-pem\\ca.cert.pem')
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
ssl_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 # Disable old TLS versions
#ssl_context.options |= ssl.OP_CIPHER_SERVER_PREFERENCE  # Prefer the server's choice of ciphers
ssl_context.set_ciphers("HIGH:!aNULL:!eNULL:!EXPORT:!DES:!MD5:!PSK:!RC4:!CAMELLIA:!SEED:!IDEA:!3DES")  # Set a strong cipher suite
ssl_context.ssl_version = ssl.PROTOCOL_TLSv1_2 


producer = KafkaProducer(bootstrap_servers=['192.168.11.154:9094'],
                         ###### SECURITY PLAIN #####
                        #  security_protocol = 'SASL_PLAINTEXT',
                        #  sasl_mechanism = 'PLAIN',
                        #  sasl_plain_username = 'admin',
                        #  sasl_plain_password = 'admin-secret',
                         ###########################
                         ####### SECURITY SSL #########
                         security_protocol = 'SSL',
                         ssl_context=ssl_context,
                         #############################
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
for e in range(7):
    data = {'Message TEST1' : e}
    DataHeaders =  [("Header Key", my_dt1_as_bytes)] 
    producer.send('test-topic', headers=DataHeaders, value=data )
    print (data)
    sleep(1)