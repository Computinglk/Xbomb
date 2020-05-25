import subprocess
import time

time.sleep(1)

print("[I] Installing dependencies....")
print(" ")
time.sleep(2)

installing = True


def install():
    for _ in range(0, 1):
        try:
            try:
                print("         [+] Installing setuptools")
                subprocess.run("pip install setuptools", text=True, capture_output=True, shell=True)
            except:
                try:
                    print("         [+] Installing setuptools")
                    subprocess.run("pip3 install setuptools", text=True, capture_output=True, shell=True)
                except:
                    print("[x] Please install pip in your computer")
                    break

            try:
                print("         [+] Installing socket")
                subprocess.run("pip install socket", text=True, capture_output=True, shell=True)
            except:
                try:
                    print("         [+] Installing socket")
                    subprocess.run("pip3 install socket", text=True, capture_output=True, shell=True)
                except:
                    print("[x] Please install pip in your computer")
                    break
            try:

                print("         [+] Installing colored")
                subprocess.run("pip install colored", text=True, capture_output=True, shell=True)
            except:
                try:
                    print("         [+] Installing colored")
                    subprocess.run("pip3 install colored", text=True, capture_output=True, shell=True)
                except:
                    print("[x] Please install pip in your computer")
                    break

            try:

                print("         [+] Installing python-nmap")
                subprocess.run("pip install python-nmap", text=True, capture_output=True, shell=True)
                from colored import fg
                blue = fg("blue")
                print(" ")
                print(blue + "[+] Installation completed successfully")
                print(" ")
            except:
                try:
                    print("         [+] Installing python-nmap")
                    subprocess.run("pip3 install python-nmap", text=True, capture_output=True, shell=True)
                    print(" ")
                    from colored import fg
                    blue = fg("blue")
                    print(blue + "[+] Installation completed successfully")
                    print(" ")
                except:
                    print("[x] Please install pip in your computer")
                    break
        except:
            print("[x] Error occured when installing dependencies")


install()
