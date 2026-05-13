pipeline {
    agent any
    stages {
        stage('Install & test') {
            steps {
                sh '''
			python3 -m venv venv 
			./venv/bin/pip install -r requirements.txt
			export PYTHONPATH=$PYTHONPATH:.			
			./venv/bin/pytest test_f1.py
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
