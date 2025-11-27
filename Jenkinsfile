pipeline {
    agent any
    stages {
        stage('Get Code') {
            steps {
                git branch: 'master', url: 'https://github.com/rkhaaleed-ship-it/3-tier-Architecture-using-Docker.git'
            }
        }
        stage('Setup Docker Compose') {
            steps {
                sh 'cp ./database-mysql/docker-compose.yml ./docker-compose.yml'
            }
        }
        stage('Build and Deploy') {
            steps {
                sh 'docker-compose up --build -d'
            }
        }
        stage('Verify') {
            steps {
                sh 'docker ps'
                sh 'sleep 10 && curl http://localhost:5000 || true'
            }
        }
    }
}
