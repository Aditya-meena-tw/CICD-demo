pipeline {
agent any

    
    stage('build') {
  steps {
    sh 'pip install -r requirements.txt'
  }
}
    stage ('Test'){
        steps {
            sh 'python unit_test.py'
        }
    }
}
}
