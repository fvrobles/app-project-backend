pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                sh 'git clone https://github.com/fvrobles/app-project-backend.git'
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'eval $(minikube docker-env)'
                sh 'docker build -t backend .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'export KUBECONFIG=/var/lib/jenkins/.kube/config'
                sh 'kubectl apply -f deployment.yml'
            }
        }
    }
}
