#!/usr/bin/python3

import os
import socket
import sys
import colorama
from colorama import Fore, Style, init

init(autoreset=True)

_target = ""
inp = True

def create_folder():
    folder_create = input("[?] Should I create a folder for you to save the outout? (y/n)")
    if folder_create == "y" or folder_create == "Y":
        folder_name = input("[!] Please enter the name of the folder and I will create it for you: ")
        os.system("mkdir " + folder_name)
        print(Fore.GREEN + "[+] Folder with the name " + folder_name + " created!")
        return str(folder_name)
    else:
        print(Fore.MAGENTA + "[-] No folder created")

def nmap(_target, folder_name):
    print(Fore.RED + "nmap -sC -sV " + _target)
    os.system("nmap -sC -sV -o " + folder_name + "/nmap_" + _target + " " + _target)


def dirb(_target, folder_name):
    file_location = dict_file()
    ssl = input(Fore.RED + "Run against SSL? (y/n): ")
    if ssl == "y" or ssl == "Y":
        print(Fore.GREEN + "Running dirb https://" + _target + " " + file_location)
        os.system("dirb https://" + _target + " " + file_location > dirb/ + folder_name)
    elif ssl == "n" or ssl == "N":
        print(Fore.GREEN + "Running dirb http://" + _target + " " + file_location)
        os.system("dirb http://" + _target + " " + file_location)

def dict_file():
    file_location = input(Fore.RED + "Please add path to dictionary file (Example: /usr/share/wordlists/dirb/common.txt " )
    return str(file_location)


def main():
    global inp
    while inp:
        print(Fore.BLUE + "______________________________________________________________________________________________")
        print(Fore.BLUE + ".___ _______    _____________________________     __________________     _____    _______ ")
        print(Fore.BLUE + "|   |\      \  /   _____/\_   _____/\_   ___ \   /   _____/\_   ___ \   /  _  \   \      \\")
        print(Fore.BLUE + "|   |/   |   \ \_____  \  |    __)_ /    \  \/   \_____  \ /    \  \/  /  /_\  \  /   |   \\")
        print(Fore.BLUE + "|   /    |    \/        \ |        \\\     \____  /        \\\     \____/    |    \/    |    \\")
        print(Fore.BLUE + "|___\____|__  /_______  //_______  / \______  / /_______  / \______  /\____|__  /\____|__  /")
        print(Fore.BLUE + "            \/        \/         \/         \/          \/         \/         \/         \/")
        print(Fore.BLUE + "*************************** CREATED BY https://invasive-security.de ***************************")
        print(Fore.BLUE + "_______________________________________________________________________________________________")

        # Define Target
        _target = input(Fore.GREEN + "[!] Enter Target IP: ")

        folder_name = create_folder()

        print(Fore.RED + "Choose your Weapon...")
        print(Fore.YELLOW + "=================================")
        print(Fore.YELLOW + "1. NMAP")
        print(Fore.YELLOW + "2. DIRB")
        print(Fore.YELLOW + "3. NIKTO")
        print(Fore.YELLOW + "4. Let´s run them ALL")
        print(Fore.YELLOW + "5. EXIT")
        print(Fore.YELLOW + "=================================")
        inp = input(Fore.GREEN + "[!] Enter the number of selection (1,2,3,4,5): ")

        if inp == "1":
            nmap(_target, folder_name)
            inp = False
        elif inp == "2":
            dirb(_target, folder_name)
            inp = False
        elif inp == "3":
            print("NIKTO")
            inp = False
        elif inp == "4":
            print("ALL")
            inp = False
        elif inp == "5":
            print("EXIT")
            exit()
        else:
            print("ERROR")
            inp = False


main()
