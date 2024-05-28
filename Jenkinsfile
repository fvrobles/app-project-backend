pipeline {
    agent any

    environment {
        VERSION = "1.0."+env.buildNumber
    }

    stages {
        stage('Build Docker image') {
            steps {
                sh 'docker build -t localhost:5000/backend:${VERSION} .'
            }
        }
        stage('Push Docker image') {
            steps {
                sh 'docker push localhost:5000/backend:${VERSION}'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yml'
            }
        }
    }
}
