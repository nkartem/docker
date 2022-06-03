FROM amazonlinux

# RUN yum install -y amazon-linux-extras
RUN yum -y update
RUN yum -y groupinstall "Development Tools" 
RUN yum -y install wget nc htop

EXPOSE 8080/tcp
CMD ["nc -l 8080", "nc localhost 8080", "/bin/bash"]

##  docker build -t nc .
##  docker run -it -d --name=nc-serv -p 8080:8080 nc /bin/bash -c "nc -l 8080 && nc localhost 8080"
#######  docker run -it --name=nc-serv -p 8080:8080 nc nc -l 8080&&nc localhost 8080
##  docker exec -it nc-serv nc localhost 8080