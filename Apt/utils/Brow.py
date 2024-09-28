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

    def opera():
        os.system('wget -qO- https://deb.opera.com/archive.key | sudo apt-key add -')
        os.system('sudo add-apt-repository "deb [arch=i386,amd64] https://deb.opera.com/opera-stable/ stable non-free"')
        os.system('sudo apt install opera-stable')
        os.system('echo opera is installed')
    
    def chromium():
        os.system('sudo apt install -y chromium-browser')
        os.system('echo chromium is installed')