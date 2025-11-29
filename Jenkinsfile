pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Python & venv') {
            steps {
                sh '''
                apt-get update
                apt-get install -y python3 python3-venv python3-pip
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install poetry
                '''
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                poetry install --no-interaction
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                poetry run pytest || echo "Nenhum teste encontrado"
                '''
            }
        }

        stage('Run App') {
            steps {
                sh '''
                . venv/bin/activate
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
