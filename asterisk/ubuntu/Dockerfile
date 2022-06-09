FROM ubuntu:20.04
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get -y update ; apt-get -y install wget git vim htop curl lame mc build-essential autoconf subversion pkg-config libtool libedit-dev gcc systemctl ; mkdir /home/UIS

######## libsrtp ####
RUN cd /usr/src ; git clone https://github.com/cisco/libsrtp.git ; cd libsrtp/ ;  ./configure ; make ; make runtest ; make install

######### asterisk #####
RUN cd /usr/src ; wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz ; tar xvfz asterisk-18-current.tar.gz ; cd asterisk-18.12.1 ; DEBIAN_FRONTEND=noninteractive ./contrib/scripts/install_prereq install ; make distclean ; ./configure --libdir=/usr/lib64 --with-crypto --with-ssl=ssl --with-srtp ; make menuselect.makeopts ; menuselect/menuselect \
        --enable app_authenticate --enable app_cdr --enable app_celgenuserevent \
        --enable app_channelredirect --enable app_chanisavail --enable app_chanspy \
		--enable format_mp3 --enable format_wav --enable codec_ulaw  ; make ; make install ; make samples ; make config ; make basic-pbx ; ldconfig ; systemctl restart asterisk
########################
EXPOSE 5060/udp 10000-20000/udp 5022/udp
# CMD [ "systemctl start asterisk", "/bin/bash" ]

# docker build -t asteriskubuntu .
# docker run -it -p 5060:5060/udp -p 10000-20000:10000-20000/udp -p 5022:5022/udp -v /some/folder/:/home/ asterisk  