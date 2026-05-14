pipeline {
    agent any
    stages {
	# etapa 1: checkout
	stage ('Checkout') {
		steps {
			checkout scm
		}
	}

	#etapa 2: install
        stage('Install') {
            steps {
                sh '''
			python3 -m venv venv 
			./venv/bin/pip install -r requirements.txt		
		'''
		}	
	}
	
	#etapa 3: unit tests
	stage ('Test') {
		steps {
			sh '''
				export PYTHONPATH=$PYTHONPATH:.
				./venv/bin/python3 -m pytest test_f1.py
			'''
		}
	}

	#etapa 4: crearea imaginii docker
	stage('Docker Build') {
		steps {
			echo 'Se construieste imaginea Docker pentru formula 1'
			sh 'sudo docker build -t f1-app-stancu-andreea .'
		}
	}
    }
    post {
        always {
            echo 'Finalizare executie pipeline F1'
        }
	success {
		echo 'Proiect construit si testat cu succes'
	}
	failure {
		echo 'A aparut o eroare in piepline; check log-uri'
	}
    }
}
