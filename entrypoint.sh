#!/bin/bash

#Run the python script that was copied to the docker image
python3 /usr/local/apache2/docker.py
#Run the container in foreground. 
#By default this container runs in foreground. This can be run in background by using the parameter '-d' while running the image
httpd-foreground 

#keep the container running until stopped 
tail -f /dev/null
