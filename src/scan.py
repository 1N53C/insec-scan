import os
from colorama import Fore


def nmap(target, folder_name):
    print(Fore.RED + "nmap -sC -sV " + target)
    if folder_name:
        os.system("sudo nmap -sC -sV -o " + folder_name + "/nmap_" + target + " " + target)
    else:
        os.system("sudo nmap -sC -sV -o " + "nmap_" + target + " " + target)


def dirb(target, folder_name, ssl, file_location):
    if folder_name:
        if ssl == "y" or ssl == "Y":
            print(Fore.GREEN + "Running dirb https://" + target + " " + file_location)
            os.system("sudo dirb https://" + target + " " + file_location + " -o " + folder_name + "/dirb_" + target)
        elif ssl == "n" or ssl == "N":
            print(Fore.GREEN + "Running dirb http://" + target + " " + file_location)
            os.system("sudo dirb http://" + target + " " + file_location + " -o " + folder_name + "/dirb_" + target)
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
