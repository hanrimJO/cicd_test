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
                sh 'docker build -t riverforest02/my_django:latest .'
            }
        }
        // stage('docker push to dockerhub'){
        //     steps{
        //         script{
        //             docker.withRegistry("https://registry.hub.docker.com", 'dockerhub_id'){
        //                 sh 'docker push riverforest02/my_django:latest'
        //             }
        //         }
        //     }
        // }
        stage('docker push to dockerhub'){
            steps{
                script{
                    withCredentials([usernamePassword( credentialsId: 'dockerhub_id', usernameVariable: 'USER', passwordVariable: 'PASSWORD')]) {
                        def registry_url = "https://registry.hub.docker.com"
                        
                        sh "docker login -u $USER -p $PASSWORD ${registry_url}"
                        
                        docker.withRegistry("${registry_url}") {
                            sh "docker push riverforest02/my_django:latest"
                        }
                    }
                }
            }
        }
        stage('docker push to azurecr'){
            steps{
                script{
                    withCredentials([usernamePassword( credentialsId: 'azurecr_id', usernameVariable: 'USER', passwordVariable: 'PASSWORD')]) {
                        def registry_url = "hrjotest.azurecr.io"
                        sh "docker login -u $USER -p $PASSWORD ${registry_url}"
                        
                        docker.withRegistry("${registry_url}") {
                            sh "docker push ${registry_url}/riverforest02/my_django:latest"
                        }
                    }
                }
            }
        }
    }
}
