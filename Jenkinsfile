/* Jenkinsfile - pipeline declarativ adaptat pentru Minifotbal */
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
                    . ./activeaza_venv_jenkins
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                sh '''
                    . ./activeaza_venv;
                    export PYTHONPATH="${WORKSPACE}";
                    pylint --exit-zero app/lib/biblioteca_sporturi.py;
                    pylint --exit-zero app/tests/test_biblioteca_sporturi.py;
                    pylint --exit-zero sporturi.py;
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Unit testing...'
                sh '''
                    . ./activeaza_venv;
                    export PYTHONPATH="${WORKSPACE}";
                    pytest;
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
