#!/usr/bin/python3

import os
import socket
import sys
import colorama
from colorama import Fore, Style, init
init(autoreset=True)


_target = ""


inp = True
while inp:
    print(Fore.BLUE + "________________________________________________________________________________________________")
    print(Fore.BLUE + ".___ _______    _____________________________     __________________     _____    _______ ")
    print(Fore.BLUE + "|   |\      \  /   _____/\_   _____/\_   ___ \   /   _____/\_   ___ \   /  _  \   \      \\")
    print(Fore.BLUE + "|   |/   |   \ \_____  \  |    __)_ /    \  \/   \_____  \ /    \  \/  /  /_\  \  /   |   \\")
    print(Fore.BLUE + "|   /    |    \/        \ |        \\\     \____  /        \\\     \____/    |    \/    |    \\")
    print(Fore.BLUE + "|___\____|__  /_______  //_______  / \______  / /_______  / \______  /\____|__  /\____|__  /")
    print(Fore.BLUE + "            \/        \/         \/         \/          \/         \/         \/         \/")
    print(Fore.BLUE + "*************************** CREATED BY https://invasive-security.de ****************************")
    print(Fore.BLUE + "________________________________________________________________________________________________")

    # Define Target
    _target = input(Fore.GREEN + "[!] Enter Target IP: ")

    print(Fore.RED + "Choose your Weapon...")
    print(Fore.YELLOW + "=================================")
    print(Fore.YELLOW + "1. NMAP")
    print(Fore.YELLOW + "2. DIRBUSTER")
    print(Fore.YELLOW + "3. NIKTO")
    print(Fore.YELLOW + "4. Let´s run them ALL")
    print(Fore.YELLOW + "=================================")
    inp = input(Fore.GREEN + "[!] Enter the number of selection (1,2,3,4): ")

    if inp == "1":
        print(Fore.RED + "nmap -sC -sV " + _target)
        os.system("nmap -sC -sV " + _target)
        inp = False
    elif inp == "2":
        print("DIRBUSTER")
        inp = False
    elif inp == "3":
        print("NIKTO")
        inp = False
    elif inp == "4":
        print("ALL")
        inp = False
    else:
        print("ERROR")
        inp = False
