from .utils.Brow import Browser
from .utils.Lang import Progams
from .utils.Programs import Program
import os

def br():
    print('\n1. brave  \n2. chrome \n3. firefox \n4. opera \n5. chromium \n6. exit')
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
        Browser.chromium()
    elif choice == 6:
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
        Program.docker_machine()
    elif choice == 12:
        Program.snap()
    elif choice == 13:
        Program.pycahrm()
    elif choice == 14:
        exit()

    
def main():
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