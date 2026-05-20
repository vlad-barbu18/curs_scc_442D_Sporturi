/* Jenkinsfile - pipeline declarativ pentru proiectul Sporturi / Balet */

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
                echo 'Verificare cod cu pylint...'
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
        echo 'Rulare teste pytest...'
        sh '''
            . ./activeaza_venv
            .venv/bin/python -m pytest
        '''
    }
}
        stage('Deploy') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                sh '''
                    docker build -t sporturi:v${BUILD_NUMBER} .
                    docker rm -f sporturi${BUILD_NUMBER} || true
                    docker create --name sporturi${BUILD_NUMBER} -p 8021:5012 sporturi:v${BUILD_NUMBER}
                '''
            }
        }
    }
}
