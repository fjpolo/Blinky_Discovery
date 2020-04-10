pipeline {
    agent { dockerfile false }
     stages {
          stage('Unit Test') {
            steps {
                sh 'ceedling test:all'
            }
     }
}