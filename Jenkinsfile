pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/fvrobles/app-project-backend.git'
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t backend .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yml'
            }
        }
    }
}
