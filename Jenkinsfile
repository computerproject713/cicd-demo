pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/computerproject713/cicd-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest --junitxml=report.xml'
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'report.xml'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t cicd-demo .'
            }
        }

        stage('Run Container') {
            steps {
                bat '''
                docker stop cicd-demo || exit 0
                docker rm cicd-demo || exit 0
                docker run -d -p 5000:5000 --name cicd-demo cicd-demo
                '''            
            }
        }
    }
}