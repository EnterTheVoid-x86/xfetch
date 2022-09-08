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
    print("Please now re-run xfetch.")
    exit

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

shell = os.popen('echo $SHELL').read()[:-1]

shell1 = os.popen('echo $SHELL | cut -b 6-').read()[:-1]

shell2 = os.popen('echo $SHELL | cut -b 10-').read()[:-1]

bashcheck = shell.startswith('/bin')

gpu = os.popen('lspci | grep " VGA " | cut -b 36-').read()[:-1]

ramamount = os.popen('free -h | grep Mem: | cut -b 16- | cut -b -5').read()[:-1]

ramused = os.popen('free -h | grep Mem: | cut -b 28- | cut -b -5').read()[:-1]

print(CBLUE + username + CGREEN + "@" + CYELLOW + hostname)

print(CBLUE + "OS: " + CRESET + distro)

print(CBLUE + "Kernel: " + CRESET + kernel)

print(CBLUE + "Uptime: " + CRESET + uptime)

if distro == "Fedora Linux" or "Red Hat Enterprise Linux" or "CentOS" or "openSUSE":
    print(CBLUE + "Packages: " + CRESET + packages + " (rpm)")
elif distro == "Arch Linux" or "EndeavourOS" or "Manjaro":
    print(CBLUE + "Packages: " + CRESET + packages + " (pacman)")

if bashcheck == True:
    print(CBLUE + "Shell: " + CRESET + shell1)
else:
    print(CBLUE + "Shell: " + CRESET + shell2)

if wmname != False:
    print(CBLUE + "Window Manager: " + CRESET + wmname)

print(CBLUE + "CPU: " + CRESET + cpu)

print(CBLUE + "GPU: " + CRESET + gpu)

print(CBLUE + "Memory Usage: " + CRESET + ramused + "/" + ramamount)
