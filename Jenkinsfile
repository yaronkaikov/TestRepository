pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Testing (build) with flake8'
                sh "flake8 ${env.WORKSPACE}/app --max-line-length=80"
            }
        }
        stage("Deploy") {
          steps {
            script {
            echo 'Deploying to app server'
              try {
                  sh "scp ${env.WORKSPACE}/app/* ${env.APP_SERVER_USER}@${env.APP_SERVER_ADDRESS}:/app"
                  currentBuild.result = 'SUCCESS'
                } catch (Exception e) {
                    echo 'Exception occurred: ' + e.toString()
                }
                }
            }
        }
        stage('Test-Deploy') {
            steps {
                sh "ssh ${env.APP_SERVER_USER}@${env.APP_SERVER_ADDRESS} 'cd /app && python3 commitLogger.py'"
            }
        }
    }
    post {
        success {
            echo 'Deployment done successfully'
        }
        failure {
            echo 'Deployment failed'
        }
    }
}
