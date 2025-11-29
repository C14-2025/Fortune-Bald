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

        stage('Build Artifact') {
            steps {
                sh '''
                . venv/bin/activate
                # Gera os arquivos na pasta dist/
                poetry build
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                # Roda testes e gera o XML. Falha a pipeline se tiver erro.
                poetry run pytest --junitxml=test-results.xml
                '''
            }
            // Este post é ESPECÍFICO do estágio de testes para ler o XML
            post {
                always {
                    junit 'test-results.xml'
                }
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

    // Este post roda no final de TUDO
    post {
        success {
            // Salva o artefato gerado no estágio 'Build Artifact'
            archiveArtifacts artifacts: 'dist/*', allowEmptyArchive: true
            echo "Pipeline finalizada com sucesso!"
        }
        failure {
            echo "Pipeline falhou!"
        }
    }
}