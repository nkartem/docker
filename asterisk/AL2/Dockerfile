FROM amazonlinux:latest
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN yum -y update ; yum  -y install epel-release ; yum -y install nano wget git net-tools openssl-devel vim htop curl lame mc autoconf subversion pkg-config libtool gcc ; yum -y groupinstall "Development Tools" ; mkdir /home/UIS

######## libsrtp ####
RUN cd /usr/src ; git clone https://github.com/cisco/libsrtp.git ; cd libsrtp/ ;  ./configure ; make ; make runtest ;make install

######### asterisk #####
RUN cd /usr/src ; wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz ; tar xvfz asterisk-18-current.tar.gz ; rm asterisk-18-current.tar.gz ; cd asterisk-18.12.1 ; DEBIAN_FRONTEND=noninteractive ./contrib/scripts/install_prereq install ; make distclean ; ./configure --libdir=/usr/lib64 --with-crypto --with-ssl=ssl --with-srtp ; make menuselect.makeopts ; menuselect/menuselect \
        --enable app_authenticate --enable app_cdr --enable app_celgenuserevent \
        --enable app_channelredirect --enable app_chanisavail --enable app_chanspy \
		--enable format_mp3 --enable format_wav --enable codec_ulaw  ; make ; make install ; make samples ; make basic-pbx ; ldconfig ; make install-logrotate 
#		--enable format_mp3 --enable format_wav --enable codec_ulaw  ; make ; make install ; make samples ; make config ; make basic-pbx ; echo "/usr/lib64" >> /etc/ld.so.conf.d/asterisk.conf ; ldconfig ; make install-logrotate     
#######################
EXPOSE 5060/udp 10000-20000/udp 5022/udp
#CMD [ "systemctl start asterisk", "/bin/bash" ]

# docker build -t asterisk .
# docker run -it -p 5060:5060/udp -p 10000-20000:10000-20000/udp -p 5022:5022/udp -v /some/folder/:/home/ asterisk /bin/bash