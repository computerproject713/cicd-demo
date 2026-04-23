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
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest --junitxml=report.xml'
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'report.xml'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cicd-demo .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 cicd-demo'
            }
        }
    }
}