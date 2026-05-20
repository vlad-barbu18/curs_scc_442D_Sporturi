pipeline {
    agent none

    stages {
        stage('Build') {
            agent any
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
            agent any
            steps {
                echo 'Verificare calitate cod cu pylint...'
                sh '''
                    . ./activeaza_venv;

                    echo '\\n\\nVerificare app/lib/*.py cu pylint';
                    pylint --exit-zero app/lib/*.py;

                    echo '\\n\\nVerificare app/test/*.py cu pylint';
                    pylint --exit-zero app/test/*.py;

                    echo '\\n\\nVerificare sporturi.py cu pylint';
                    pylint --exit-zero sporturi.py;
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . ./activeaza_venv;
                    PYTHONPATH=. pytest app/tests;
                '''
            }
        }

        stage('Deploy') {
            agent any
            steps {
                echo 'Deploy in lucru...'
            }
        }
    }
}
