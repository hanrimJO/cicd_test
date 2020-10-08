pipeline {
    agent any
    stages {
        stage('test echo'){
            steps{
                sh 'echo test 3'
            }
        }
        stage('run docker-compose'){
            steps{
                sh 'docker-compose up --build'
            }
        }
    }
}