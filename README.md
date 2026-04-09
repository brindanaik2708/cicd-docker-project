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
