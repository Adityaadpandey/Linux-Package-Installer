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

def br():
    print('\n1. brave  \n2. chrome \n3. firefox')
    choice = int(input('\nEnter your choice: '))
    if choice == 1:
        Browser.brave()
    elif choice == 2:
        Browser.chrome()
    elif choice == 3:
        Browser.firefox()

def pr():
    print('\n1. python \n2. java \n3. node \n4. c \n5. c++ \n6. c# \n7. go \n8. ruby \n9. php \n10. java script \n11. kotlin \n12. rust \n13. go lang')
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

def pg():
    print('\n1. vs_code \n2. atom \n3. postman \n4. vim \n5. sublime text \n6. git \n7. github cli')
    choice = int(input('\nEnter your choice: '))
    if choice == 1:
        Program.vs_code()
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


while True:
    print('\n1. Browser \n2. Programming Language \n3. Programming Tools \n4. Exit')
    choice = int(input('\nEnter your choice: '))
    if choice == 1:
            br()
    elif choice == 2:
            pr()
    elif choice == 3:
            pg()
    elif choice == 4:
            exit()