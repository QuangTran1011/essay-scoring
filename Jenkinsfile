pipeline {
    agent any

    environment{
        registry = 'quangtran1011/essay_scoring'
        registryCredential = 'dockerhub'
    }

    stages {
        stage('Deploy') {
            agent {
                kubernetes {
                    containerTemplate {
                        name 'helm' // Name of the container to be used for helm upgrade
                        image 'quangtran1011/jenkins:lts' // The image containing helm
                        alwaysPullImage true // Always pull image in case of using the same tag
                    }
                }
            }
            steps {
                script {
                    container('helm') {
                        // Deploy model-serving
                        sh("helm upgrade --install ess ./deployments/ess --namespace model-serving")


                        // Deploy nginx-ingress
                        sh("helm upgrade --install nginx-ingress ./deployments/nginx-ingress --namespace nginx-system")
                    }
                }
            }
        }
    }
}
