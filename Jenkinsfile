pipeline {
    agent any
    
    stages {
        stage('Get Code') {
            steps {
                echo 'Downloading code from GitHub...'
                git branch: 'master', 
                credentialsId: '', 
                url: 'https://github.com/rkhaaleed-ship-it/3-tier-Architecture-using-Docker.git'
            }
        }
        
        stage('Check Files') {        
            steps {
                sh 'ls -la'
                sh 'find . -name "*.yml" -o -name "*.yaml"'
            }
        }
        
        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }
        
        stage('Deploy App') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        
        stage('Check Status') {
            steps {
                sh 'docker ps'
                sh 'docker-compose ps'
                sh 'sleep 10'
                sh 'curl -f http://localhost:5000/ || echo "Application starting..."'
            }
        }
    }
    
    post {
        always {
            echo 'Jenkins pipeline finished!'
        }
    }
}
