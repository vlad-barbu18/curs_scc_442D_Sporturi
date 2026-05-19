/* Jenkinsfile - pipeline declarativ pentru proiectul SCC Sporturi */
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building virtual environment...'
                sh '''
                    pwd
                    ls -l
                    . ./activeaza_venv_jenkins
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                echo 'Running pylint...'
                sh '''
                    . ./activeaza_venv
                    export PYLINTHOME=.pylint.d
                    pylint --exit-zero app/lib/*.py
                    pylint --exit-zero app/tests/*.py
                    pylint --exit-zero sporturi.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    . ./activeaza_venv
                    pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                sh '''
                    docker build -t sporturi:v${BUILD_NUMBER} .
                    docker rm -f sporturi${BUILD_NUMBER} || true
                    docker create --name sporturi${BUILD_NUMBER} -p 5000:5000 sporturi:v${BUILD_NUMBER}
                '''
            }
        }
    }
}
