# https://github.com/Omid-Mohajerani/Learn-Kamailio/wiki/Kamailio-installation-on-Debian-11
FROM debian:11

#WORKDIR /home/username/
RUN mkdir /home/username/ && \
    cd /home/username/ && \
    touch /home/username/.bashrc && \
    touch /home/username/.inputrc && \
#    source .bashrc
    apt update -y && \
    apt install wget gnupg2 nano sngrep vim bash-completion -y && \
    wget -O- https://deb.kamailio.org/kamailiodebkey.gpg | apt-key add - && \
    echo "deb http://deb.kamailio.org/kamailio56 bullseye main" >> /etc/apt/sources.list && \
    echo  "deb-src http://deb.kamailio.org/kamailio56 bullseye main" >> /etc/apt/sources.list && \
    apt update -y && \
    apt install default-mysql-server -y && \
    apt install kamailio kamailio-mysql-modules  -y && \
    cp /etc/kamailio/kamctlrc /etc/kamailio/kamctlrc_org && \
    cp /etc/kamailio/kamailio.cfg /etc/kamailio/kamailio.cfg_org
#    apt-get -y install systemctl
#CMD [ "/etc/init.d/kamailio start" $$ "/etc/init.d/mariadb start" ]
EXPOSE 5060/TCP
EXPOSE 5060/UDP