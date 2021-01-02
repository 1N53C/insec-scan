from colorama import Fore, init
import os


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
