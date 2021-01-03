from colorama import Fore

def display_menu():
    print(Fore.MAGENTA + "Choose your Scan Type...")
    print(Fore.YELLOW + "=================================")
    print(Fore.YELLOW + "1. NMAP")
    print(Fore.YELLOW + "2. DIRB")
    print(Fore.YELLOW + "3. NIKTO")
    print(Fore.YELLOW + "4. Let´s run them ALL")
    print(Fore.YELLOW + "5. EXIT")
    print(Fore.YELLOW + "=================================\n")

    return input(Fore.GREEN + "[!] Enter the number of selection (1,2,3,4,5): ")

