pipeline {
    agent { label 'jenkins_agent' }

    stages {
        stage('docker compose') {
            steps {            
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }
    }
}
