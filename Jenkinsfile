pipeline {
    agent any

    stages {
        stage('Build Docker image') {
            steps {
                sh 'docker build -t localhost:5000/backend .'
            }
        }
        stage('Push Docker image') {
            steps {
                sh 'docker push localhost:5000/backend'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yml'
            }
        }
    }
}
