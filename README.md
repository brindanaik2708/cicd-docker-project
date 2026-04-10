# End-to-End CI/CD Pipeline with Docker, GitHub Actions & AWS EC2

## Overview

This project implements a production-style CI/CD pipeline for a containerized Flask application, automating the complete software delivery lifecycle from code commit to deployment.

The architecture uses Docker for containerization, GitHub Actions for automation, Docker Hub as an image registry, AWS EC2 for deployment, and Nginx as a reverse proxy. The system is designed to ensure consistent, reliable, and secure deployments with minimal manual intervention.

## Live Application

Deployed Application (Public IP):
http://54.227.96.95

*Note: Instance may be stopped occasionally to optimize AWS usage.*

## Architecture

GitHub → GitHub Actions → Docker Hub → AWS EC2 → Nginx → Flask Container

## Technology Stack

* Flask (Python)
* Docker
* GitHub Actions (CI/CD)
* AWS EC2 (Amazon Linux 2023)
* Nginx (Reverse Proxy)
* Linux (SSH)

## CI/CD Pipeline

The pipeline is triggered automatically on every push using GitHub Actions.

### Workflow Stages

**Build**

* Docker image is created from application source code

**Push**

* Image is pushed to Docker Hub for versioning and portability

**Deploy**

* EC2 instance is accessed via SSH
* Latest Docker image is pulled
* Existing container is stopped and removed
* Updated container is deployed

This ensures a fully automated, consistent, and repeatable deployment process.

## Reverse Proxy (Nginx)

Nginx is configured as a reverse proxy to route incoming HTTP traffic from port 80 to the Flask application running inside a Docker container on port 5000.

### Why Nginx?

* Enables access via standard HTTP port (80)
* Hides internal container ports
* Provides a foundation for scaling, load balancing, and HTTPS

**Flow:**
User → Nginx (80) → Docker Container (5000)

## Docker Setup

Build image:

```bash
docker build -t brindanaik2708/flask-app .
```

Run container:

```bash
docker run -d -p 5000:5000 brindanaik2708/flask-app
```

## AWS Deployment

* Instance Type: t3.micro
* OS: Amazon Linux 2023
* Open Ports:

  * 22 (SSH)
  * 80 (HTTP)

Deployment is fully automated via CI/CD without manual intervention.

## Security Practices

* Sensitive credentials (Docker Hub login, SSH key) are stored securely using GitHub Secrets
* No credentials are hardcoded in the repository
* EC2 access is restricted via SSH key authentication
* AWS Security Groups allow only required ports (22, 80)

These practices ensure secure and controlled deployment workflows.

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

## Screenshots

* [Live Application](images/app.PNG)
* [CI/CD Pipeline](images/cicd.PNG)
* [EC2 Instance](images/ec2.PNG)

## Key Highlights

* Fully automated CI/CD pipeline with zero manual deployment
* Containerized application using Docker
* Image versioning via Docker Hub
* Secure deployment using GitHub Secrets and SSH authentication
* Reverse proxy setup using Nginx
* Cloud deployment on AWS EC2

## Future Improvements

* Custom domain with HTTPS (SSL/TLS)
* Monitoring and logging integration (Prometheus/Grafana)
* Load balancing with Nginx
* Kubernetes-based deployment

## Repository

https://github.com/brindanaik2708/cicd-docker-project

## Author

Brinda Naik
