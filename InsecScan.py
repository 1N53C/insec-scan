#!/usr/bin/python3

import helper as h
import scan as scan
import banner as banner
import threading
from colorama import Fore, init

init(autoreset=True)

# Globals
target = ""
inp = True


# Main Function
def main():
    global inp
    while inp:
        banner.banner()
        # Define Target
        target = input(Fore.GREEN + "[!] Enter Target IP: ")
        ssl = h.check_ssl()

        folder_name = h.create_folder()

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
            scan.nmap(target, folder_name)
            inp = False
        elif inp == "2":
            scan.dirb(target, folder_name, ssl)
            inp = False
        elif inp == "3":
            scan.nikto(target, folder_name)
            inp = False
        elif inp == "4":
            t1 = threading.Thread(target=scan.nmap, args=(target, folder_name))
            t1.start()
            t2 = threading.Thread(target=scan.dirb, args=(target, folder_name, ssl))
            t2.start()
            t3 = threading.Thread(target=scan.nikto, args=(target, folder_name))
            t3.start()
            inp = False
        elif inp == "5":
            print("EXIT")
            exit()
        else:
            print("ERROR")
            inp = False


main()
