pipeline {
    agent any

    stages {
        stage('Installing dependencies in a virtual environment') {
            steps {
                echo "Current workspace is ${env.WORKSPACE}"
                sh "python3 --version"
                sh "which python3"
                sh "python3 -m venv ${env.WORKSPACE}/build_venv"
                sh "source ${env.WORKSPACE}/build_venv/bin/activate"
                sh "python --version"
                sh "which ${env.WORKSPACE}/build_venv/bin/python"
                sh "pip install -r requirements.txt"
                sh "python setup.py develop"
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


    post {
        always {
            echo 'Removing virtual environment'
            sh "rm -r ${env.WORKSPACE}/build_venv"
        }
        success {
            echo 'I succeeded!'
        }
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            echo 'I failed :('
        }
        changed {
            echo 'Things were different before...'
        }
    }
}