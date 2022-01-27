FROM centos
RUN yum -y install epel-release
RUN yum group -y install "Development Tools"
RUN yum -y install git wget vim net-tools sqlite-devel psmisc ncurses-devel libtermcap-devel newt-devel libxml2-devel libtiff-devel gtk2-devel libtool libuuid-devel subversion kernel-devel kernel-devel-$(uname -r) crontabs cronie-anacron libedit libedit-devel
RUN cd /usr/src
RUN git clone https://github.com/akheron/jansson.git 
RUN cd jansson
RUN autoreconf -i
RUN ./configure --prefix=/usr/ 
RUN make 
RUN make install
RUN cd /usr/src
RUN git clone https://github.com/pjsip/pjproject.git
RUN cd pjproject
RUN ./configure CFLAGS="-DNDEBUG -DPJ_HAS_IPV6=1" --prefix=/usr --libdir=/usr/lib64 --enable-shared --disable-video --disable-sound --disable-opencore-amr
RUN make dep
RUN make
RUN make install
RUN ldconfig
RUN cd /usr/src
RUN wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz
RUN tar xvfz asterisk-18-current.tar.gz
RUN cd asterisk-18.9.0
RUN ./configure --libdir=/usr/lib64
RUN make menuselect
RUN
RUN
RUN
RUN
RUN
RUN
RUN
RUN
RUN