#!/bin/sh

# sudo apt install git

# git clone https://github.com/Adityaadpandey/Linux-Package-Installer.git

# sudo apt install python3-pip

sh -c "$(curl -fsSl https://raw.githubusercontent.com/Adityaadpandey/Linux-Package-Installer/master/main.py)"


python3 Linux-Package-Installer/main.py

rm -r Linux-Package-Installer