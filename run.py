from Test.browser import Browser
from Test.lang import Progams
from Test.prog import Programs



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
        Programs.vs_code()
    elif choice == 2:
        Programs.atom()
    elif choice == 3:
        Programs.postman()
    elif choice == 4:
        Programs.vim()
    elif choice == 5:
        Programs.sublime_text()
    elif choice == 6:
        Programs.git()
    elif choice == 7:
        Programs.github_cli()

    
if __name__ == '__main__':
    print('\n1. Browser \n2. Programming Language \n3. Programming Tools')
    choice = int(input('\nEnter your choice: '))
    if choice == 1:
        br()
    elif choice == 2:
        pr()
    elif choice == 3:
        pg()