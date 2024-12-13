import os

class Programs:
    @staticmethod
    def install_program(commands, success_message):
        """Helper method to install programs and check their versions."""
        for command in commands:
            result = os.system(command)
            if result != 0:
                print(f"Error executing: {command}")
                return
        print(success_message)

    @staticmethod
    def python():
        commands = [
            "sudo pacman -S python python-pip --noconfirm",
            "python --version"
        ]
        Programs.install_program(commands, "Python and pip are installed")

    @staticmethod
    def java():
        commands = [
            "sudo pacman -S jdk-openjdk --noconfirm",
            "java -version"
        ]
        Programs.install_program(commands, "Java is installed")

    @staticmethod
    def node():
        commands = [
            "sudo pacman -S nodejs npm --noconfirm",
            "node -v"
        ]
        Programs.install_program(commands, "Node.js is installed")

    @staticmethod
    def c():
        commands = [
            "sudo pacman -S gcc --noconfirm",
            "gcc --version"
        ]
        Programs.install_program(commands, "GCC (C) is installed")

    @staticmethod
    def c_plus():
        commands = [
            "sudo pacman -S gcc --noconfirm",  # G++ is included in GCC
            "g++ --version"
        ]
        Programs.install_program(commands, "G++ (C++) is installed")

    @staticmethod
    def c_sharp():
        commands = [
            "sudo pacman -S mono --noconfirm",
            "mono --version"
        ]
        Programs.install_program(commands, "Mono (C#) is installed")

    @staticmethod
    def go():
        commands = [
            "sudo pacman -S go --noconfirm",
            "go version"
        ]
        Programs.install_program(commands, "Go is installed")

    @staticmethod
    def ruby():
        commands = [
            "sudo pacman -S ruby --noconfirm",
            "ruby --version"
        ]
        Programs.install_program(commands, "Ruby is installed")

    @staticmethod
    def php():
        commands = [
            "sudo pacman -S php --noconfirm",
            "php --version"
        ]
        Programs.install_program(commands, "PHP is installed")

    @staticmethod
    def java_script():
        # JavaScript is usually Node.js in this case
        commands = [
            "sudo pacman -S nodejs npm --noconfirm",
            "node --version"
        ]
        Programs.install_program(commands, "Node.js (JavaScript) is installed")

    @staticmethod
    def kotlin():
        commands = [
            "sudo pacman -S jdk-openjdk --noconfirm",
            "curl -s https://get.sdkman.io | bash",
            "source ~/.sdkman/bin/sdkman-init.sh",
            "sdk install kotlin",
            "kotlin --version"
        ]
        Programs.install_program(commands, "Kotlin is installed")

    @staticmethod
    def rust():
        commands = [
            "sudo pacman -S rust --noconfirm",
            "rustc --version"
        ]
        Programs.install_program(commands, "Rust is installed")

    @staticmethod
    def yarn():
        commands = [
            "sudo pacman -S nodejs npm --noconfirm",
            "sudo npm install -g yarn",
            "node --version",
            "yarn --version"
        ]
        Programs.install_program(commands, "Yarn is installed")

    @staticmethod
    def perl():
        commands = [
            "sudo pacman -S perl --noconfirm",
            "perl --version"
        ]
        Programs.install_program(commands, "Perl is installed")

    @staticmethod
    def flutter():
        commands = [
            "sudo pacman -S wget --noconfirm",
            "wget https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.0.4-stable.tar.xz",
            "tar xf flutter_linux_3.0.4-stable.tar.xz -C ~",
            "export PATH=\"$PATH:~/flutter/bin\"",
            "flutter precache",
            "flutter doctor"
        ]
        Programs.install_program(commands, "Flutter is installed")
