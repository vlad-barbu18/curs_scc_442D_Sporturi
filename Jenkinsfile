pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pwd
                    ls -l
                    . ./activeaza_venv_jenkins
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                sh '''
                    . ./activeaza_venv

                    echo "Verificare app/lib/*.py"
                    pylint --exit-zero app/lib/*.py

                    echo "Verificare app/tests/*.py"
                    pylint --exit-zero app/tests/*.py

                    echo "Verificare sporturi.py"
                    pylint --exit-zero sporturi.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Unit testing...'
                sh '''
                    . ./activeaza_venv
                    PYTHONPATH=. pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                sh '''
                    docker build -t sporturi:v${BUILD_NUMBER} .
                    docker rm -f sporturi${BUILD_NUMBER} || true
                    docker create --name sporturi${BUILD_NUMBER} -p 8021:5011 sporturi:v${BUILD_NUMBER}
                    docker ps -a | grep sporturi || true
                '''
            }
        }
    }
}
