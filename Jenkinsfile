pipeline {
  agent any
  stages {
    stage('git pull') {
      parallel {
        stage('git pull') {
          steps {
            sh 'git pull'
          }
        }

        stage('test') {
          steps {
            sh 'python manage.py test'
          }
        }

      }
    }

  }
}