import threading
import scan


def start_scan(file_location, folder_name, ssl, target, inp):
    if inp == "1":
        scan.nmap(target, folder_name)
    elif inp == "2":
        scan.dirb(target, folder_name, ssl, file_location)
    elif inp == "3":
        scan.nikto(target, folder_name)
    elif inp == "4":
        t1 = threading.Thread(target=scan.nmap, args=(target, folder_name))
        t1.start()
        t2 = threading.Thread(target=scan.dirb, args=[target, folder_name, ssl, file_location])
        t2.start()
        t3 = threading.Thread(target=scan.nikto, args=(target, folder_name))
        t3.start()
    elif inp == "5":
        print("EXIT")
        exit()
    else:
        print("ERROR")

