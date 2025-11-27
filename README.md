# 3-tier-Architecture-using-Docker


One common architecture for information systems that includes a user interface and persistent storage of data is known as the three-tier architecture. A classic description of the vertical tiers is:  
Presentation - windows, reports, and so on.  
Application Logic - tasks and rules which govern the process.  
Storage - persistent storage mechanism.  
The singular quality of a three-tier architecture is the separation of the application logic into a distinct logical middle tier of software. The presentation tier is relatively free of application processing; windows forward task requests to the middle tier. The middle tier communicates with the back-end storage layer.  
Commands used 
# To build any image
``` 
sudo docker build –t <image name> <path> 
```
&nbsp;&nbsp;&nbsp;&nbsp; Used to build an image
&nbsp;&nbsp;&nbsp;&nbsp;sudo docker build –t frontend .  

# To run any image
``` 
sudo docker [commands] run 
```
&nbsp;&nbsp;&nbsp;&nbsp; -p <port to run on localhost> : <post on which it is exposed> :- port mapping    
&nbsp;&nbsp;&nbsp;&nbsp;--name <name>:- Name of the Container    
&nbsp;&nbsp;&nbsp;&nbsp;--network <network name> :- name of network  
&nbsp;&nbsp;&nbsp;&nbsp;-it :- interactive mode  
&nbsp;&nbsp;&nbsp;&nbsp;-d :- deattached mode  
 
# To delete the image
```
 sudo docker rmi <image name> 
```
&nbsp;&nbsp;&nbsp;&nbsp; -f :- forcefully delete the image 


# To Build, (re)create, start, and attache to containers for a service.
```
 sudo docker-compose up   
```

# To Stop containers and removes containers, networks, volumes, and images created by up
```
 sudo docker-compose down
```

# To delete the container
``` 
 sudo docker rm <container name>   
```
&nbsp;&nbsp;&nbsp;&nbsp; -f :- forcefully delete the container  

# Restart docker 
```
 sudo systemctl restart docker 
```
 &nbsp;&nbsp;&nbsp;&nbsp;Used to restart the docker
 
# IP address of container
```
 sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}} <container name/id> 
```
&nbsp;&nbsp;&nbsp;&nbsp;to know the ip address of container  

# Create Network
```
 sudo docker network create [options] network  
```
```
 docker network create -d bridge my-bridge-network  
```
``` 
 sudo docker network connect <network name> <container name> 
```
```
 sudo docker network inspect <network name>
```
# get MySQL database server
```
 mysql –h <ip address> -u <user name> -p <password(if any)> 
```
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<img width="640" height="380" alt="Screenshot 2025-11-24 192124" src="https://github.com/user-attachments/assets/0e5deb42-5740-4f29-a650-79db2b1d8176" />

# Table of Contents
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Overview
Setup Instructions for KinD Cluster
CI/CD Pipeline Configuration
Kubernetes Manifests and Application Architecture
Monitoring with Prometheus and Grafana
GitOps - CD with ArgoCD
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# DEVOPS add environment setup instructions for full DevOps cycle:
Added detailed environment setup documentation including:

Prerequisites for Ubuntu/WSL

Installation steps for Git

Installation and configuration of Docker & Docker Compose

Added Docker repository, GPG keys, and dependencies

Enabled Docker service and added user to docker group

Installed kubectl (latest stable), kind, and Helm

Added Ansible installation steps for upcoming Jenkins automation

