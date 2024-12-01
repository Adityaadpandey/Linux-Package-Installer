import os

class Browser:
    @staticmethod
    def install_browser(command, success_message):
        # Execute the installation command
        result = os.system(command)
        if result == 0:
            print(success_message)
        else:
            print(f"Error installing {success_message}")

    @staticmethod
    def brave():
        commands = [
            "sudo apt install apt-transport-https curl -y",
            "sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg",
            'echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list',
            "sudo apt update",
            "sudo apt install brave-browser -y"
        ]
        for command in commands:
            Browser.install_browser(command, "Brave Browser")

    @staticmethod
    def chrome():
        commands = [
            "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb",
            "sudo dpkg -i google-chrome-stable_current_amd64.deb",
            "sudo apt --fix-broken install -y"  # This helps in case of dependency issues
        ]
        for command in commands:
            Browser.install_browser(command, "Chrome")

    @staticmethod
    def firefox():
        Browser.install_browser("sudo apt install firefox -y", "Firefox")

    @staticmethod
    def opera():
        commands = [
            'wget -qO- https://deb.opera.com/archive.key | sudo apt-key add -',
            'sudo add-apt-repository "deb [arch=i386,amd64] https://deb.opera.com/opera-stable/ stable non-free"',
            "sudo apt install opera-stable -y"
        ]
        for command in commands:
            Browser.install_browser(command, "Opera")

    @staticmethod
    def chromium():
        Browser.install_browser("sudo apt install chromium-browser -y", "Chromium")

