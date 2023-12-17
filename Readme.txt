***DOCKER PROJECT***

1. Objective:
	Develop a Python script which changes the index.html file content automatically when a docker image is run.

2. Approach:
	I built a Dockerfile to run the python script in order to change the index.html file of a docker container.
	To do so, I have included 3 files
	a. Dockerfile: Dockerfile is a script containing instructions to build a docker image. Here, we can customise our image based on our requirements and can include other scripts that has to be run when the container is spun up. In this script, I have included the python and the entrypoint script.
	b. Python Script: The script includes the changes that has to be made to index.html file when we run a container.
	c. Entrypoint script: This is a bash script which allows you to provide a default behavior for your container. In my project, the entrypoint script (entrypoint.sh) is copied into the /usr/local/bin/ directory in the image, and then its permissions are modified to make it executable. Finally, the ENTRYPOINT instruction specifies that the entrypoint.sh script should be the default command to run when a container based on this image starts. I have called the python script in my entrypoint script. This will run my python script as soon as we run the docker image

3. Steps to run the files:
	-> Download all the 3 files and keep it in the same directory
	-> Make sure that the docker application installed in your system is up to date
	-> Now run the docker build command to create a docker image (NOTE: Make sure to run the cmd in the directory where Dockerfile is present)
		CMD: sudo docker build -t my_custom_httpd .
	-> The image will now be created. You can verify this by listing all the docker images
		CMD: sudo docker images
	-> Now run the created docker image in background
		CMD: sudo docker run -d -p 8080:80 my_custom_httpd
		NOTE: you can also run the image in foreground by taking out the '-d' parameter in the above command
	-> List the running containers
		CMD: sudo docker ps
	-> You can now verify the changed index.html file by entering the bash of the container
		CMD: sudo docker exec -it <Cont-id> bash
			Navigate to folder /usr/local/apache2/htdocs to view the index.html file
	-> You can also verify using curl command
		CMD: curl localhost:8080
