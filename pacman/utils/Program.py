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
            "sudo pacman -Sy --noconfirm",  # Update package database
            "sudo pacman -S --noconfirm code"
        ]
        Program.install_program(commands, "VS Code is installed")

    @staticmethod
    def atom():
        commands = [
            "yay -S --noconfirm atom"
        ]
        Program.install_program(commands, "Atom is installed")

    @staticmethod
    def postman():
        commands = [
            "sudo pacman -S --noconfirm snapd",
            "sudo systemctl enable --now snapd.socket",
            "sudo ln -s /var/lib/snapd/snap /snap",
            "sudo snap install postman"
        ]
        Program.install_program(commands, "Postman is installed")

    @staticmethod
    def vim():
        commands = [
            "sudo pacman -S --noconfirm vim"
        ]
        Program.install_program(commands, "Vim is installed")

    @staticmethod
    def sublime_text():
        commands = [
            "yay -S --noconfirm sublime-text"
        ]
        Program.install_program(commands, "Sublime Text is installed")

    @staticmethod
    def git():
        commands = [
            "sudo pacman -S --noconfirm git"
        ]
        Program.install_program(commands, "Git is installed")

    @staticmethod
    def github_cli():
        commands = [
            "sudo pacman -S --noconfirm github-cli"
        ]
        Program.install_program(commands, "GitHub CLI is installed")

    @staticmethod
    def docker():
        commands = [
            "sudo pacman -S --noconfirm docker",
            "sudo systemctl start docker",
            "sudo systemctl enable docker",
            "docker --version"
        ]
        Program.install_program(commands, "Docker is installed")

    @staticmethod
    def docker_compose():
        commands = [
            "sudo pacman -S --noconfirm docker-compose",
            "docker-compose --version"
        ]
        Program.install_program(commands, "Docker Compose is installed")

    @staticmethod
    def docker_machine():
        commands = [
            "yay -S --noconfirm docker-machine",
            "docker-machine --version"
        ]
        Program.install_program(commands, "Docker Machine is installed")

    @staticmethod
    def intelli_j():
        commands = [
            "yay -S --noconfirm intellij-idea-community-edition"
        ]
        Program.install_program(commands, "IntelliJ IDEA Community is installed")

    @staticmethod
    def snap():
        commands = [
            "sudo pacman -S --noconfirm snapd",
            "sudo systemctl enable --now snapd.socket",
            "sudo ln -s /var/lib/snapd/snap /snap"
        ]
        Program.install_program(commands, "Snapd is installed")

    @staticmethod
    def pycharm():
        commands = [
            "sudo pacman -S --noconfirm snapd",
            "sudo systemctl enable --now snapd.socket",
            "sudo ln -s /var/lib/snapd/snap /snap",
            "sudo snap install pycharm-community --classic"
        ]
        Program.install_program(commands, "PyCharm Community is installed")
