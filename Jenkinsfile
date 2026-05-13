pipeline {
    agent any
    stages {
        stage('Install & test') {
            steps {
                sh '''
			python3 -m venv venv 
			. venv/bin/activate
			pip install -r requirements.txt
			pytest test_f1.py
		'''
		}	
	}
    }
    post {
        always {
            echo 'Finalizare executie pipeline.'
        }
    }
}
