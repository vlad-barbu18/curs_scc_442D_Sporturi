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
                    . ./activeaza_venv_jenkins
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                sh '''
                    . ./activeaza_venv;
                    pylint --exit-zero app/lib/*.py;
                    pylint --exit-zero app/tests/*.py;
                    pylint --exit-zero <tema>.py;
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
                    docker build -t <tema>:v${BUILD_NUMBER} .
                    docker create --name <tema>${BUILD_NUMBER} -p 8021:5012 <tema>:v${BUILD_NUMBER}
                '''
            }
        }
    }
}
