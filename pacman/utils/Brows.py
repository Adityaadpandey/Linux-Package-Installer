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
            "yay -S --noconfirm brave-bin"
        ]
        for command in commands:
            Browser.install_browser(command, "Brave Browser")

    @staticmethod
    def chrome():
        commands = [
            "yay -S --noconfirm google-chrome"
        ]
        for command in commands:
            Browser.install_browser(command, "Chrome")

    @staticmethod
    def firefox():
        Browser.install_browser("sudo pacman -S --noconfirm firefox", "Firefox")

    @staticmethod
    def opera():
        Browser.install_browser("sudo pacman -S --noconfirm opera", "Opera")

    @staticmethod
    def chromium():
        Browser.install_browser("sudo pacman -S --noconfirm chromium", "Chromium")
