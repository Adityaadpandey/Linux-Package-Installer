import distro
from Apt.run import main as apt_main
from pacman.run import main as pacman_main

name = distro.name()

apt = ["Linux Mint", "Ubuntu", "Debian", "Lubuntu", "Xubuntu", "Kubuntu", "peppermint", "Knoppix", "bodhi linux", "Deepin","Pop!_OS"]
arch = ["Arch Linux", "Manjaro", "EndeavourOS", "ArcoLinux", "Anarchy Linux"]

if name in apt:
    print(name)
    apt_main()
elif name in arch:
    print(name)
    pacman_main()
else:
    print(name)
    print("Not Available for your OS")
