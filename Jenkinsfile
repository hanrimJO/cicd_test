pipeline {
    agent any
    stages {
        stage('test echo'){
            steps{
                sh 'echo test 3'
            }
        }
        stage('build docker image'){
            steps{
                sh 'docker build -t my_django:latest .'
            }
        }
        stage('docker push acr'){
            steps{
                sh 'docker login hrjotest.azurecr.io'
                sh 'docker push hrjotest.azurecr.io/test/my_django:latest'
            }
        }
    }
}