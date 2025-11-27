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
        
        stage('Setup Files') {
            steps {
                sh '''
                    echo "Setting up project files..."
                    cp ./database-mysql/docker-compose.yml ./docker-compose.yml
                    ls -la docker-compose.yml
                    cat docker-compose.yml
                '''
            }
        }
        
        stage('Test Docker Access') {
            steps {
                sh '''
                    echo "Testing Docker access..."
                    docker version
                    docker ps
                    echo "Docker test completed"
                '''
            }
        }
        
        stage('Build Docker Images') {
            steps {
                sh '''
                    echo "Building Docker images..."
                    docker-compose build --no-cache
                    echo "Build completed successfully"
                '''
            }
        }
        
        stage('Deploy Application') {
            steps {
                sh '''
                    echo "Deploying application..."
                    docker-compose up -d
                    sleep 10
                '''
            }
        }
        
        stage('Verify Deployment') {
            steps {
                sh '''
                    echo "Verifying deployment..."
                    docker ps
                    echo "---"
                    docker-compose ps
                    echo "---"
                    curl -s http://localhost:5000 || echo "Backend not ready yet"
                    curl -s http://localhost:80 || echo "Frontend not ready yet"
                '''
            }
        }
    }
    
    post {
        always {
            echo '=== PIPELINE COMPLETED ==='
            sh 'docker-compose ps || true'
        }
    }
}
