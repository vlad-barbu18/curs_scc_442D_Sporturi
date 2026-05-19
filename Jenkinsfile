/* Jenkinsfile - pipeline declarativ */
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
                    . ./activeaza_venv
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                sh '''
                    . ./activeaza_venv;
                    pylint --exit-zero app/lib/*.py;
                    pylint --exit-zero app/tests/*.py;
                    pylint --exit-zero sporturi.py;
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Unit testing...'
                sh '''
                    . ./activeaza_venv;
                    pytest;
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                sh '''
                    docker build -t sporturi:v${BUILD_NUMBER} .
                    docker create --name sporturi${BUILD_NUMBER} -p 8030:5030 sporturi:v${BUILD_NUMBER}
                '''
            }
        }
    }
}
