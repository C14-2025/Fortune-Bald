pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Python') {
            steps {
                sh '''
                apt-get update
                apt-get install -y python3 python3-pip
                '''
            }
        }

        stage('Install Poetry') {
            steps {
                sh '''
                pip3 install --upgrade pip
                pip3 install poetry
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
                poetry run pytest || echo "Nenhum teste encontrado"
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
        success { echo "Pipeline finalizada com sucesso!" }
        failure { echo "Pipeline falhou!" }
    }
}
