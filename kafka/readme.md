
## 1. Install Kafka

To install Kafka server on RHEL  create a bash script with the next content

```
#!/bin/bash
sudo dnf install -y java-11-openjdk
cd /tmp
sudo wget https://archive.apache.org/dist/kafka/2.8.2/kafka_2.13-2.8.2.tgz
sudo tar xzf kafka_2.13-2.8.2.tgz
sudo mv kafka_2.13-2.8.2 /opt/kafka
cd /opt/kafka/

sudo tee /etc/systemd/system/zookeeper.service <<EOF
[Unit]
Description=Apache Zookeeper server
Documentation=http://zookeeper.apache.org
Requires=network.target remote-fs.target
After=network.target remote-fs.target
[Service]
Type=simple
ExecStart=/usr/bin/bash /opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties
ExecStop=/usr/bin/bash /opt/kafka/bin/zookeeper-server-stop.sh
Restart=on-abnormal
[Install]
WantedBy=multi-user.target
EOF

sudo tee /etc/systemd/system/kafka.service <<EOF
[Unit]
Description=Apache Kafka Server
Documentation=http://kafka.apache.org/documentation.html
Requires=zookeeper.service
[Service]
Type=simple
Environment="JAVA_HOME=/usr/lib/jvm/jre-11-openjdk"
ExecStart=/usr/bin/bash /opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties
ExecStop=/usr/bin/bash /opt/kafka/bin/kafka-server-stop.sh
[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now zookeeper.service
sudo systemctl enable --now kafka.service
sudo systemctl status zookeeper.service
sudo systemctl status kafka.service
sudo firewall-cmd --zone=public --permanent --add-port 9092/tcp
sudo firewall-cmd --zone=public --permanent --add-port 9093/tcp
sudo firewall-cmd --zone=public --permanent --add-port 8080/tcp
sudo firewall-cmd --reload
```


## 2. Install UI Kafka

To install UI Kafka: 
2.1. [Install docker and docker compose] (https://docs.docker.com/engine/install/rhel/)
2.2. Create folder
```	
sudo mkdir /opt/docker
cd /opt/docker
```

2.3. Create docker-compose.yaml
```
sudo nano docker-compose.yaml
```

```
version: "3"

services:
 kafka-ui:
    image: 'provectuslabs/kafka-ui:latest'
    container_name: kafka-ui
    hostname: kafka-ui
    ports:
     - '8080:8080'
    environment:
      - KAFKA_CLUSTERS_0_NAME=kafka-name-in-web
      - KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=172.1.2.3:9092
    restart: always
```

2.4. Start docker compose
```
sudo docker compose up -d
```

2.5. Open browser http://172.1.2.3:8080
![[Pasted image 20231218113242.png]]