import os

class Program:
    @staticmethod
    def install_program(commands, success_message):
        """Helper method to install programs and verify installation."""
        for command in commands:
            result = os.system(command)
            if result != 0:
                print(f"Error executing: {command}")
                return
        print(success_message)

    @staticmethod
    def vs_code():
        commands = [
            "sudo apt install software-properties-common apt-transport-https wget -y",
            "wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -",
            'sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"',
            "sudo apt install code -y"
        ]
        Program.install_program(commands, "VS Code is installed")

    @staticmethod
    def atom():
        commands = [
            'wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -',
            'sudo sh -c "echo \"deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main\" > /etc/apt/sources.list.d/atom.list"',
            'sudo apt-get update',
            'sudo apt-get install atom -y'
        ]
        Program.install_program(commands, "Atom is installed")

    @staticmethod
    def postman():
        commands = [
            'sudo apt install snapd -y',
            'sudo snap install postman'
        ]
        Program.install_program(commands, "Postman is installed")

    @staticmethod
    def vim():
        commands = [
            'sudo apt install vim -y'
        ]
        Program.install_program(commands, "Vim is installed")

    @staticmethod
    def sublime_text():
        commands = [
            'sudo apt install sublime-text -y'
        ]
        Program.install_program(commands, "Sublime Text is installed")

    @staticmethod
    def git():
        commands = [
            'sudo apt install git -y'
        ]
        Program.install_program(commands, "Git is installed")

    @staticmethod
    def github_cli():
        commands = [
            'curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg',
            'sudo apt-key add /usr/share/keyrings/githubcli-archive-keyring.gpg',
            'echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null',
            'sudo apt update',
            'sudo apt install gh -y'
        ]
        Program.install_program(commands, "GitHub CLI is installed")

    @staticmethod
    def docker():
        commands = [
            'sudo apt install docker.io -y',
            'docker --version',
            'sudo systemctl start docker',
            'sudo systemctl enable docker',
            'sudo systemctl status docker'
        ]
        Program.install_program(commands, "Docker is installed")

    @staticmethod
    def docker_compose():
        commands = [
            'sudo apt install docker-compose -y',
            'docker-compose --version'
        ]
        Program.install_program(commands, "Docker Compose is installed")

    @staticmethod
    def docker_machine():
        commands = [
            'sudo apt install docker-machine -y',
            'docker-machine --version'
        ]
        Program.install_program(commands, "Docker Machine is installed")

    @staticmethod
    def intelli_j():
        commands = [
            'sudo add-apt-repository ppa:mmk2410/intellij-idea-community -y',
            'sudo apt update',
            'sudo apt install intellij-idea-community -y'
        ]
        Program.install_program(commands, "IntelliJ IDEA Community is installed")

    @staticmethod
    def snap():
        commands = [
            'sudo mv /etc/apt/preferences.d/nosnap.pref ~/Documents/nosnap.backup',
            'sudo apt update',
            'sudo apt install snapd -y'
        ]
        Program.install_program(commands, "Snapd is installed")

    @staticmethod
    def pycharm():
        commands = [
            'sudo mv /etc/apt/preferences.d/nosnap.pref ~/Documents/nosnap.backup',
            'sudo apt update',
            'sudo apt install snapd -y',
            'sudo snap install pycharm-community --classic'
        ]
        Program.install_program(commands, "PyCharm Community is installed")
