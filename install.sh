#!/bin/bash

filename=Linux-Package-Installer
if test -f "$filename";
then
    cd  Linux-Package-Installer/
    python3 main.py
    cd ..
    sudo rm -r Linux-Package-Installer

else
    sudo apt install git
    git clone https://github.com/Adityaadpandey/Linux-Package-Installer.git
    sudo apt install python3-pip
    cd  Linux-Package-Installer/
    python3 main.py
    cd ..
    sudo rm -r Linux-Package-Installer

fi