import os

class Programs():
    def python():
        os.system("sudo pacman -S --noconfirm python")
        os.system("sudo pacman -S --noconfirm python-pip")
        os.system('echo pip is installed')
        os.system('python --version')

    def java():
        os.system('sudo pacman -S --noconfirm jdk8-openjdk')
        os.system('echo java is installed')
        os.system('java -version')

    def node():
        os.system("sudo pacman -S --noconfirm nodejs npm")
        os.system("echo nodejs is installed")
        os.system("node -v")

    def c():
        os.system("sudo pacman -S --noconfirm gcc")
        os.system("echo gcc is installed")
        os.system("gcc --version")

    def c_plus():
        os.system("sudo pacman -S --noconfirm gcc")
        os.system("echo gcc is installed")
        os.system("gcc --version")

    def c_sharp():
        os.system("sudo pacman -S --noconfirm mono")
        os.system("echo mono is installed")
        os.system("mono --version")

    def go():
        os.system("sudo pacman -S --noconfirm go")
        os.system("echo go is installed")
        os.system("go version")

    def ruby():
        os.system("sudo pacman -S --noconfirm ruby")
        os.system("echo ruby is installed")
        os.system("ruby --version")

    def php():
        os.system("sudo pacman -S --noconfirm php")
        os.system("echo php is installed")
        os.system("php --version")

    def java_script():
        os.system("sudo pacman -S --noconfirm nodejs npm")
        os.system("echo nodejs is installed")
        os.system("node --version")

    def kotlin():
        os.system("sudo pacman -S --noconfirm jdk-openjdk")
        os.system("yay -S --noconfirm kotlin")
        os.system("kotlin --version")

    def rust():
        os.system("sudo pacman -S --noconfirm rust")
        os.system("echo rust is installed")
        os.system("rustc --version")

    def perl():
        os.system("sudo pacman -S --noconfirm perl")
        os.system("echo perl is installed")
        os.system("perl --version")

    def flutter():
        os.system('yay -S --noconfirm flutter')
        os.system('flutter precache')
        os.system('flutter doctor')

class Browser():
    def brave():
        os.system("yay -S --noconfirm brave-bin")
        os.system("echo brave-browser is installed")

    def chrome():
        os.system("yay -S --noconfirm google-chrome")
        os.system("echo chrome is installed")

    def firefox():
        os.system("sudo pacman -S --noconfirm firefox")
        os.system("echo firefox is installed")

    def opera():
        os.system("sudo pacman -S --noconfirm opera")
        os.system("echo opera is installed")

class Program():
    def vs_code():
        os.system("sudo pacman -S --noconfirm code")
        os.system("echo VS-code is installed")

    def atom():
        os.system("yay -S --noconfirm atom")
        os.system("echo Atom is installed")

    def postman():
        os.system("yay -S --noconfirm postman-bin")
        os.system("echo Postman is installed")

    def vim():
        os.system("sudo pacman -S --noconfirm vim")
        os.system("echo Vim is installed")

    def sublime_text():
        os.system("yay -S --noconfirm sublime-text")
        os.system("echo Sublime-text is installed")

    def git():
        os.system("sudo pacman -S --noconfirm git")
        os.system("echo Git is installed")

    def github_cli():
        os.system("sudo pacman -S --noconfirm github-cli")
        os.system("echo Github-cli is installed")

    def docker():
        os.system("sudo pacman -S --noconfirm docker")
        os.system("docker --version")
        os.system("sudo systemctl start docker")
        os.system("sudo systemctl enable docker")
        os.system("sudo systemctl status docker")

    def docker_compose():
        os.system("sudo pacman -S --noconfirm docker-compose")
        os.system("docker-compose --version")
        os.system("echo Docker-compose is installed")

    def intelli_j():
        os.system("yay -S --noconfirm intellij-idea-community-edition")

    def snap():
        os.system("sudo pacman -S --noconfirm snapd")
        os.system("sudo systemctl enable --now snapd.socket")

    def pycharm():
        os.system("sudo pacman -S --noconfirm snapd")
        os.system("sudo systemctl enable --now snapd.socket")
        os.system("sudo snap install pycharm-community --classic")

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
    print('\n1. python \n2. java \n3. node \n4. c \n5. c++ \n6. c# \n7. go \n8. ruby \n9. php \n10. java script \n11. kotlin \n12. rust \n13. perl \n14. Exit')
    choice = int(input('\nEnter your choice: '))
    if choice == 1:
        Programs.python()
    elif choice == 2:
        Programs.java()
    elif choice == 3:
        Programs.node()
    elif choice == 4:
        Programs.c()
    elif choice == 5:
        Programs.c_plus()
    elif choice == 6:
        Programs.c_sharp()
    elif choice == 7:
        Programs.go()
    elif choice == 8:
        Programs.ruby()
    elif choice == 9:
        Programs.php()
    elif choice == 10:
        Programs.java_script()
    elif choice == 11:
        Programs.kotlin()
    elif choice == 12:
        Programs.rust()
    elif choice == 13:
        Programs.perl()
    elif choice == 14:
        exit()

def pg():
    print('\n1. vs_code \n2. atom \n3. postman \n4. vim \n5. sublime text \n6. git \n7. github cli \n8. IntelliJ IDEA \n9. docker \n10. docker_compose \n11. snap \n12. pycharm \n13. Exit')
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
    elif choice == 8:
        Program.intelli_j()
    elif choice == 9:
        Program.docker()
    elif choice == 10:
        Program.docker_compose()
    elif choice == 11:
        Program.snap()
    elif choice == 12:
        Program.pycharm()
    elif choice == 13:
        exit()

while True:
    print('\n1. Browser \n2. Programming Language \n3. Programming Tools \n4. Update the system \n5. Exit')
    choice = int(input('\nEnter your choice: '))
    if choice == 1:
        br()
    elif choice == 2:
        pr()
    elif choice == 3:
        pg()
    elif choice == 4:
        os.system('sudo pacman -Syu --noconfirm')
    elif choice == 5:
        exit()
