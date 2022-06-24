#!/bin/sh

sudo apt install git

git clone https://github.com/Adityaadpandey/Linux-Package-Installer.git
sudo apt install python3-pip
python3 Linux-Package-Installer/run.py