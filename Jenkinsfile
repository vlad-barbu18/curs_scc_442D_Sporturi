pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Unit Tests') {
            steps {
                sh 'pytest test_f1.py'
            }
        }
    }
    post {
        always {
            echo 'Finalizare executie pipeline.'
        }
    }
}
