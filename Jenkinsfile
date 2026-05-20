pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh '''
                    pwd
                    ls -R

                    . ./activeaza_venv_jenkins
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                sh '''
                    . ./activeaza_venv

                    export PYTHONPATH=$(pwd)

                    echo $PYTHONPATH

                    python -c "
import sys
print(sys.path)
import app
import app.lib
"

                    pylint --exit-zero app/lib/biblioteca_sporturi.py
                    pylint --exit-zero app/tests/test_biblioteca_sporturi.py
                    pylint --exit-zero sporturi.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                sh '''
                    . ./activeaza_venv

                    export PYTHONPATH=$(pwd)

                    python -m pytest app/tests
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker build -t sporturi:v${BUILD_NUMBER} .

                    docker create \
                      --name sporturi${BUILD_NUMBER} \
                      -p 8021:5012 \
                      sporturi:v${BUILD_NUMBER}
                '''
            }
        }

    }
}
