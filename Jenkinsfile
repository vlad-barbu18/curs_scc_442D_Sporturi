pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Codul a fost deja clonat de Jenkins.'
                sh 'ls -la'
            }
        }

        stage('Setup mediu virtual') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install --upgrade pip'
                sh '. .venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Verificare statica (pylint)') {
            steps {
                sh '. .venv/bin/activate && PYTHONPATH=. pytest app/test/ -v'
            }
        }

        stage('Teste unitare (pytest)') {
            steps {
                sh '. .venv/bin/activate && PYTHONPATH=. pytest app/test/ -v'
            }
        }

        stage('Build imagine Docker') {
            steps {
                sh 'docker build -t inot:latest .'
                sh 'docker images | grep inot'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizat cu succes!'
        }
        failure {
            echo 'Pipeline-ul a esuat. Verifica log-urile.'
        }
    }
}
