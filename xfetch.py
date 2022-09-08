#!/usr/bin/env python
#
# This file is a part of xfetch; you can redistrubute, modify, or spread this work.# You may not sell this work under any given circumstances.

import platform
import sys
import distro
import subprocess
import time
import os
import socket

try:
    import cpuinfo
except ModuleNotFoundError:
    print("Installing the cpuinfo module...")
    print("CPUINFO: Provides the CPU Model Name.")
    os.system("pip install py-cpuinfo")
    import cpuinfo

CBLACK = '\33[30m'
CRED = '\33[31m'
CGREEN = '\33[32m'
CYELLOW = '\33[33m'
CBLUE = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE = '\33[36m'
CWHITE = '\33[37m'
CRESET = '\33[0m'

username = os.getlogin()

hostname = socket.gethostname()

wm = subprocess.run(['wmctrl', '-m'], text=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
namestr = wm.stdout.split('\n')[0]
try:
    wmname = namestr.split(' ')[1]
except IndexError:
    wmname = False

distro = distro.name()

kernel = platform.release()

uptime = os.popen('uptime -p | cut -b 4-').read()[:-1]

cpu = cpuinfo.get_cpu_info()['brand_raw']

if distro == "Fedora Linux" or "Red Hat Enterprise Linux" or "CentOS" or "openSUSE":
    packages = os.popen('yum list installed | wc -l').read()[:-1]
elif distro == "Arch Linux" or "EndeavourOS" or "Manjaro":
    packages = os.popen('pacman -Qq | wc -l').read()[:-1]
else:
    packages = False

shell = os.popen('echo $SHELL | cut -b 10-').read()[:-1]

print(CBLUE + username + CGREEN + "@" + CYELLOW + hostname)

print(CBLUE + "OS: " + CRESET + distro)

print(CBLUE + "Kernel: " + CRESET + kernel)

print(CBLUE + "Uptime: " + CRESET + uptime)

if distro == "Fedora Linux" or "Red Hat Enterprise Linux" or "CentOS" or "openSUSE":
    print(CBLUE + "Packages: " + CRESET + packages + " (rpm)")
elif distro == "Arch Linux" or "EndeavourOS" or "Manjaro":
    print(CBLUE + "Packages: " + CRESET + packages + " (pacman)")

print(CBLUE + "Shell: " + CRESET + shell)

if wmname != False:
    print(CBLUE + "Window Manager: " + CRESET + wmname)

print(CBLUE + "CPU: " + CRESET + cpu)
