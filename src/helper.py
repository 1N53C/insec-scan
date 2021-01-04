from colorama import Fore, init
import os

# Create a Folder to safe the output files
def create_folder():
    folder_create = input(Fore.GREEN + "[?] Create a folder to save the output? (y/n) [n] ")
    if folder_create == "y" or folder_create == "Y":
        folder_name = input(Fore.GREEN + "[!] Enter the name of the folder and I will create it for you: ")
        os.system("sudo mkdir " + folder_name)
        print(Fore.GREEN + "[+] Folder with the name '" + folder_name + "' created!\n")
        return str(folder_name)
    else:
        print(Fore.RED + "[-] No folder created\n")

# Check if we have to run the scans against SSL
def check_ssl():
    ssl = input(Fore.GREEN + "[?] Run against SSL? (y/n) [n]: ")
    return str(ssl)

# Specify the path to the dirb dictionary file
def dict_file():
    location = input(Fore.GREEN + "[!] Specify path to dictionary file or hit Enter for default: [/usr/share/wordlists/dirb/common.txt] ")
    if location:
        file_location = location
    else:
        file_location = "/usr/share/wordlists/dirb/common.txt"
    return str(file_location)
