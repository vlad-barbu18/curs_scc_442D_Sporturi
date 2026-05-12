/* Jenkins */
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pwd
                    ls -l
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    PYTHONPATH=. python3 -m pytest app/test
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
