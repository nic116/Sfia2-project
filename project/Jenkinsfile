pipeline {
    // agent none
    agent any

    stages{

            stage('Dependencies'){
                // agent {label 'master'}
                steps{
                    sh 'chmod +x ./script/*'
                    sh './script/before_installation.sh'
                    sh './script/ansible.sh'
                }
            }

            stage('Deploying Docker Stack'){
                // agent {label 'manager_node'}
                steps{
                    sh 'chmod +x ./script/*'
                    sh './script/docker.sh'
                }
            }

    }
}