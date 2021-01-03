#!/usr/bin/python3

import helper as h
import scan as scan
import banner as banner
import menu as menu
import threading
from colorama import Fore, init

init(autoreset=True)

# Globals
target = ""
inp = True


# Main Function
def main():
    # type: () -> object
    global inp
    while inp:

        # Display Banner
        banner.banner()

        # Define Target
        target = input(Fore.GREEN + "[!] Enter Target IP: ")

        # Call Helper and Menu Functions
        file_location = h.dict_file()
        ssl = h.check_ssl()
        folder_name = h.create_folder()
        inp = menu.display_menu()

        print("Chosen Selection: " + inp)
        if inp == "1":
            scan.nmap(target, folder_name)
            inp = False
        elif inp == "2":
            scan.dirb(target, folder_name, ssl, file_location)
            inp = False
        elif inp == "3":
            scan.nikto(target, folder_name)
            inp = False
        elif inp == "4":
            t1 = threading.Thread(target=scan.nmap, args=(target, folder_name))
            t1.start()
            t2 = threading.Thread(target=scan.dirb, args=[target, folder_name, ssl, file_location])
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
