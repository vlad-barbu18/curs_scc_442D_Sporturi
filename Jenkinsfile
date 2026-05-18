pipeline {
    agent none

    stages {
        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                sh '''
                    pwd
                    ls -l

                    echo 'Activare/creare mediu virtual pentru Jenkins...'
                    . ./activeaza_venv_jenkins
                '''
            }
        }

        stage('pylint - calitate cod') {
            agent any
            steps {
                echo 'Verificare calitate cod cu pylint...'
                sh '''
                    . ./activeaza_venv

                    echo '\\n\\nVerificare app/lib/*.py cu pylint\\n'
                    pylint --exit-zero app/lib/*.py

                    echo '\\n\\nVerificare app/tests/*.py cu pylint\\n'
                    pylint --exit-zero app/tests/*.py

                    echo '\\n\\nVerificare sporturi.py cu pylint\\n'
                    pylint --exit-zero sporturi.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . ./activeaza_venv

                    echo '\\n\\nRulare teste unitare cu pytest\\n'
                    pytest -v
                '''
            }
        }

        stage('Docker build') {
            agent any
            steps {
                echo 'Construire imagine Docker...'
                sh '''
                    docker build -t sporturi-ciclism:latest .
                '''
            }
        }

        stage('Deploy') {
            agent any
            steps {
                echo 'Deploy - in lucru.'
                echo 'Aplicatia a fost verificata prin build, pylint, pytest si Docker build.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizat cu succes. Rezultat: PASS.'
        }

        failure {
            echo 'Pipeline esuat. Verifica erorile din consola Jenkins.'
        }

        always {
            echo 'Executie pipeline incheiata.'
        }
    }
}