import distro
from Apt.run import main as apt_main

name = distro.name()

apt = ["Linux Mint", "Ubuntu", "Debian","Lubuntu","Xubuntu","Kubuntu","peppermint","Knoppix","bodhi linux", "Deepin"]

if name in apt:
    print(name)
    apt_main()
    

else:
    print(name)
    print("Not Available for your OS")
