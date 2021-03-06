pipeline {
    environment{
        LOCALIMAGE = 'riverforest02/my_django:latest'
        AZUREIMAGE = 'hrjotest.azurecr.io/my_django:latest'
        AZURECR = 'hrjotest.azurecr.io'
    }
    agent any
    stages {
        stage('build docker image'){
            steps {
                sh 'docker build -t $LOCALIMAGE .'
            }
        }
        // stage('docker push to dockerhub'){
        //     steps{
        //         script{
        //             withCredentials([usernamePassword( credentialsId: 'dockerhub_id', usernameVariable: 'USER', passwordVariable: 'PASSWORD')]) {
        //                 def registry_url = "https://registry.hub.docker.com"
                        
        //                 sh "docker login -u $USER -p $PASSWORD ${registry_url}"
                        
        //                 docker.withRegistry("${registry_url}") {
        //                     sh "docker push riverforest02/my_django:latest"
        //                 }
        //             }
        //         }
        //     }
        // }
        stage('docker push to azurecr'){
            steps {
                script{
                    withCredentials([usernamePassword( credentialsId: 'azurecr_id', usernameVariable: 'USER', passwordVariable: 'PASSWORD')]) {
                        sh "docker login -u $USER -p $PASSWORD $AZURECR"
                        sh "docker tag $LOCALIMAGE $AZUREIMAGE"
                        sh "docker push $AZUREIMAGE"
                    }
                }
            }
        }
        stage('delete docker image'){
            steps {
                sh "docker rmi $LOCALIMAGE"
                sh "docker rmi $AZUREIMAGE"
            }
        }
        stage('ssh deploy') {
            steps{
                sshagent (credentials: ['deploy_id']) {
                    sh 'ssh -o StrictHostKeyChecking=no -l azureuser 20.194.25.143 uname -a'
                    script{
                        withCredentials([usernamePassword( credentialsId: 'azurecr_id', usernameVariable: 'USER', passwordVariable: 'PASSWORD')]) {
                            sh 'ssh azureuser@20.194.25.143 "sudo docker login -u $USER -p $PASSWORD $AZURECR"'
                        }
                    }
                    sh 'ssh azureuser@20.194.25.143 "cd cicd_test && git pull"'
                    sh 'ssh azureuser@20.194.25.143 "sudo docker pull hrjotest.azurecr.io/my_django:latest"'
                    sh 'ssh azureuser@20.194.25.143 "cd cicd_test && sudo docker-compose up --build -d"'
                }
            }
        }
    }
}