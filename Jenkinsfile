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
        
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f my-app.yaml'
            }
        }
        
        stage('Check Status') {
            steps {
                sh 'sleep 10'
                sh 'kubectl get pods'
                sh 'kubectl get services'
            }
        }
    }
}
        always {
            echo 'Jenkins pipeline finished!'
        }
    }
}
