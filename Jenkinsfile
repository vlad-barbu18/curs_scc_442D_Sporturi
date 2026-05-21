/* Jenkinsfile - pipeline declarativ */
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pwd
                    ls -l
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r quickrequirements.txt
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pylint --exit-zero app/lib/*.py
                    pylint --exit-zero app/tests/*.py
                    pylint --exit-zero sporturi.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Unit testing...'
                sh '''
                    . .venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                sh '''
                    docker build -t sporturi:v${BUILD_NUMBER} .
                    docker create --name sporturi${BUILD_NUMBER} -p 8021:5012 sporturi:v${BUILD_NUMBER}
                '''
            }
        }
    }
}