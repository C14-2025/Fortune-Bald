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
                poetry build
                '''
            }
        }
    }

    // Adicione isso para salvar o arquivo gerado no Jenkins
    post {
        success {
            archiveArtifacts artifacts: 'dist/*', allowEmptyArchive: true
            echo "Pipeline finalizada com sucesso!"
        }
        failure { echo "Pipeline falhou!" }
    }


        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                # --junitxml gera o relatório que o Jenkins entende
                # Removemos o "|| echo" para que a pipeline falhe se os testes falharem
                poetry run pytest --junitxml=test-results.xml
                '''
            }
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

    post {
        success { echo "Pipeline finalizada com sucesso!" }
        failure { echo "Pipeline falhou!" }
    }
}
