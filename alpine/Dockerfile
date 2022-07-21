# Use existing docker image as a base
FROM alpine

# Download and install dependency
RUN apk add --update redis

# EXPOSE the port to the Host OS
EXPOSE 6379

# Tell the image what command it has to execute as it starts as a container
CMD ["redis-server"]

# docker build -t nkartem/testalpine .
# docker run -it -p 5060:5060/udp -p 10000-20000:10000-20000/udp -p 5022:5022/udp -v /some/folder/:/home/ asterisk  