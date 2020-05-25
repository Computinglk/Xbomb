import socket
import time


def port_manual():
    ip = input("Enter the ip address: ")
    port = input("Enter the port: ")

    s = socket.socket()
    s.settimeout(5)
    result = s.connect_ex((ip, int(port)))

    if result == 0:
        print("Port " + port + " is open")
        time.sleep(2)
    elif result != "0":
        print("Port " + port + " is closed")
        time.sleep(2)


def port_range():
    ip = input("Enter the ip address: ")
    print("Enter the port range")
    a = input("from > ")
    b = input("to > ")
    s = socket.socket()
    for port in range(int(a), int(b)):
        result = s.connect_ex((ip, port))
        if result == 0:
            print("Port " + str(port) + " is open")
        else:
            print("Port " + str(port) + " is closed")

    time.sleep(3)


def auto_scan():
    ip = input("Enter the ip address: ")
    ports = [21, 22, 80, 135, 139, 443, 445]

    s = socket.socket()
    for port in ports:
        result = s.connect_ex((ip, port))
        if result == 0:
            print("Port " + str(port) + " is open")
        else:
            print("Port " + str(port) + " is closed")

    time.sleep(3)


print("*" * 72)
print("PortScanner")
print("*" * 72)

while True:
    print("          1-----> Normal Port scan")
    print("          2-----> Range Port scan")
    print("          3-----> Auto Port scan")
    print(" ")
    answer = str(input("Enter type of scanning : "))
    print(" ")
    if answer == "1":
        port_manual()
        time.sleep(3)
    elif answer == "2":
        port_range()
        time.sleep(5)
    elif answer == "3":
        auto_scan()
        time.sleep(5)
    elif answer == "quit":
        quit()
        break
    else:
        print("Wrong choice")
        time.sleep(3)
