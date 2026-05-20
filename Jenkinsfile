/* Jenkinsfile - pipeline declarativ pentru proiectul Sailing */
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building proiect Sailing...'
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
                    pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                sh '''
                    docker build -t sporturi-sailing:v${BUILD_NUMBER} .
                    docker create --name sporturi_sailing_${BUILD_NUMBER} -p 8021:5012 sporturi-sailing:v${BUILD_NUMBER}
                '''
            }
        }
    }
}
