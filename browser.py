import os

class Browser():
    def brave():
        os.system("sudo apt install apt-transport-https curl")
        os.system("sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
        os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
        os.system("sudo apt update")
        os.system("sudo apt install brave-browser")
        os.system("echo brave-browser is installed")
        
    def chrome():
        os.system('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
        os.system('sudo dpkg -i google-chrome-stable_current_amd64.deb')
        os.system('echo chrome is installed')
    
    def firefox():
        os.system('sudo apt install firefox')
        os.system('echo firefox is installed')