# End-to-End CI/CD Pipeline with Docker, GitHub Actions & AWS EC2

## Overview

This project demonstrates the design and implementation of a production-style CI/CD pipeline for a Flask-based web application. The pipeline automates the entire workflow from code integration to deployment, ensuring consistent and reliable delivery.

The application is containerized using Docker, automated using GitHub Actions, and deployed on an AWS EC2 instance. Nginx is configured as a reverse proxy to expose the application on a standard HTTP port, simulating real-world deployment architecture.

---

## Technology Stack

* Backend: Flask (Python)
* Containerization: Docker
* CI/CD: GitHub Actions
* Cloud Platform: AWS EC2 (Amazon Linux 2023)
* Web Server: Nginx (Reverse Proxy)
* Version Control: Git & GitHub

---

## CI/CD Workflow

The pipeline is triggered automatically on every push to the repository:

1. Code is pushed to GitHub
2. GitHub Actions builds a Docker image
3. Basic application checks are executed
4. Image is pushed to Docker Hub
5. EC2 instance pulls the latest image
6. Existing container is stopped and removed
7. New container is deployed automatically

This eliminates manual deployment steps and ensures consistency across updates.

---

## Reverse Proxy (Nginx)

Nginx is configured as a reverse proxy to route incoming HTTP traffic from port 80 to the Flask application running inside a Docker container on port 5000.

This allows the application to be accessed without specifying a port and reflects a production-style setup.

**Request Flow:**
User → Nginx (Port 80) → Docker Container (Port 5000)

---

## Docker Implementation

* Created a Dockerfile to containerize the Flask application
* Ensured consistent runtime environment across development and deployment
* Simplified application execution using container-based architecture

---

## AWS Deployment

* Deployed application on an EC2 instance (t3.micro)
* Configured inbound rules for HTTP (80) and SSH (22)
* Managed server via SSH and automated deployment through CI/CD

---

## Project Structure

```
cicd-docker-project/
│── app.py
│── requirements.txt
│── Dockerfile
│── .github/workflows/
│   └── ci-cd.yml
│── images/
```

---

## Running Locally

### Clone repository

```
git clone https://github.com/brindanaik2708/cicd-docker-project.git
cd cicd-docker-project
```

### Build Docker image

```
docker build -t flask-app .
```

### Run container

```
docker run -p 5000:5000 flask-app
```

### Access application

```
http://localhost:5000
```

---

## Key Features

* Automated CI/CD pipeline for build and deployment
* Docker-based containerized application
* Cloud deployment on AWS EC2
* Reverse proxy configuration using Nginx
* Zero-manual deployment workflow
* Reproducible and scalable setup

---

## Learning Outcomes

* Hands-on experience with CI/CD pipeline design
* Practical use of Docker for containerization
* Deployment and server management on AWS EC2
* Automation using GitHub Actions
* Debugging real-world deployment issues

---

## Screenshots

* [Live Application](images/app.PNG)
* [CI/CD Pipeline](images/cicd.PNG)
* [EC2 Instance](images/ec2.PNG)

---

## Repository

https://github.com/brindanaik2708/cicd-docker-project

---

## Note

This project is built for learning and demonstration purposes. Further enhancements such as HTTPS configuration, load balancing, monitoring, and container orchestration can be implemented for production-grade systems.






















# Flask CI/CD Deployment on AWS EC2

End-to-end deployment of a containerized Flask application using an automated CI/CD pipeline. Every code push triggers build, image push, and deployment to a live AWS EC2 instance.

## Live Application

http://54.227.96.95

## Technology Stack

* Flask (Python)
* Docker
* AWS EC2 (Amazon Linux 2023)
* GitHub Actions (CI/CD)
* Nginx (Reverse Proxy)
* Linux (SSH)

## Key Features

* Containerized Flask application using Docker
* Automated CI/CD pipeline using GitHub Actions
* Automatic deployment on every push
* Reverse proxy setup using Nginx (production-style)
* Publicly accessible live application
* Zero-manual deployment workflow

## Architecture

GitHub → GitHub Actions → Docker Hub → AWS EC2 → Nginx → Flask Container

## CI/CD Workflow

1. Code pushed to GitHub
2. GitHub Actions builds Docker image
3. Image pushed to Docker Hub
4. EC2 pulls latest image
5. Existing container stopped and removed
6. New container deployed automatically

## Reverse Proxy (Nginx)

Configured Nginx as a reverse proxy to route HTTP traffic from port 80 to the Flask application running inside a Docker container on port 5000.

This allows users to access the application without specifying a port.

Flow:
User → Nginx (Port 80) → Flask App (Port 5000)

## Docker Commands (Local)

Build image:

```bash
docker build -t brindanaik2708/flask-app .
```

Run container:

```bash
docker run -d -p 5000:5000 brindanaik2708/flask-app
```

## AWS EC2 Configuration

* Instance Type: t3.micro
* OS: Amazon Linux 2023
* Open Ports:

  * 22 (SSH)
  * 80 (HTTP)
  * 5000 (optional)

## Environment Variables / Secrets

* EC2_HOST
* EC2_USER
* EC2_KEY
* DOCKER_USERNAME
* DOCKER_PASSWORD

## Screenshots

* [Live Application](images/app.PNG)
* [CI/CD Pipeline](images/cicd.PNG)
* [EC2 Instance](images/ec2.PNG)

## Future Improvements

* Custom domain with HTTPS
* Nginx load balancing
* Monitoring and logging (Prometheus/Grafana)
* Kubernetes deployment

## Author

Brinda Naik
