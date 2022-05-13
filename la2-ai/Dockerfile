FROM amazonlinux


RUN npm install python3
RUN pip install ujson==1.35
RUN pip install numpy==1.15.4
RUN pip install pika
RUN pip install wget
RUN git clone https://github.com/bukosabino/ta
RUN pip install pandas==0.24.2
RUN https://pypi.org/project/scipy/1.1.0/
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
RUN https://repo.anaconda.com/archive/



EXPOSE 8080
CMD [ "/bin/bash" ]