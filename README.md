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





##### Steps: #########

[https://www.youtube.com/watch?v=NE2TZj-2wb4]

   
1.  Create a Kubernetes cluster
   
2.  Console: Search for Service Accounts
   
3.  Create a Service Account and give it Kubernetes Engine Admin Permission
   
4.  Crate JSON key, View
   
5.  Copy JSON file content to new file in home dir (remember the file name)
   
6. Authenticate with GCP using the JSON file::  gcloud auth activate-service-account --key-file=/home/naman/demo.json

       [ before proceeding with further steps check if Cloud Resource Manager API is enabled] 
   
7.  Set my project: 
       gcloud config set project youtube-demo-1234567
   
8.  Post-check:  Am I on the right project: 
       gcloud config list
   
9.  List clusters:  
       gcloud container clusters list
   
10. Post check: Who am I: 
       gcloud config list account
   
11. Show list of accounts I have auth-ed with and make sure youtube is the current one: 
       gcloud auth list  | grep youtube
   
12. Authenticate/connect-with the GKE cluster:  
       gcloud container clusters get-credentials $CLUSTER  --region $REGION --project youtube-demo-1234567
       e.g. gcloud container clusters get-credentials cluster-1 --region=us-central1-c --project=youtube-demo-1234567
            Ignore the plugin warning
   
13.   postcheck: kubectl config view | grep cluster-1
                                kubectl get nodes







Install nginx ingress controller


kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml

kubectl get pods -n ingress-nginx

kubectl get svc -n ingress-nginx

kubectl logs deploy/ingress-nginx-controller -f -n ingress-nginx




    docker build --no-cache -t palak8/flask-app-micro150:latest -f Dockerfile.app .
    docker build --no-cache -t palak8/product150:latest -f Dockerfile.product .
    docker build --no-cache -t palak8/wishlist150:latest -f Dockerfile.wishlist .
    docker build --no-cache -t palak8/cart150:latest -f Dockerfile.cart .
    docker run -d -p 5000:5000 --name flask-app-micro palak8/flask-app-micro3:latest
    docker run -d -p 5001:5001 --name product palak8/product3:latest
    docker run -d -p 5002:5002 --name wishlist palak8/wishlist3:latest
    docker run -d -p 5003:5003 --name cart palak8/cart3:latest
    docker images

    docker push palak8/product150:latest
    docker push palak8/wishlist150:latest
    docker push palak8/cart150:latest
    docker push palak8/flask-app-micro150:latest

    kubectl apply -f app-deployment.yaml
    kubectl apply -f product-deployment.yaml
    kubectl apply -f wishlist-deployment.yaml
    kubectl apply -f cart-deployment.yaml
    kubectl get all
    kubectl apply -f ingress.yaml




Task1
created docker images for flask application application, and run container of docker images using jenkins
1. application - flask(.py), template files(html)
2. dockerfile - dockerized above application 

3. Write a jenkins files which will
   a. create images and push to docker hub with the latest images tag
   b. Pull the image with latest image tag
   c. Run the docker container
   d. check if service is running on browser.


Task-2
1. application - flask(.py), template files(html)
2. dockerfile - dockerized above application 
3. create images and push to docker hub 
4. create different microservices using different deployment.yaml files 
   [use different docker images for different microservices : check the latest images tag and use in deployment.yaml files]
5. create ingress.yaml file for ingress. [before this create ingress controller, ingress class] 
6. run the aaplication using domain name mentioned in /etc/hosts which is mapped to ingress controller external ip.


Task-3
7. learn helm [using helm create all the deployment.yaml files]
8. Deploy your application using helm manually.
9. And deploy your application using jenkins
   a. once with deployment.yaml files without using helm
   b. other with deployment.yaml files created using helm

   Write a jenkins file for this which will
   a. create images and push to docker hub with the latest images tag
   b. Pull the image with latest image tag
   c. Replace the image tag in deployment.yaml files
   d. Run deployment.yaml file by creating pods for different microservices.
   e. For helm using helm update and all to update the deployment.

Task-4

Check waston x assistance website 
techton pipelines functioning. 
IBM cloud
pager duty
Terraform


docker, k8[helm], cloud(AWS,GCP), Linux, jenkins, CI/CD, terraform, scripting

CI/CD : jenkins, tekton pipelines.
monitoring - pager duty (basically when you get calls, notification for thesholds) 
IBM cloud yet to be learned





