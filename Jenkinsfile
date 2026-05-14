pipeline {
    agent any
    stages {
        stage('Install & test') {
            steps {
                sh '''
			python3 -m venv venv 
			./venv/bin/pip install -r requirements.txt		
			export PYTHONPATH=$PYTHONPATH:.
			./venv/bin/python3 -m pytest test_f1.py
		'''
		}	
	}
	stage('Docker Build') {
		steps {
			echo 'Se construieste imaginea Docker pentru formula 1'
			sh 'docker build -t f1-app-stancu-andreea .'
	}
    }
    post {
        always {
            echo 'Finalizare executie pipeline.'
        }
    }
}
