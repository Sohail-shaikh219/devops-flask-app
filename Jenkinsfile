pipeline {
    agent any
    environment {
        IMAGE = "flask-app:${env.BUILD_NUMBER}"
    }
    stages {
        stage('Checkout Code') {
            steps {
                // If you have GitHub repo, use:
                // git 'https://github.com/<your-github-username>/devops-flask-app.git'
                // Otherwise, skip Git and build from local workspace:
                echo 'Using local workspace for build...'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                if [ "$(docker ps -aq -f name=flask-container)" ]; then
                    docker stop flask-container || true
                    docker rm flask-container || true
                fi
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d --name flask-container -p 5000:5000 $IMAGE'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
