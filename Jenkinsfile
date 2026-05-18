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

        stage('Pylint') {
            steps {
                sh '''
                    . ./activeaza_venv
                    pylint --exit-zero app/lib/*.py
                    pylint --exit-zero app/test/*.py
                    pylint --exit-zero sporturi.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Unit testing...'
                sh '''
                    . ./activeaza_venv
                    PYTHONPATH=. pytest app/test/test_biblioteca_sporturi.py -v
                '''
            }
        }

        stage('Deploy Docker') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                sh '''
                    docker build -t sporturi-golf:v${BUILD_NUMBER} .
                    docker create --name sporturi-golf${BUILD_NUMBER} -p 8021:5011 sporturi-golf:v${BUILD_NUMBER}
                '''
            }
        }
    }
}

