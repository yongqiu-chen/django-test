pipeline {
    agent any
    stages {
        stage('git') {
            steps {
                git credentialsId: 'b41b9f60-aae2-4dea-8ffb-46e07a6a5523', url: 'http://10.66.245.5/cyq/django-test.git'
            }
        }
    }
}