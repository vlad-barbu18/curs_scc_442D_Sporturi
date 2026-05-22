/* Jenkins */
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
                    PYTHONPATH=. pytest app/test;
                '''
            }
        }

        stage('Deploy') {
            agent any
            steps {
                echo 'Deploy in lucru...'
                sh '''
                    echo "Construire imagine Docker...";
                    docker build -t sporturi:v${BUILD_NUMBER} .;

                    echo "Stergere container vechi, daca exista...";
                    docker rm -f sporturi_container || true;

                    echo "Pornire container Docker...";
                    docker run -d --name sporturi_container -p 8021:5010 sporturi:v${BUILD_NUMBER};

                    echo "Astept sa porneasca aplicatia...";
                    sleep 5;

                    echo "Verific daca aplicatia raspunde...";
                    curl -f http://127.0.0.1:8021/sporturi;

                    echo "Containerul ruleaza corect.";
                '''
            }
        }
    }
}
