import os
from .utils.Brow import Browser
from .utils.Lang import Programs
from .utils.Programs import Program

# Function to handle browser installation
def br():
    browsers = {
        1: Browser.brave,
        2: Browser.chrome,
        3: Browser.firefox,
        4: Browser.opera,
        5: Browser.chromium,
        6: exit
    }

    print('\n1. Brave \n2. Chrome \n3. Firefox \n4. Opera \n5. Chromium \n6. Exit')
    choice = int(input('\nEnter your choice: '))

    # Call the appropriate function based on the user input
    action = browsers.get(choice)
    if action:
        action()
    else:
        print("Invalid choice. Please try again.")

# Function to handle programming language installation
def pr():
    languages = {
        1: Progams.python,
        2: Progams.java,
        3: Progams.node,
        4: Progams.c,
        5: Progams.c_plus,
        6: Progams.c_sharp,
        7: Progams.go,
        8: Progams.ruby,
        9: Progams.php,
        10: Progams.java_script,
        11: Progams.kotlin,
        12: Progams.rust,
        13: Progams.go_lang,
        14: Progams.perl,
        15: exit
    }

    print('\n1. Python \n2. Java \n3. Node \n4. C \n5. C++ \n6. C# \n7. Go \n8. Ruby \n9. PHP \n10. JavaScript \n11. Kotlin \n12. Rust \n13. Go Lang \n14. Perl \n15. Exit')
    choice = int(input('\nEnter your choice: '))

    # Call the appropriate function based on the user input
    action = languages.get(choice)
    if action:
        action()
    else:
        print("Invalid choice. Please try again.")

# Function to handle programming tools installation
def pg():
    tools = {
        1: Program.vs_code,
        2: Program.atom,
        3: Program.postman,
        4: Program.vim,
        5: Program.sublime_text,
        6: Program.git,
        7: Program.github_cli,
        8: Program.intelli_j,
        9: Program.docker,
        10: Program.docker_compose,
        11: Program.docker_machine,
        12: Program.snap,
        13: Program.pycharm,
        14: exit
    }

    print('\n1. VS Code \n2. Atom \n3. Postman \n4. Vim \n5. Sublime Text \n6. Git \n7. GitHub CLI \n8. IntelliJ IDEA \n9. Docker \n10. Docker Compose \n11. Docker Machine \n12. Snap \n13. PyCharm \n14. Exit')
    choice = int(input('\nEnter your choice: '))

    # Call the appropriate function based on the user input
    action = tools.get(choice)
    if action:
        action()
    else:
        print("Invalid choice. Please try again.")

# Main menu function
def main():
    while True:
        print('\n1. Browser \n2. Programming Language \n3. Programming Tools \n4. Update the System \n5. Exit')
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
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
