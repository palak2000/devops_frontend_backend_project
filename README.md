1. If you are running jenkins as a docker container. Then you have to install docker inside jenkins docker container.

   a. Run Jenkins as a Docker Container
      
      docker run -d --name jenkins-dind --privileged --restart=unless-stopped -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:lts
   
   
   b. download Docker Pipeline Plugin
   
   
   c. Go inside docker conatainer and install docker 
      
      docker exec -u root -it jenkins bash
      
      apt-get update
      
      apt-get install -y docker.io
      
      usermod -aG docker jenkins
      
      chmod 666 /var/run/docker.sock  --> change the permission of docker socket as it will give error: permission denied while trying to connect to the Docker daemon socket


Notes: the name of the repo shoud be in small case.


2. Pushing docker image to docker hub after the docker build add docker hub credentials in the jenkins. 


3. To update any file in the git repo using git push command.

   Add token geneted through git hub in the jenkins.
   use that git token for git push command.
   In the working directory you will have the files you have cloned. 
