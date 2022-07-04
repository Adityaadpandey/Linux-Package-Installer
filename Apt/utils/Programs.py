import os


class Program():
    def vs_code():
        os.system("sudo apt install software-properties-common apt-transport-https wget")
        os.system("wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -")
        os.system('sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"')
        os.system("sudo apt install code")
        os.system("echo VS-code is installed")

    def atom():
        os.system('wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -')
        os.system('sudo sh -c "echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list"')
        os.system('sudo apt-get update')
        os.system('sudo apt-get install atom')
        os.system('echo Atom is installed')
    
    def postman():
        os.system('sudo apt install snapd')
        os.system('sudo snap install postman')
        os.system('echo Postman is installed')

    def vim():
        os.system('sudo apt install vim')
        os.system('echo Vim is installed')
    
    def sublime_text():
        os.system('sudo apt install sublime-text')
        os.system('echo Sublime-text is installed')
    
    def vscode():
        os.system('sudo apt install software-properties-common apt-transport-https wget')
        os.system('wget -qO - https://packages.microsoft.com/keys/microsoft.asc - | sudo apt-key add -')
        os.system('sudo sh -c "echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list"')
        os.system('sudo apt-get update')
        os.system('sudo apt-get install code')
        os.system('echo VS-code is installed')
        
    def git():
        os.system('sudo apt install git')
        os.system('echo Git is installed')

    def github_cli():
        os.system('curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg')
        os.system('sudo apt-key add /usr/share/keyrings/githubcli-archive-keyring.gpg')
        os.system('echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null')
        os.system('sudo apt update')
        os.system('sudo apt install gh')
        os.system('echo Github-cli is installed')