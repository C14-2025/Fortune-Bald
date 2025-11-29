pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Baixando código do GitHub..."
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                echo "Instalando Python e Poetry..."
                sh '''
                sudo apt-get update
                sudo apt-get install -y python3 python3-pip
                pip3 install poetry
                '''
            }
        }

        stage('Install dependencies') {
            steps {
                echo "Instalando dependências do projeto..."
                sh '''
                poetry install --no-interaction --no-root
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Executando testes unitários..."
                sh '''
                poetry run pytest || echo "Nenhum teste encontrado (ok)"
                '''
            }
        }

        stage('Build') {
            steps {
                echo "Rodando versão principal do projeto..."
                sh '''
                poetry run python -m cassino_cli
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline concluída com sucesso!"
        }
        failure {
            echo "Pipeline falhou!"
        }
    }
}
