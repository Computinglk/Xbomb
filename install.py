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
                subprocess.run("pip install setuptools", text=True, capture_output=True, shell=True)
                print("         [+] Installing setuptools")
                
            except:
                try:
                    subprocess.run("pip3 install setuptools", text=True, capture_output=True, shell=True)
                    print("         [+] Installing setuptools")
                    
                except:
                    print("[x] Please install pip in your computer")
                    break

            try:
                subprocess.run("pip install sockets", text=True, capture_output=True, shell=True)
                print("         [+] Installing sockets")
                
            except:
                try:
                    subprocess.run("pip3 install sockets", text=True, capture_output=True, shell=True)
                    print("         [+] Installing sockets")
                    
                except:
                    print("[x] Please install pip in your computer")
                    break
            try:

                subprocess.run("pip install colored", text=True, capture_output=True, shell=True)
                print("         [+] Installing colored")
                
            except:
                try:
                    subprocess.run("pip3 install colored", text=True, capture_output=True, shell=True)
                    print("         [+] Installing colored")
                    
                except:
                    print("[x] Please install pip in your computer")
                    break

            try:

                subprocess.run("pip install python-nmap", text=True, capture_output=True, shell=True)
                print("         [+] Installing python-nmap")
                print("  ")
                print("[+] Installation completed successfully")
                print(" ")
            except:
                try:
                    subprocess.run("pip3 install python-nmap", text=True, capture_output=True, shell=True)
                    print("         [+] Installing python-nmap")
                    print(" ")
            
                    print("[+] Installation completed successfully")
                    print(" ")
                except:
                    print("[x] Please install pip in your computer")
                    break
        except:
            print("[x] Error occured when installing dependencies")


install()
