#!/usr/bin/python3

import os
from colorama import Fore, init

init(autoreset=True)

# Globals
target = ""
inp = True


# Helper Functions

# Create a folder for the output if needed
def create_folder():
    folder_create = input(Fore.GREEN + "[?] Should I create a folder for you to save the outout? (y/n) ")
    if folder_create == "y" or folder_create == "Y":
        folder_name = input(Fore.GREEN + "[!] Please enter the name of the folder and I will create it for you: ")
        os.system("sudo mkdir " + folder_name)
        print(Fore.GREEN + "[+] Folder with the name " + folder_name + " created!\n")
        return str(folder_name)
    else:
        print(Fore.RED + "[-] No folder created\n")


def check_ssl():
    ssl = input(Fore.GREEN + "[?] Run against SSL? (y/n): ")
    return str(ssl)


def dict_file():
    file_location = input(
        Fore.RED + "Please add path to dictionary file (Example: /usr/share/wordlists/dirb/common.txt ")
    return str(file_location)


# System Functions

def nmap(target, folder_name):
    print(Fore.RED + "nmap -sC -sV " + target)
    if folder_name:
        os.system("sudo nmap -sC -sV -o " + folder_name + "/nmap_" + target + " " + target)
    else:
        os.system("sudo nmap -sC -sV -o " + "nmap_" + target + " " + target)


def dirb(target, folder_name, ssl):
    file_location = dict_file()
    if folder_name:
        if ssl == "y" or ssl == "Y":
            print(Fore.GREEN + "Running dirb https://" + target + " " + file_location)
            os.system("sudo dirb https://" + target + " " + file_location + "-o " + folder_name + "/dirb_" + target)
        elif ssl == "n" or ssl == "N":
            print(Fore.GREEN + "Running dirb http://" + target + " " + file_location)
            os.system("sudo dirb http://" + target + " " + file_location + "-o " + folder_name + "/dirb_" + target)
    else:
        if ssl == "y" or ssl == "Y":
            print(Fore.GREEN + "Running dirb https://" + target + " " + file_location)
            os.system("sudo dirb https://" + target + " " + file_location + "> " + "dirb_" + target)
        elif ssl == "n" or ssl == "N":
            print(Fore.GREEN + "Running dirb http://" + target + " " + file_location)
            os.system("sudo dirb http://" + target + " " + file_location)


def nikto(target, folder_name):
    if folder_name:
        print(Fore.GREEN + "Running nikto")
        os.system("sudo nikto -h " + target + " --output " + folder_name + "/nikto_" + target + ".txt")
    else:
        print(Fore.GREEN + "Running nikto")
        os.system("sudo nikto -h " + target + " --output nikto_" + target + ".txt")


# Main Function

def main():
    global inp
    while inp:
        print(
                Fore.BLUE + "______________________________________________________________________________________________")
        print(Fore.BLUE + ".___ _______    _____________________________     __________________     _____    _______ ")
        print(Fore.BLUE + "|   |\      \  /   _____/\_   _____/\_   ___ \   /   _____/\_   ___ \   /  _  \   \      \\")
        print(
                Fore.BLUE + "|   |/   |   \ \_____  \  |    __)_ /    \  \/   \_____  \ /    \  \/  /  /_\  \  /   |   \\")
        print(
                Fore.BLUE + "|   /    |    \/        \ |        \\\     \____  /        \\\     \____/    |    \/    |    \\")
        print(
                Fore.BLUE + "|___\____|__  /_______  //_______  / \______  / /_______  / \______  /\____|__  /\____|__  /")
        print(Fore.BLUE + "            \/        \/         \/         \/          \/         \/         \/         \/")
        print(
                Fore.BLUE + "*************************** CREATED BY https://invasive-security.de ***************************")
        print(
                Fore.BLUE + "_______________________________________________________________________________________________")

        # Define Target
        target = input(Fore.GREEN + "[!] Enter Target IP: ")
        ssl = check_ssl()

        folder_name = create_folder()

        print(Fore.MAGENTA + "Choose your Scan Type...")
        print(Fore.YELLOW + "=================================")
        print(Fore.YELLOW + "1. NMAP")
        print(Fore.YELLOW + "2. DIRB")
        print(Fore.YELLOW + "3. NIKTO")
        print(Fore.YELLOW + "4. Let´s run them ALL")
        print(Fore.YELLOW + "5. EXIT")
        print(Fore.YELLOW + "=================================\n")

        inp = input(Fore.GREEN + "[!] Enter the number of selection (1,2,3,4,5): ")

        if inp == "1":
            nmap(target, folder_name)
            inp = False
        elif inp == "2":
            dirb(target, folder_name, ssl)
            inp = False
        elif inp == "3":
            nikto(target, folder_name)
            inp = False
        elif inp == "4":
            nmap(target, folder_name)
            dirb(target, folder_name, ssl)
            nikto(target, folder_name)
            inp = False
        elif inp == "5":
            print("EXIT")
            exit()
        else:
            print("ERROR")
            inp = False


main()
