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

fedora_ascii = r"""
      _____
     /   __)\
     |  /  \ \
  ___|  |__/ /
 / (_    _)_/
/ /  |  |
\ \__/  |
 \(_____/
"""

rhel_ascii = """
              _ _           _   
             | | |         | |  
 _ __ ___  __| | |__   __ _| |_ 
| '__/ _ \/ _` | '_ \ / _` | __|
| | |  __/ (_| | | | | (_| | |_ 
|_|  \___|\__,_|_| |_|\__,_|\__|
"""

centos_ascii = """
                 ..
               .PLTJ.
              <><><><>
     KKSSV' 4KKK LJ KKKL.'VSSKK
     KKV' 4KKKKK LJ KKKKAL 'VKK
     V' ' 'VKKKK LJ KKKKV' ' 'V
     .4MA.' 'VKK LJ KKV' '.4Mb.
   . KKKKKA.' 'V LJ V' '.4KKKKK .
 .4D KKKKKKKA.'' LJ ''.4KKKKKKK FA.
<QDD ++++++++++++  ++++++++++++ GFD>
 'VD KKKKKKKK'.. LJ ..'KKKKKKKK FV
   ' VKKKKK'. .4 LJ K. .'KKKKKV '
      'VK'. .4KK LJ KKA. .'KV'
     A. . .4KKKK LJ KKKKA. . .4
     KKA. 'KKKKK LJ KKKKK' .4KK
     KKSSA. VKKK LJ KKKV .4SSKK
              <><><><>
               'MKKM'
                 ''
"""

suse_ascii = r"""
  _______
__|   __ \
     / .\ \
     \__/ |
   _______|
   \_______
__________/
"""

arch_ascii = r"""
      /\
     /  \
    /\   \
   /      \
  /   ,,   \
 /   |  |  -\
/_-''    ''-_\
"""

manjaro_ascii = """
||||||||| ||||
||||||||| ||||
||||      ||||
|||| |||| ||||
|||| |||| ||||
|||| |||| ||||
|||| |||| ||||
"""

penguin_ascii = """
        #####
       #######
       ##O#O##
       #######
     ###########
    #############
   ###############
   ################
  #################
#####################
#####################
  #################
"""

username = os.getlogin()

hostname = socket.gethostname()

wm = subprocess.run(['wmctrl', '-m'], text=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
namestr = wm.stdout.split('\n')[0]
try:
    wmname = namestr.split(' ')[1]
except IndexError:
    wmname = False

distro = distro.name()

if distro == "Fedora Linux":
    ascii = fedora_ascii
    asciicolor = CBLUE
elif distro == "Red Hat Enterprise Linux":
    ascii = rhel_ascii
    asciicolor = CRED
elif distro == "CentOS":
    ascii = centos_ascii
    asciicolor = CVIOLET
elif distro == "openSUSE":
    ascii = suse_ascii
    asciicolor = CGREEN
elif distro == "Arch Linux":
    ascii = arch_ascii
    asciicolor = CBLUE
elif distro == "EndeavourOS":
    ascii = arch_ascii
    asciicolor = CVIOLET
elif distro == "Manjaro Linux":
    ascii = manjaro_ascii
    asciicolor = CGREEN
else:
    ascii = penguin_ascii
    asciicolor = CRESET

kernel = platform.release()

uptime = os.popen('uptime -p | cut -b 4-').read()[:-1]

cpu = cpuinfo.get_cpu_info()['brand_raw']

if distro == "Fedora Linux" or "Red Hat Enterprise Linux" or "CentOS" or "openSUSE":
    packages = os.popen('yum list installed | wc -l').read()[:-1]
elif distro == "Arch Linux" or "EndeavourOS" or "Manjaro Linux":
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

print(asciicolor + ascii + CRESET)

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
