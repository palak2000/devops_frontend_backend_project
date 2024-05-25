pipeline {
    agent any
    environment {
        DOCKERHUB_REPO = 'devops_frontend_backend_project/flask-app'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "this stage is passed"
                // git branch: 'main', url: 'https://github.com/your-repo/flask-app.git', credentialsId: 'Docker_pass'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    def app = docker.build("${env.DOCKERHUB_REPO}:${env.BUILD_ID}")
                }
            }
        }
        
        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove any existing container
                    sh '''
                    docker stop flask-app || true
                    docker rm flask-app || true
                    '''

                    // Run the new container
                    sh "docker run -d --name flask-app -p 5000:5000 ${env.DOCKERHUB_REPO}:${env.BUILD_ID}"
                }
            }
        }
    }

    post {
        success {
            echo 'Application deployed successfully!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
