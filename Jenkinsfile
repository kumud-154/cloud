pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    /
                    image 'python:2-alpine'
                }
            }
            steps {
                
                sh 'python -m py_compile  sources/calc.py'
                
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
        stage('Test') {
            agent {
                docker {
                    
                    image 'qnib/pytest'
                }
            }
            steps {
                
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }
            post {
                always {
                    
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') {
                    agent any
                    
                    environment {
                        VOLUME = '$(pwd)/sources:/src'
                        IMAGE = 'cdrx/pyinstaller-linux:python2'
                    }
                    steps {
                        
                        dir(path: env.BUILD_ID) {
                            unstash(name: 'compiled-results')

                            
                            sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F calc.py'"
                        }
                    }
                    post {
                        success {
                            
                            archiveArtifacts "${env.BUILD_ID}/sources/dist/calc"
                            sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                        }
                    }
        }
    }
}