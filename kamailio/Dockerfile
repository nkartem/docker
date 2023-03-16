FROM debian:11

# создание директории приложения
WORKDIR /home/username/
RUN apt update -y
RUN apt install wget gnupg2 -y
RUN wget -O- https://deb.kamailio.org/kamailiodebkey.gpg | apt-key add -
RUN echo "deb http://deb.kamailio.org/kamailio56 bullseye main" >> /etc/apt/sources.list
RUN echo  "deb-src http://deb.kamailio.org/kamailio56 bullseye main" >> /etc/apt/sources.list
RUN apt update -y 
RUN apt install default-mysql-server -y 
RUN apt install kamailio kamailio-mysql-modules -y  
#    yum install vim kamailio kamailio-mysql kamailio-presence kamailio-ldap kamailio-debuginfo kamailio-xmpp kamailio-unixodbc kamailio-utils kamailio-gzcompress kamailio-tls kamailio-outbound \
RUN kamailio -version 


EXPOSE 5022
#CMD [ "node", "server.js" ]