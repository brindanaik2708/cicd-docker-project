# 🚀 Flask CI/CD Deployment on AWS EC2

A production-style DevOps project demonstrating end-to-end deployment of 
a Dockerized Flask application using GitHub Actions and AWS EC2.

## 🌍 Live Demo

http://54.227.96.95:5000

## ⚙️ Tech Stack

* Python (Flask)
* Docker
* AWS EC2 (Amazon Linux)
* GitHub Actions (CI/CD)
* Linux (SSH, server management)

## 📌 Features

* Dockerized Flask application
* Automated CI/CD pipeline using GitHub Actions
* Auto deployment to AWS EC2 on every push
* Publicly accessible live application
* Secure SSH-based deployment

## 🏗️ Architecture

GitHub → GitHub Actions → Docker Hub → AWS EC2 → Live Application


## 🔄 CI/CD Workflow

1. Code pushed to GitHub
2. GitHub Actions builds Docker image
3. Image pushed to Docker Hub
4. EC2 pulls latest image
5. Old container stopped and removed
6. New container deployed automatically

## 🐳 Docker Setup

# Build image
docker build -t your-docker-username/flask-app .

# Run container
docker run -d -p 5000:5000 your-docker-username/flask-app

## ☁️ AWS EC2 Setup

* Instance Type: t2.micro / t3.micro (Free Tier)
* OS: Amazon Linux 2023
* Ports Open:

  * 22 (SSH)
  * 5000 (Application)

## 🔐 Environment & Secrets

GitHub Secrets used:

* EC2_HOST
* EC2_USER
* EC2_KEY
* DOCKER_USERNAME
* DOCKER_PASSWORD

## 📸 Screenshots
🌍 Live Application
![App](images/app.png)

⚙️ CI/CD Pipeline
![CI/CD](images/cicd.png)

☁️ EC2 Instance
![EC2](images/ec2.png)


## 📈 Future Improvements

* Add custom domain & HTTPS
* Use Nginx as reverse proxy
* Add monitoring & logging
* Deploy using Kubernetes

## 👨‍💻 Author

Brinda Naik

## ⭐ If you found this useful, consider giving it a star!
