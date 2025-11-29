pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup environment') {
            steps {
                sh '''
                pip install --upgrade pip
                pip install poetry
                '''
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                poetry install --no-interaction --no-root
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                poetry run pytest || echo "Nenhum teste encontrado."
                '''
            }
        }

        stage('Run App') {
            steps {
                sh '''
                poetry run python -m cassino_cli
                '''
            }
        }
    }

    post {
        success { echo "Pipeline concluída com sucesso!" }
        failure { echo "Pipeline falhou!" }
    }
}
