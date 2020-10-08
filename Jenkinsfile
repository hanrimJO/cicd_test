pipeline {
    environment {
        dockeruser = 'riverforest02'
        dockerpw = 'k7654892!@'
    }
    agent any
    stages {
        stage('test echo'){
            steps{
                sh 'echo test 3'
            }
        }
        stage('build docker image'){
            steps{
                sh 'docker build -t riverforest02/my_django:latest .'
            }
        }
        stage('docker push acr'){
            steps{
                sh 'docker login -u $dockeruser -p $dockerpw'
                sh 'docker push riverforest02/my_django:latest'
            }
        }
    }
}