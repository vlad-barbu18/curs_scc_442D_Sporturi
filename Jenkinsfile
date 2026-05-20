/* Jenkinsfile - pipeline declarativ pentru proiectul Sporturi / MMA */
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building proiectul Sporturi - MMA...'
                sh '''
                    pwd
                    ls -l

                    chmod +x activeaza_venv activeaza_venv_jenkins ruleaza_aplicatia dockerstart.sh || true

                    . ./activeaza_venv_jenkins
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                echo 'Verificare calitate cod cu pylint...'
                sh '''
                    . ./activeaza_venv

                    pylint --exit-zero app/lib/*.py
                    pylint --exit-zero app/tests/*.py
                    pylint --exit-zero sporturi.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Rulare teste automate cu pytest...'
                sh '''
                    . ./activeaza_venv

                    pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo 'Build imagine Docker pentru proiectul sporturi...'

                sh '''
                    docker build -t sporturi:v${BUILD_NUMBER} .

                    docker rm -f sporturi${BUILD_NUMBER} || true

                    docker create --name sporturi${BUILD_NUMBER} -p 8021:5012 sporturi:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizat cu succes.'
        }

        failure {
            echo 'Pipeline esuat. Verifica logurile din Jenkins.'
        }
    }
}
