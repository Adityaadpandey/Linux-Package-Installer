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
    def perl():
        os.system("sudo apt install perl -y")
        os.system("echo perl is installed")
        os.system("perl --version")

    def flutter():
        os.system('https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.0.4-stable.tar.xz')
        os.system('tar xf ~/flutter_linux_3.0.4-stable.tar.xz')
        os.system('export PATH="$PATH:`pwd`/flutter/bin"')
        os.system('flutter precache')
        os.system('flutter doctor')

class Browser():
    def brave():
        os.system("sudo apt install apt-transport-https curl")
        os.system("sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
        os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
        os.system("sudo apt update")
        os.system("sudo apt install brave-browser")
        os.system("echo brave-browser is installed")
        
    def chrome():
        os.system('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
        os.system('sudo dpkg -i google-chrome-stable_current_amd64.deb')
        os.system('echo chrome is installed')
    
    def firefox():
        os.system('sudo apt install firefox')
        os.system('echo firefox is installed')

    def opera():
        os.system('wget -qO- https://deb.opera.com/archive.key | sudo apt-key add -')
        os.system('sudo add-apt-repository "deb [arch=i386,amd64] https://deb.opera.com/opera-stable/ stable non-free"')
        os.system('sudo apt install opera-stable')
        os.system('echo opera is installed')
import os


class Program():
    def vs_code():
        os.system("sudo apt install software-properties-common apt-transport-https wget")
        os.system("wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -")
        os.system('sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"')
        os.system("sudo apt install code")
        os.system("echo VS-code is installed")

    def atom():
        os.system('wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -')
        os.system('sudo sh -c "echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list"')
        os.system('sudo apt-get update')
        os.system('sudo apt-get install atom')
        os.system('echo Atom is installed')
    
    def postman():
        os.system('sudo apt install snapd')
        os.system('sudo snap install postman')
        os.system('echo Postman is installed')

    def vim():
        os.system('sudo apt install vim')
        os.system('echo Vim is installed')
    
    def sublime_text():
        os.system('sudo apt install sublime-text')
        os.system('echo Sublime-text is installed')
    
    def vscode():
        os.system('sudo apt install software-properties-common apt-transport-https wget')
        os.system('wget -qO - https://packages.microsoft.com/keys/microsoft.asc - | sudo apt-key add -')
        os.system('sudo sh -c "echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list"')
        os.system('sudo apt-get update')
        os.system('sudo apt-get install code')
        os.system('echo VS-code is installed')
        
    def git():
        os.system('sudo apt install git')
        os.system('echo Git is installed')

    def github_cli():
        os.system('curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg')
        os.system('sudo apt-key add /usr/share/keyrings/githubcli-archive-keyring.gpg')
        os.system('echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null')
        os.system('sudo apt update')
        os.system('sudo apt install gh')
        os.system('echo Github-cli is installed')

    def docker():
        os.system('sudo apt install docker.io')
        os.system('docker --version')
        os.system('sudo systemctl start docker')
        os.system('sudo systemctl enable docker')
        os.system('sudo systemctl status docker')
    
    def docker_compose():
        os.system('sudo apt install docker-compose')
        os.system('docker-compose --version')
        os.system('echo Docker-compose is installed')
    
    def docker_machine():
        os.system('sudo apt install docker-machine')
        os.system('docker-machine --version')
        os.system('echo Docker-machine is installed')
    
    def intelli_j():
        os.system('sudo add-apt-repository ppa:mmk2410/intellij-idea-community')
        os.system('sudo apt update')
        os.system('sudo apt install intellij-idea-community')

    def snap():
        os.system('sudo mv /etc/apt/preferences.d/nosnap.pref ~/Documents/nosnap.backup')
        os.system('sudo apt update')
        os.system('sudo apt install snapd')
    
    def pycahrm():
        os.system('sudo mv /etc/apt/preferences.d/nosnap.pref ~/Documents/nosnap.backup')
        os.system('sudo apt update')
        os.system('sudo apt install snapd')
        os.system('sudo snap install pycharm-community --classic')
def br():
    print('\n1. brave  \n2. chrome \n3. firefox \n4. opera \n5. exit')
    choice = int(input('\nEnter your choice: '))
    if choice == 1:
        Browser.brave()
    elif choice == 2:
        Browser.chrome()
    elif choice == 3:
        Browser.firefox()
    elif choice == 4:
        Browser.opera()
    elif choice == 5:
        exit()

def pr():
    print('\n1. python \n2. java \n3. node \n4. c \n5. c++ \n6. c# \n7. go \n8. ruby \n9. php \n10. java script \n11. kotlin \n12. rust \n13. go lang \n14. Perl \n15. Exit')
    choice = int(input('\nEnter your choice: '))
    if choice == 1:
        Progams.python()
    elif choice == 2:
        Progams.java()
    elif choice == 3:
        Progams.node()
    elif choice == 4:
        Progams.c()
    elif choice == 5:
        Progams.c_plus()
    elif choice == 6:
        Progams.c_sharp()
    elif choice == 7:
        Progams.go()
    elif choice == 8:
        Progams.ruby()
    elif choice == 9:
        Progams.php()
    elif choice == 10:
        Progams.java_script()
    elif choice == 11:
        Progams.kotlin()
    elif choice == 12:
        Progams.rust()
    elif choice == 13:
        Progams.go_lang()
    elif choice == 14:
        Progams.perl()
    elif choice == 15:
        exit()

def pg():
    print('\n1. vs_code \n2. atom \n3. postman \n4. vim \n5. sublime text \n6. git \n7. github cli \n8. IntelliJ IDEA \n9. docker \n10. docker_compose \n11. docker_machine \n12 snap \n13. Pycharm \n14. Exit')
    choice = int(input('\nEnter your choice: '))
    if choice == 1:
        print("You need to Install through .sh version on the terminal")
    elif choice == 2:
        Program.atom()
    elif choice == 3:
        Program.postman()
    elif choice == 4:
        Program.vim()
    elif choice == 5:
        Program.sublime_text()
    elif choice == 6:
        Program.git()
    elif choice == 7:
        Program.github_cli()
    elif choice == 8:
        Program.intelli_j()
    elif choice == 9:
        Program.docker()
    elif choice == 10:
        Program.docker_compose()
    elif choice == 11:
        Program.docker_machine()
    elif choice == 12:
        Program.snap()
    elif choice == 13:
        Program.pycahrm()
    elif choice == 14:
        exit()

    

while True:
    print('\n1. Browser \n2. Programming Language \n3. Programming Tools \n4. Update the sysytem \n5. Exit')
    choice = int(input('\nEnter your choice: '))
    if choice == 1:
        br()
    elif choice == 2:
        pr()
    elif choice == 3:
        pg()
    elif choice == 4:
        os.system('sudo apt update && sudo apt upgrade -y && sudo apt autoremove && sudo apt autoclean')
    elif choice == 5:
        exit()