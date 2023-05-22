pipeline {
    agent any
    stages {
       stage('Installing packages') {
            steps {
                // Use the sh step to install packages
                sh 'pip install -r requirements.txt'
            }
        }
        stage ('Test'){
             steps {
                sh 'python3 unit_test.py'
        }
       
}
}

