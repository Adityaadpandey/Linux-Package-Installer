import distro
from Apt.run import main as apt_main

name = distro.linux_distribution()


if name[0] == "Linux Mint":
    print("Linux Mint")
    apt_main()
if name[0] == "Ubuntu":
    print("Ubuntu")
    apt_main()

if name[0] == "Debian":
    print("Debian")
    apt_main()
if name[0] == "Lubuntu":
    print("Lubuntu")
    apt_main()
if name[0] == "Xubuntu":
    print("Xubuntu")
    apt_main()
if name[0] == "Kubuntu":
    print("Kubuntu")
    apt_main()
if name[0] == "peppermint":
    print("peppermint")
    apt_main()
if name[0] == "Knoppix":
    print("Knoppix")
    apt_main()
if name[0] == "bodhi linux":
    print("bodhi linux")
    apt_main()
if name[0] == "Deepin":
    print("Deepin")
    apt_main()