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
                
             //   sh 'docker-compose down'
                sh 'docker-compose up 
                sh 'docker ps'
                
            }
        }
    }
}