This commit prepares the development environment for building the 3-tier architecture using Docker, Kubernetes (KinD), and automation tools.
# 1. Install Git and Docker (Ubuntu)
```
sudo apt update
```
```
sudo apt install -y git
```
```
sudo apt install -y ca-certificates curl gnupg
```
```
sudo install -m 0755 -d /etc/apt/keyrings
```
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
```
```
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```
```
sudo apt update
```
```
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
```
sudo systemctl enable docker
```
```
sudo systemctl start docker
```
```
sudo usermod -aG docker $USER
```
# 2. Install kubectl + kind + Helm
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```
```
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.23.0/kind-linux-amd64
chmod +x kind
sudo mv kind /usr/local/bin/
```
```
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```
# 3. Install Ansible 
```
sudo apt update
```
```
sudo apt install -y ansible
```
# Verification
```
git --version
```
```
docker --version
```
```
docker-compose version
```
```
kubectl version --client
```
```
kind --version
```
```
helm version
```
```
ansible --version
```


# 3-Tier Web Application - Docker Deployment

A complete 3-tier web application containerized with Docker and orchestrated with Docker Compose. This project demonstrates a modern DevOps workflow for containerizing multi-service applications.

## Architecture
### Prerequisites
- Docker
- Docker Compose

### Run the Application
```
git clone https://github.com/your-username/3-tier-Architecture-using-Docker.git
cd 3-tier-Architecture-using-Docker
```
# Start all services
```
docker-compose up -d
```
# Verify services are running
```
docker-compose ps
```
 # Container Details
Backend Service (backend-app)
Image: Custom Python Flask application
Port: 5000
# Environment Variables:
MYSQL_HOST=mysql-app
MYSQL_USER=root
MYSQL_PASSWORD=root123!
MYSQL_DB=testdb

# Backend Service (backend-app)
mage: Custom Python Flask application
Port: 5000
Environment Variables:
MYSQL_HOST=mysql-app
MYSQL_USER=root
MYSQL_PASSWORD=root123!
MYSQL_DB=testdb
<img width="468" height="231" alt="Picture2 pngback" src="https://github.com/user-attachments/assets/a0edd1e9-53b7-486f-b772-d31669d79950" />


# Frontend Service (frontend-app)
Image: Python HTTP server serving static HTML
Port: 3000
Features: Interactive web interface with API testing
<img width="468" height="249" alt="Picture1 png front" src="https://github.com/user-attachments/assets/5c93c5cd-f842-4253-b6e8-696e26baeec8" />

# Database Service (mysql-app)
Image: MySQL 8.0
Port: 3306
# Development
# Building Images Manually
```
cd backend-flask
docker build -t 3tier-backend:latest .
```
```
cd ../frontend-html
docker build -t 3tier-frontend:latest .
```
# Running Individual Containers

```
docker network create 3tier-network
```
# Testing
```
docker-compose ps
```
```
curl http://localhost:5000
```
```
curl http://localhost:3000
```

<img width="468" height="76" alt="Picture3 png2222" src="https://github.com/user-attachments/assets/a7c010c3-1e48-4b77-bafc-7b0ae3589ec7" />
<img width="468" height="118" alt="Picture4 png55" src="https://github.com/user-attachments/assets/c02e6efc-cda7-4e5d-9df3-18007bcad4fe" />


# Backend Dependencies Fix

# Problem
The original `requirements.txt` contained outdated and incompatible libraries that caused Docker build failures.

# Solution  
Updated to modern, compatible versions:

# Before (`backend-flask/requirements.txt`):
```
txt
flask==1.1.2
flask-Cors==3.0.8
flask-MySQLdb==0.2.0
mysqlclient==1.4.6
requests==2.23.0
jinja2==2.11.3
MarkupSafe==2.0.1
itsdangerous==2.0.1
```


  # Key Changes:
Upgraded Flask from 1.1.2 → 2.3.3
Replaced flask-MySQLdb with PyMySQL + mysql-connector-python
Updated all libraries to current stable versions
Removed redundant dependencies that come bundled with Flask


# Build Docker Images
```
docker build -t rawankhaled2/final_app:frontend-latest ./frontend
```
```
docker build -t rawankhaled2/final_app:backend-latest ./backend
```
# Push Images to Docker Hub
```
docker login
```
docker push rawankhaled2/final_app:frontend-latest
```
```
docker push rawankhaled2/final_app:backend-latest
```

# Pull Images from Docker Hub

```
docker pull rawankhaled2/final_app:frontend-latest
```
docker pull rawankhaled2/final_app:backend-latest
```
```
docker pull rawankhaled2/final_app:frontend-latest
```
<img width="956" height="467" alt="dh" src="https://github.com/user-attachments/assets/361903b5-98d5-4902-bbad-a35625598648" />


# KinD Cluster Setup
# Create KinD Cluster
# Create cluster
```
kind create cluster --name final-project --config kind-config.yaml
```
```
kubectl cluster-info
kubectl get nodes
```
# Create Kubernetes Directory 
```
mkdir -p k8s-manifests
cd k8s-manifests
```
# Database Deployment
mysql-deployment.yaml

# Backend Deployment
backend-deployment.yaml

# Frontend Deployment
frontend-deployment.yaml

# Apply Kubernetes Manifests
```
kubectl apply -f mysql-deployment.yaml
```

```
kubectl apply -f backend-deployment.yaml  
```

```
kubectl apply -f frontend-deployment.yaml
```
# Check status
```
kubectl get all
```
```
kubectl get pods
```
```
kubectl get services
```
 # Use Public Images for Testing
 
```
kubectl set image deployment/frontend-deployment frontend=nginx:alpine
```

```
kubectl set image deployment/backend-deployment backend=nginx:alpine
```

```
kubectl set image deployment/mysql-deployment mysql=mysql:5.7
```
```
kubectl get pods
```
# Test Application Access
<img width="950" height="437" alt="Screenshot 2025-11-24 190508 pngmnn" src="https://github.com/user-attachments/assets/9f076f34-29d9-4ee6-84f0-beba2bfc21bc" />

# Jenkins CI/CD 
<img width="922" height="465" alt="Screenshot 2025-11-27 182841" src="https://github.com/user-attachments/assets/91cac3b6-29ca-439f-a124-b06ed52919b2" />
<img width="949" height="463" alt="Screenshot 2025-11-27 182335" src="https://github.com/user-attachments/assets/91715fcf-c4b7-4cc5-b149-f4e4e9905e3c" />




 



ر











 
