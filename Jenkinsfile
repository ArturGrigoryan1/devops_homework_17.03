pipeline {
    agent { label 'jenkins_agent' }
    triggers {
    GenericTrigger(
        genericVariables: [
            [defaultValue: '', key: 'base', regexpFilter: '', value: '$.ref']
            ],
     causeString: 'Triggered on $base',
     token: 'dev123',
     tokenCredentialId: '' )
    }

    stages {
        stage('docker compose') {
            steps {  
                sh 'ls -la'
                sh 'cat docker-compose.yml'
                sh 'docker compose version'
                sh 'docker images'
                sh 'docker run --rm hello-world'
            //    sh 'docker-compose up -d'
            //    sh 'docker-compose up -d'
            }
        }
    }
}
