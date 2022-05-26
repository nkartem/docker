FROM amazonlinux
#FROM amazonlinux:devel-with-sources

#COPY . /home/user/myapp
#WORKDIR /home/user/myapp

# RUN yum install -y amazon-linux-extras
RUN yum -y update
RUN yum -y groupinstall "Development Tools" 
RUN yum -y install openssl-devel bzip2-devel libffi-devel wget 
RUN wget -P /opt/ https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz 
RUN cd /opt/ && tar xvf Python-3.6.6.tgz 
RUN cd /opt/Python-3.6.6/ && ./configure --enable-optimizations 
RUN cd /opt/Python-3.6.6/ && make altinstall 
RUN cd /opt/ && curl -O https://bootstrap.pypa.io/pip/3.6/get-pip.py 
RUN cd /opt/ && python3.6 get-pip.py 
RUN pip install ujson==1.35 
RUN pip install numpy==1.15.4 
RUN pip install pika 
RUN pip install wget 
RUN pip install --upgrade ta
RUN pip install pandas==0.24.2 
RUN pip install scipy==1.1.0 
RUN pip install Werkzeug==0.14.1 
RUN pip install svglib==1.1.0 
RUN pip install opencv-python==4.1.1.26
RUN pip install keras==2.2.4
RUN pip install tensorflow==1.12.0
RUN pip install CairoSVG==2.2.1
RUN pip install pdfrw
RUN pip install PyPDF2
RUN pip install reportlab==3.5.13
RUN pip install Flask==1.0.2
RUN pip install Flask-Login==0.4.1
RUN pip install scikit-image==0.14.0
RUN pip install scikit-learn==0.20.1
RUN pip install xgboost==0.80
RUN cd /opt/ && wget https://repo.anaconda.com/archive/Anaconda2-5.2.0-Linux-x86_64.sh && chmod +x Anaconda2-5.2.0-Linux-x86_64.sh
# RUN cd /opt/ && ./Anaconda2-5.2.0-Linux-x86_64.sh

# RUN git clone https://github.com/bukosabino/ta
# RUN https://pypi.org/project/scipy/1.1.0/ 


# EXPOSE 8080
#CMD [ "/bin/bash" ]

## docker run -it ai -c "cd /opt/ && ./Anaconda2-5.2.0-Linux-x86_64.sh"