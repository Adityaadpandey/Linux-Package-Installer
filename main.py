import distro
from Apt.run import main as apt_main

name = distro.linux_distribution()

apt = ["Linux Mint", "Ubuntu", "Debian","Lubuntu","Xubuntu","Kubuntu","peppermint","Knoppix","bodhi linux", "Deepin"]

if name[0] in apt:
    print(name[0])
    apt_main()
else:
    print("Not Available for your OS")
