FROM fedora:37
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN yum -y update ; yum  -y install epel-release ; yum -y install nano wget git net-tools openssl-devel vim htop curl lame mc autoconf subversion pkg-config libtool gcc ; yum -y groupinstall "Development Tools" ; mkdir /opt/UIS

######## libsrtp ####
RUN cd /usr/src ; git clone https://github.com/cisco/libsrtp.git ; cd libsrtp/ ;  ./configure ; make ; make runtest ;make install

######### asterisk #####
RUN cd /usr/src ; wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz ; tar xvfz asterisk-18-current.tar.gz ; rm asterisk-18-current.tar.gz ; cd asterisk-18.12.1 ; ./contrib/scripts/get_mp3_source.sh ; DEBIAN_FRONTEND=noninteractive ./contrib/scripts/install_prereq install ; make distclean ; ./configure --libdir=/usr/lib64 --with-crypto --with-ssl=ssl --with-srtp ; make menuselect.makeopts ; menuselect/menuselect \
        --enable app_authenticate --enable app_cdr --enable app_celgenuserevent \
        --enable app_channelredirect --enable app_chanisavail --enable app_chanspy \
		--enable format_mp3 --enable format_wav --enable codec_ulaw  ; make ; make install ; make samples ; make basic-pbx ; ldconfig ; make install-logrotate
#######################
#COPY entrypoint.sh /usr/bin/entrypoint.sh
ENTRYPOINT [ "sh","-c", "asterisk && /bin/bash" ]
EXPOSE 5060/udp 10000-20000/udp 5022/udp
#ENTRYPOINT ["sh", "asterisk", "/bin/bash"]
#CMD ["/bin/bash", "asterisk"]

# docker build -t asterisk .
# podman run -it -p 5060:5060/udp -p 10000-20000:10000-20000/udp -p 5022:5022/udp  -v /opt/podman/asterisk:/etc/asterisk -v /home/app:/home/app docker.io/nkartem/asterisk:18.12.1-fedora37
