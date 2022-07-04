import os

class Progams():
    def python():
        os.system("sudo apt install python3 -y")
        os.system('sudo apt install python3-pip -y')
        os.system('echo pip is installed')
        os.system('python3 --version')
    
    def java(): 
        os.system('sudo apt install openjdk-8-jdk -y')
        os.system('echo java is installed')
        os.system('java -version')
    
    def node():
        os.system("curl -sL https://deb.nodesource.com/setup_16.x | sudo bash -")
        os.system("sudo apt -y install nodejs")
        os.system("echo nodejs is installed")
        os.system("node -v")

    def c():
        os.system("sudo apt install gcc -y")
        os.system("echo gcc is installed")
        os.system("gcc --version")
        
    def c_plus():
        os.system("sudo apt install gcc -y")
        os.system("echo gcc is installed")
        os.system("gcc --version")

    def c_sharp():
        os.system("sudo apt install mono-complete -y")
        os.system("echo mono-complete is installed")
        os.system("mono --version")
    def go():
        os.system("sudo apt install golang-go -y")
        os.system("echo golang-go is installed")
        os.system("go version")
    def ruby():
        os.system("sudo apt install ruby -y")
        os.system("echo ruby is installed")
        os.system("ruby --version")
    def php():
        os.system("sudo apt install php -y")
        os.system("echo php is installed")
        os.system("php --version")
    def java_script():
        os.system("sudo apt install nodejs -y")
        os.system("echo nodejs is installed")
        os.system("node --version")
    def kotlin():
        os.system("sudo apt install default-jdk")
        os.system("curl -s https://get.sdkman.io | bash ")
        os.system('sdk install kotlin')
        os.system("kotlin --version")
    def rust():
        os.system("sudo apt install rustc -y")
        os.system("echo rustc is installed")
        os.system("rustc --version")
    def go_lang():
        os.system("sudo apt install golang-go -y")
        os.system("echo golang-go is installed")
        os.system("go version")
    def yarn ():
        os.system("sudo apt install nodejs -y")
        os.system("echo nodejs is installed")
        os.system("node --version")
        os.system("sudo apt install yarn -g")
        os.system("echo yarn is installed")
        os.system("yarn --version")
