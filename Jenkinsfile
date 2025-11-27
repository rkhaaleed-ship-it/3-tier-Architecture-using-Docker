pipeline {
    agent any
    
    environment {
        APP_NAME = "3tier-app"
    }
    
    stages {
        stage('Get Code') {
            steps {
                echo 'Downloading code from GitHub...'
                git branch: 'master', 
                credentialsId: '', 
                url: 'https://github.com/rkhaaleed-ship-it/3-tier-Architecture-using-Docker.git'
            }
        }
        
        stage('Setup Kubernetes Secrets') {
            steps {
                echo 'Creating Kubernetes Secrets...'
                sh '''
                    kubectl create secret generic mysql-secrets \
                        --from-literal=mysql-root-password=mysecret123 \
                        --from-literal=mysql-database=appdb \
                        --dry-run=client -o yaml | kubectl apply -f -
                    
                    kubectl get secrets
                '''
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying application to Kubernetes...'
                sh '''
                    kubectl apply -f my-app.yaml
                    
                    sleep 30
                    
                    kubectl get pods
                    kubectl get services
                '''
            }
        }
        
        stage('Verify Deployment') {
            steps {
                echo 'Verifying application deployment...'
                sh '''
                    kubectl get pods -o wide
                    echo "--- Services ---"
                    kubectl get services
                    echo "--- Secrets ---"
                    kubectl get secrets
                    
                    kubectl port-forward service/backend-service 5000:5000 &
                    sleep 5
                    curl -s http://localhost:5000/ || echo "Backend is starting..."
                    pkill kubectl
                '''
            }
        }
        
        stage('Setup Ingress') {
            steps {
                echo 'Setting up Ingress...'
                sh '''
                    kubectl apply -f ingress.yaml
                    
                    kubectl get ingress
                '''
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed!'
            sh '''
                echo "=== Final Status ==="
                kubectl get pods
                echo "=== Application URLs ==="
                echo "Frontend: http://localhost"
                echo "Backend API: http://localhost/api"
            '''
        }
        success {
            echo 'Pipeline succeeded! Application deployed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check logs above for details.'
        }
    }
}
