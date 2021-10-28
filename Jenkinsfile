pipeline {
    agent any

    stages {
        stage('Creating a virtual environment with anaconda') {
            steps {
                echo "Current workspace is ${env.WORKSPACE}"
                sh 
                sh "/data/miniconda/condabin/conda --version"
                sh "/data/miniconda/condabin/conda env create --name jenkins_test --file environment.yaml"

                //sh "source ${env.WORKSPACE}/build_venv/bin/activate"
                //sh "python --version" // python is not found
                //sh "which ${env.WORKSPACE}/build_venv/bin/python"
                //sh "pip install -r requirements.txt"
                //sh "python setup.py develop"
            }
        }

        stage('Test anaconda environment') {
            steps {
                sh "/data/miniconda/condabin/conda activate jenkins_test"
                sh "/data/miniconda/condabin/conda list"
                sh "python --version"
                sh "which python"
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