# 🌍 Country-Based News Portal

A Flask-based web app that fetches top news headlines by country using the NewsAPI. The project uses Docker for containerization and Jenkins for CI/CD, deployed on an AWS EC2 instance (Amazon Linux 2).

## 🚀 Features
- Select a country to get real-time news
- Flask backend using NewsAPI
- Dockerized app
- CI/CD with Jenkins
- Hosted on Amazon EC2 (Amazon Linux 2)

## 🛠️ Tech Stack
- Python Flask
- Docker
- Jenkins
- AWS EC2
- NewsAPI.org

## 🧪 Local Development
```bash
git clone https://github.com/Vimal9059/flask-news-portal.git
cd flask-news-portal
docker build -t flask-news-app .
docker run -p 5000:5000 flask-news-app

