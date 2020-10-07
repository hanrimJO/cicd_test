pipeline {
  agent any
  stages {
    stage('git pull') {
      parallel {
        stage('git pull') {
          steps {
            sh '''cd cicd_test
git pull'''
          }
        }

        stage('test') {
          steps {
            sh '''cd cicd_test
python manage.py test'''
          }
        }

      }
    }

  }
}