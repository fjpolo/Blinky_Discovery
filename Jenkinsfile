pipeline {
    agent any
     stages {
        stage('Unit Test') {
            steps {
                bat 'echo Testing...'
                bat 'cd D:/Dokumenten/STM32F4/Blinky_Discovery && ceedling test:all'

            }
        }
        stage('Simulator Test'){
            steps{
                bat 'echo Initializing Jumper...'
                bat 'cd D:/Dokumenten/STM32F4/Blinky_Discovery/jumper && (python init_jumper.py && echo \n) '
            }
        }
        stage('Build'){
            steps{
                bat 'echo Building...'
                bat 'D:/Programmen/Keil_v5/UV4/UV4.exe -b -j0 D:/Dokumenten/STM32F4/Blinky_Discovery/MDK-ARM/blinky.uvprojx -t"blinky" -o"D:/Dokumenten/STM32F4/Blinky_Discovery/MDK-ARM/BuildOutputfile.txt"'
            }
        }
    }
}