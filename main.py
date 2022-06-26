import distro
from LinuxMint.main import main as lm
from Ubuntu.main import main as lm1


name = distro.linux_distribution()


if name[0] == "Linux Mint":
    # print("Linux Mint")
    lm()
if name[0] == "Ubuntu":
    # print("Linux Mint")
    lm1()