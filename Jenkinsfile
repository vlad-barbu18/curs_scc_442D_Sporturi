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
                echo 'Verificare calitate cod cu pylint...'
                sh '''
                    . ./activeaza_venv

                    echo "Verificare app/lib/*.py cu pylint"
                    pylint --exit-zero app/lib/*.py

                    echo "Verificare app/tests/*.py cu pylint"
                    pylint --exit-zero app/tests/*.py

                    echo "Verificare sporturi.py cu pylint"
                    pylint --exit-zero sporturi.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . ./activeaza_venv

                    echo "Current path:"
                    pwd

                    echo "Project structure:"
                    find app -maxdepth 3 -type f -print

                    export PYTHONPATH=$WORKSPACE
                    pytest app/tests
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy in lucru...'
            }
        }
    }
}
