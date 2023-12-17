#Dockerfile

#using httpd image
FROM httpd:latest

#Update the system and Install Python
RUN apt-get update && apt-get install -y python3

#Copying created python script to the container
COPY docker.py /usr/local/apache2/

#Copy entrypoint script into the container
COPY entrypoint.sh /usr/local/bin/

#Make entrypoint script executable
RUN chmod +x /usr/local/bin/entrypoint.sh

#Set the entrypoint script as the entrypoint for the container
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
