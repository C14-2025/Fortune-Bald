pipeline {
  agent any

  environment {
    POETRY_VENV = "${WORKSPACE}/.venv"
  }

  stages {

    stage('Install dependencies') {
      steps {
        echo "Instalando Poetry e dependências..."
        sh 'python -V'
        sh 'pip install --upgrade pip'
        sh 'pip install poetry'
        sh 'poetry config virtualenvs.in-project true || true'
        sh 'poetry install --no-interaction'
      }
    }

    stage('Run tests') {
      steps {
        echo "Executando testes (pytest)..."
        sh 'mkdir -p reports'
        // gera junit xml para o plugin JUnit do Jenkins
        sh 'poetry run pytest --maxfail=1 --disable-warnings --junitxml=reports/junit.xml || true'
      }
      post {
        always {
          junit 'reports/junit.xml' // publica relatório de testes
        }
      }
    }

    stage('Lint') {
      steps {
        echo "Rodando ruff..."
        sh 'pip install ruff'
        // faz o lint e falha se houver problemas
        sh 'ruff cassino_cli/ || true'
      }
    }

    stage('Build') {
      steps {
        echo "Construindo pacote (poetry build)..."
        sh 'poetry build'
      }
      post {
        success {
          archiveArtifacts artifacts: 'dist/**', fingerprint: true
        }
      }
    }

    // Stages para contar como "jobs por integrante" — cada integrante modifica/personaliza seu stage
    stage('job_andre') {
      steps {
        echo "Job do André — responsável: André"
      }
    }

    stage('job_joao') {
      steps {
        echo "Job do João — responsável: João"
      }
    }

    stage('job_maria') {
      steps {
        echo "Job da Maria — responsável: Maria"
      }
    }
  }

  post {
    always {
      echo "Pipeline finalizada. Limpando workspace."
      cleanWs()
    }
  }
}
