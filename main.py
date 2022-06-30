import distro
from LinuxMint.main import main as lm
from Debian.main import main as lm2
from Lubuntu.main import main as lm3
from Xubuntu.main import main as lm4
from Kubuntu.main import main as lm5
from Knoppix.main import main as lm6
from Deepin.main import main as lm7
from peppermint.main import main as lm8
from bodhi_linux.main import main as lm9
from Ubuntu.main import main as lm1


name = distro.linux_distribution()


if name[0] == "Linux Mint":
    print("Linux Mint")
    lm()
if name[0] == "Ubuntu":
    print("Ubuntu")
    lm1()

if name[0] == "Debian":
    print("Debian")
    lm2()
if name[0] == "Lubuntu":
    print("Lubuntu")
    lm3()
if name[0] == "Xubuntu":
    print("Xubuntu")
    lm4()
if name[0] == "Kubuntu":
    print("Kubuntu")
    lm5()
if name[0] == "peppermint":
    print("peppermint")
    lm8()
if name[0] == "Knoppix":
    print("Knoppix")
    lm6()
if name[0] == "bodhi linux":
    print("bodhi linux")
    lm9()
if name[0] == "Deepin":
    print("Deepin")
    lm7()