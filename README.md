If you are running jenkins as a docker container. Then you have to install docker inside jenkins docker container.

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
