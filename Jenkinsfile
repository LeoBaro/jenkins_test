pipeline {
    agent any

    stages {
        stage('Dependencies') {
            steps {
                sh "python --version"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Store artifacts') {
            steps {
                echo 'Storing artifacts....'
            }
        }
    }
}