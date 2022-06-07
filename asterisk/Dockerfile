FROM ubuntu:20.04
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get -y update ; apt-get -y install wget git vim htop curl lame mc build-essential autoconf subversion pkg-config libtool libedit-dev gcc systemctl ; mkdir /home/UIS
# RUN apt-get -y install wget git vim htop curl lame mc build-essential autoconf subversion pkg-config libtool libedit-dev gcc systemctl 

###### jansson ###########
RUN cd /usr/src ; git clone https://github.com/akheron/jansson.git ; cd jansson ; autoreconf -i ; ./configure --prefix=/usr/ ; make ; make install

########## pjproject #####
RUN cd /usr/src ; git clone https://github.com/pjsip/pjproject.git ; cd pjproject ; ./configure CFLAGS="-DNDEBUG -DPJ_HAS_IPV6=1" --prefix=/usr --libdir=/usr/lib64 --enable-shared --disable-video --disable-sound --disable-opencore-amr ; make dep ; make ; make install ; ldconfig

######### asterisk #####
RUN cd /usr/src ; wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz ; tar xvfz asterisk-18-current.tar.gz ; rm asterisk-18-current.tar.gz ; cd asterisk-18.12.1    
RUN cd /usr/src/asterisk-18.12.1 ; DEBIAN_FRONTEND=noninteractive ./contrib/scripts/install_prereq install ; make distclean ; ./configure --libdir=/usr/lib64 ; make menuselect.makeopts ; menuselect/menuselect \
        --enable app_authenticate --enable app_cdr --enable app_celgenuserevent \
        --enable app_channelredirect --enable app_chanisavail --enable app_chanspy \
		--enable format_mp3 --enable format_wav --enable codec_ulaw  ; make ; make install ; make samples ; make config ; make basic-pbx ; echo "/usr/lib64" >> /etc/ld.so.conf.d/asterisk.conf ; ldconfig ; make install-logrotate     
########################
EXPOSE 5060/udp 10000-20000/udp 5022/udp
CMD [ "systemctl start asterisk", "/bin/bash" ]

# docker build -t asterisk .
# docker run -it -p 5060:5060/udp -p 10000-20000:10000-20000/udp -p 5022:5022/udp -v /some/folder/:/home/ asterisk  