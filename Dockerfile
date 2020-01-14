FROM ubuntu:18.04
#LABEL maintainer="admin@agricom.com.ua"
## обновление
RUN apt -y update
# Открываем и запускаем АПАЧЕ
RUN apt -y install apache2
#ENTRYPOINT /usr/sbin/httpd –D FOREGROUND
# Открываем порты http://localhost:8000
EXPOSE 8000

#запуск docker run -it -p 8000:80 ИМЯ_ОБРАЗА
