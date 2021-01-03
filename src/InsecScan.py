#!/usr/bin/python3

import helper as h
import start as start
import banner as banner
import menu as menu
from colorama import Fore, init

init(autoreset=True)

# Main Function
def main():
    # type: () -> object

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
    start.start_scan(file_location, folder_name, ssl, target, inp)

main()
