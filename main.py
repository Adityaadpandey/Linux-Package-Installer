import distro
from LinuxMint.main import main as lm


name = distro.linux_distribution()


if name[0] == "Linux Mint":
    # print("Linux Mint")
    lm()