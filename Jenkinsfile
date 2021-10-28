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
                sh "${env.WORKSPACE}/build_venv/bin/pip install -r requirements.txt"
                sh "${env.WORKSPACE}/build_venv/bin/python setup.py develop"
                sh "${env.WORKSPACE}/build_venv/bin/pip list"
            }
        }

        stage('Test') {
            steps {
                echo 'Testing....'
                sh "source SampleProject/testing/start_test.sh ${env.WORKSPACE}/build_venv"
            }
        }
        
    
        stage('Store artifacts') { 
            steps {
                junit(testResults: "SampleProject/testing/junit_report.xml", allowEmptyResults: true)
                archiveArtifacts artifacts: "SampleProject/testing/coverage_report.xml"
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