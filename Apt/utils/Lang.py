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
            "sudo apt install python3 -y",
            "sudo apt install python3-pip -y",
            "python3 --version"
        ]
        Programs.install_program(commands, "Python and pip are installed")

    @staticmethod
    def java():
        commands = [
            "sudo apt install openjdk-8-jdk -y",
            "java -version"
        ]
        Programs.install_program(commands, "Java is installed")

    @staticmethod
    def node():
        commands = [
            "curl -sL https://deb.nodesource.com/setup_16.x | sudo bash -",
            "sudo apt -y install nodejs",
            "node -v"
        ]
        Programs.install_program(commands, "Node.js is installed")

    @staticmethod
    def c():
        commands = [
            "sudo apt install gcc -y",
            "gcc --version"
        ]
        Programs.install_program(commands, "GCC (C) is installed")

    @staticmethod
    def c_plus():
        commands = [
            "sudo apt install g++ -y",  # Using g++ for C++
            "g++ --version"
        ]
        Programs.install_program(commands, "G++ (C++) is installed")

    @staticmethod
    def c_sharp():
        commands = [
            "sudo apt install mono-complete -y",
            "mono --version"
        ]
        Programs.install_program(commands, "Mono (C#) is installed")

    @staticmethod
    def go():
        commands = [
            "sudo apt install golang-go -y",
            "go version"
        ]
        Programs.install_program(commands, "Go is installed")

    @staticmethod
    def ruby():
        commands = [
            "sudo apt install ruby -y",
            "ruby --version"
        ]
        Programs.install_program(commands, "Ruby is installed")

    @staticmethod
    def php():
        commands = [
            "sudo apt install php -y",
            "php --version"
        ]
        Programs.install_program(commands, "PHP is installed")

    @staticmethod
    def java_script():
        # JavaScript is usually Node.js in this case
        commands = [
            "sudo apt install nodejs -y",
            "node --version"
        ]
        Programs.install_program(commands, "Node.js (JavaScript) is installed")

    @staticmethod
    def kotlin():
        commands = [
            "sudo apt install default-jdk -y",
            "curl -s https://get.sdkman.io | bash",
            "source ~/.sdkman/bin/sdkman-init.sh",
            "sdk install kotlin",
            "kotlin --version"
        ]
        Programs.install_program(commands, "Kotlin is installed")

    @staticmethod
    def rust():
        commands = [
            "sudo apt install rustc -y",
            "rustc --version"
        ]
        Programs.install_program(commands, "Rust is installed")

    @staticmethod
    def yarn():
        commands = [
            "sudo apt install nodejs -y",
            "sudo apt install yarn -g",
            "node --version",
            "yarn --version"
        ]
        Programs.install_program(commands, "Yarn is installed")

    @staticmethod
    def perl():
        commands = [
            "sudo apt install perl -y",
            "perl --version"
        ]
        Programs.install_program(commands, "Perl is installed")

    @staticmethod
    def flutter():
        # Download and install Flutter
        commands = [
            "wget https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.0.4-stable.tar.xz",
            "tar xf flutter_linux_3.0.4-stable.tar.xz -C ~/",
            "export PATH=\"$PATH:~/flutter/bin\"",
            "flutter precache",
            "flutter doctor"
        ]
        Programs.install_program(commands, "Flutter is installed")
