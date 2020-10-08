pipeline {
    environment {
        registryCredential = 'dockerhub_id'
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
                withDockerRegistry([credentialsId: registryCredential, url: ""]){
                    sh 'docker push riverforest02/my_django:latest'
                }
            }
        }
    }
}