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
                    echo "Verificare app/lib/*.py";
                    pylint --exit-zero app/lib/*.py;

                    echo "Verificare app/test/*.py";
                    pylint --exit-zero app/test/*.py;

                    echo "Verificare sporturi.py";
                    pylint --exit-zero sporturi.py;
                '''
            }
        }

        stage('testare cu pytest') {
            steps {
                echo 'testare'
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
                    docker create --name sporturi${BUILD_NUMBER} -p 8014:5014 sporturi:v${BUILD_NUMBER}
                '''
            }
        }
    }
}
