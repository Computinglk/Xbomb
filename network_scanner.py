import nmap
import time
from colored import bg, fg, attr

green = fg("green")
blue = fg("blue")
red = fg("red")
ns = nmap.PortScanner()


def single_host():
    try:
        print(" ")
        print(green + "[-] Single host scan")
        ip = str(input(green + "[#] Enter the ip address of the host: "))
        port = str(input("[#] Enter the port range: "))
        ns.scan(ip, port, "-v")
        print(ns.csv())
    except:
        print(red + "[-] Invalid inputs.....")


def host_state():
    try:
        print(" ")
        print(green + "[-] Host state scan")
        ip = str(input(green + "[#] Enter the ip address of the host: "))
        ns.scan(ip)
        print(ns[ip].state())
    except:
        print(red + "[-] Invalid inputs.....")


def port_state():
    try:
        print(" ")
        print(green + "[-] Port state scan")
        ip = str(input(green + "[#] Enter the ip address of the host: "))
        port_range = str(input("[#] Enter the port range: "))
        port = int(input("[#] Enter the port: "))
        ns.scan(ip, port_range, "-v --version-all")
        c = ns[ip].has_tcp(port)
        print(c)

    except:
        print(red + "[-] Invalid inputs.....")


def protocol():
    try:
        print(" ")
        print(green + "[-] Protocol scan")
        ip = str(input(green + "[#] Enter the ip address of the host: "))
        port_range = str(input("[#] Enter the port range: "))
        ns.scan(ip, port_range, "-v --version-all")
        print(ns[ip].all_protocols())
    except:
        print(red + "[-] Invalid input")


def port():
    try:
        print(" ")
        print(green + "[-] Open port scan")
        ip = str(input(green + "[#] Enter the ip address of the host: "))
        port_range = str(input("[#] Enter the port range: "))
        ns.scan(ip, port_range, "-v --version-all")
        print(ns[ip]["tcp"].keys())
    except:
        print(red + "[-] Invalid input")


def soft():
    try:
        print(" ")
        print(green + "[-] Soft scan")
        ip = str(input(green + "[#] Enter the ip address or the range of the ip's: "))
        port_range = str(input("[#] Enter the port range: "))
        ns.scan(ip, port_range, "-v --version-all")
        print(ns.scaninfo())
        print(ns.csv())

        a = ns.scanstats()["timestr"]
        b = ns.scanstats()["elapsed"]

        print("Scan started " + str(a))
        print("Time took for the scan " + str(b) + " seconds")
    except:
        print(red + "[-] Invalid input")


def a():
    try:
        print(" ")
        print(green + "[-] Single host aggressive scan")
        ip = str(input(green + "[#] Enter the ip address of the host: "))
        port_range = str(input("[#] Enter the port range: "))

        ns.scan(ip, port_range, "-v --version-all")
        print(ns.scaninfo())
        print(ns.csv())

        a = ns.scanstats()["timestr"]
        b = ns.scanstats()["elapsed"]
        c = ns.scanstats()["totalhosts"]
        d = ns.scanstats()["uphosts"]

        print("> State :")
        print(ns[ip].state())
        print("> Protocol :")
        print(ns[ip].all_protocols())
        print("> Open ports :")
        print(ns[ip]["tcp"].keys())

        print(" ")
        print("> Scan started " + str(a))
        print("> Time took for the scan " + str(b) + " seconds")
        print("> Total hosts scanned " + str(c))
        print("> Active hosts " + str(d))
        print(" ")

    except:
        print(red + "[-] Wrong input")


def b():
    try:
        print(" ")
        print(green + "[-] One time multiple host aggressive scan")
        print(
            green + "RANGE FORMAT - from > 127.0.0.1 \n                to > 127.0.0.20 \n                as 127.0.0.1-20")
        ip = str(input("[#] Enter the ip address of the host ccording to the \nabove format: "))
        port_range = str(input('[#] Enter the port range: '))

        ns.scan(ip, port_range, "-v --version-all")
        print(ns.scaninfo())
        print(ns.csv())

        a = ns.scanstats()["timestr"]
        b = ns.scanstats()["elapsed"]
        c = ns.scanstats()["totalhosts"]
        d = ns.scanstats()["uphosts"]

        print(" ")
        print("> Scan started " + str(a))
        print("> Time took for the scan " + str(b) + " seconds")
        print("> Total hosts scanned " + str(c))
        print("> Active hosts " + str(d))
        print(" ")
    except:
        print(red + "[-] Wrong input")


def c():
    try:
        print(" ")
        print(green + "[-] Multiple time multiple host aggressive scan")
        a = int(input(green + "[#] Enter the number of ip addresses you want to scan: "))
        for _ in range(a):
            ip = str(input("[#] Enter the ip address of the host: "))
            port_range = str(input('[#] Enter the port range: '))

            ns.scan(ip, port_range, "-v --version-all")
            print(ns.scaninfo())
            print(ns.csv())

            a = ns.scanstats()["timestr"]
            b = ns.scanstats()["elapsed"]
            c = ns.scanstats()["totalhosts"]
            d = ns.scanstats()["uphosts"]

            print("> State :")
            print(ns[ip].state())
            print("> Protocol :")
            print(ns[ip].all_protocols())
            print("> Open ports :")
            print(ns[ip]["tcp"].keys())

            print(" ")
            print("> Scan started " + str(a))
            print("> Time took for the scan " + str(b) + " seconds")
            print("> Total hosts scanned " + str(c))
            print("> Active hosts " + str(d))
            print(" ")
    except:
        print(red + "[-] Wrong output")


def main():
    passwd = True
    if passwd == True:
        print(" ")
        print(blue + "-" * 80)
        print("NETWORK SCANNER")
        print("-" * 80)

        print(green + "[$] Main menu")
        print("")
        print("        1 ----------> Single host scan")
        print("        2 ----------> Host state scan")
        print("        3 ----------> Port state scan")
        print("        4 ----------> Protocol scan")
        print("        5 ----------> Open port scan")
        print("        6 ----------> Soft scan")
        print("        7 ----------> Aggressive scans")

        while True:

            print(" ")
            answer = str(input(green + "[#] Enter the type of scan you want > "))
            if answer == "use 1":
                single_host()
            elif answer == "use 2":
                host_state()
            elif answer == "use 3":
                port_state()
            elif answer == "use 4":
                protocol()
            elif answer == "use 5":
                port()
            elif answer == "use 6":
                soft()
            elif answer == "use 7":
                while True:
                    print(' ')
                    print(green + '[A] Aggressive scans ')
                    print('  ')
                    print('       1 ------> Single host aggressive scan ')
                    print('       2 ------> One time multiple host aggressive scan')
                    print('       3 ------> Multiple time multiple host aggressive scan')
                    print(' ')
                    ans = str(input(green + "[#] Enter the type of aggressive scan you want > "))
                    if ans == "use 1":
                        a()
                        time.sleep(3)
                    elif ans == "use 2":
                        b()
                        time.sleep(3)
                    elif ans == "use 3":
                        c()
                        time.sleep(3)
                    elif ans == "back":
                        break
                    else:
                        print(red + "Wrong choice. (Type 'use <number>' to choose the option")
            elif answer == "back":
                break
            else:
                print(red + "[x] Wrong choice. (Type 'use <number>' to choose the option")
    else:
        print(red + "[x] Wrong choice")
