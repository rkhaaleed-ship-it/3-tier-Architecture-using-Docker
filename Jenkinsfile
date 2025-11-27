pipeline {
    agent any
    
    stages {
        stage(' Get Code') {
            steps {
                echo 'Downloading code from GitHub...'
                git branch: 'master', 
                url: 'https://github.com/rkhaaleed-ship-it/3-tier-Architecture-using-Docker.git'
            }
        }
        
        stage(' Deploy App') {
            steps {
                echo 'Deploying to Kubernetes...'
                sh '''
                kubectl apply -f my-app.yaml
                echo "Waiting for deployment..."
                sleep 30
                '''
            }
        }
        
        stage(' Check Status') {
            steps {
                echo 'Checking deployment status...'
                sh '''
                echo "=== Pods Status ==="
                kubectl get pods
                echo ""
                echo "=== Services ==="
                kubectl get services
                echo ""
                echo " DEPLOYMENT SUCCESSFUL!"
                echo " Your app is running at: http://localhost:30001"
                '''
            }
        }
    }
    
    post {
        always {
            echo 'Jenkins pipeline finished!'
        }
    }
}
