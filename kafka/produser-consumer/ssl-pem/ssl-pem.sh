#!/bin/bash 
# Generate a private key for the Kafka broker:
openssl genrsa -out kafka.broker.key.pem 2048
# Generate a certificate signing request (CSR) for the broker:
openssl req -new -key kafka.broker.key.pem -out kafka.broker.csr.pem
# Generate a self-signed certificate using the CSR:
openssl x509 -req -days 365 -in kafka.broker.csr.pem -signkey kafka.broker.key.pem -out kafka.broker.cert.pem
# Generate a certificate authority (CA) certificate:
openssl req -x509 -newkey rsa:2048 -keyout ca.key.pem -out ca.cert.pem -days 365
# Export the certificate and private key to PKCS12 format:
openssl pkcs12 -export -in kafka.broker.cert.pem -inkey kafka.broker.key.pem -out kafka.broker.pkcs12.pfx

