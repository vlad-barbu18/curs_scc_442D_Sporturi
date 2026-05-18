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
                echo "Aplicatia Sporturi - Rugby a trecut de build, pylint si pytest."
                echo "Containerizarea Docker se verifica local folosind Dockerfile si dockerstart.sh."
                echo "Comenzi Docker locale:"
                echo "docker build -t sporturi:v01 ."
                echo "docker run --name sporturi1 -p 8021:5011 sporturi:v01"
                echo "docker ps"
            }
        }
    }
}
