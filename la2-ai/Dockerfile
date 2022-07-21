FROM amazonlinux

WORKDIR /home/appuser

# RUN yum install -y amazon-linux-extras
RUN yum -y update
RUN yum -y groupinstall "Development Tools" 
RUN yum -y install openssl-devel bzip2-devel libffi-devel wget libSM libXrender libXtst cairo xz-devel 
RUN wget -P /opt/ https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz 
RUN cd /opt/ && tar xvf Python-3.6.6.tgz 
RUN cd /opt/Python-3.6.6/ && ./configure --enable-optimizations && make altinstall && cd /opt/ && rm Python-3.6.6.tgz 
RUN cd /opt/ && curl -O https://bootstrap.pypa.io/pip/3.6/get-pip.py && python3.6 get-pip.py

#TODO: delete
RUN yum -y install mc 

RUN pip install ujson==1.35 
RUN pip install numpy==1.15.4 
# RUN pip install pika 
# RUN pip install wget 
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

# COPY ai-folder /home/appuser/ai-folder

COPY start.py ./
COPY CoffeeMug.jpg ./

COPY prepare.py ./

COPY test.py ./

WORKDIR /home/appuser

RUN /usr/local/bin/python3.6 /home/appuser/prepare.py
RUN /usr/local/bin/python3.6 /home/appuser/test.py

CMD ["/usr/local/bin/python3.6", "/home/appuser/start.py"]