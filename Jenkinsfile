pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Vimal9059/flask-news-portal.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-news-app .'
            }
        }
        stage('Deploy Container') {
            steps {
                sh 'docker stop flask-news-app || true'
                sh 'docker rm flask-news-app || true'
                sh 'docker run -d -p 9999:9999 --name flask-news-app flask-news-app'
            }
        }
    }
}

