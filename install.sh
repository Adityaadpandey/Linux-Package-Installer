#!/bin/bash
filename=Linux-Package-Installer
if test -f "$filename";
then
    python3 Linux-Package-Installer/main.py
    sudo rm -r Linux-Package-Installer

else
    sudo apt install git
    git clone https://github.com/Adityaadpandey/Linux-Package-Installer.git
    sudo apt install python3-pip
    python3 Linux-Package-Installer/main.py
    sudo rm -r Linux-Package-Installer
fi
