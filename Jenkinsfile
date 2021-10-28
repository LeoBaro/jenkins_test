pipeline {
    agent any

    stages {
        stage('Dependencies') {
            steps {
                echo "Current workspace is ${env.WORKSPACE}"
                sh "python3 --version"
                //sh "python3 -m venv /path/to/new/virtual/environment"

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