import hashlib
from colored import bg, fg, attr

green = fg("green")
blue = fg("blue")
red = fg("red")


def hasher():
    print(" ")
    print(blue + "-" * 88)
    print(blue + "PASSWORD HASHER")
    print(blue + "-" * 88)
    print(" ")
    print(green + "[$] Algorithm available")
    print(" ")
    print(green + "        1 -------> SHA 1")
    print(green + "        2 -------> SHA 256")
    print(green + "        3 -------> MD5")
    print(green + "        4 -------> SHA 224")
    print(green + "        5 -------> SHA 384")
    print(" ")

    def all():
        try:
            while True:
                print(" ")
                choice = str(input(green + "[#] Enter the algorithm to hash > "))

                if choice == "use 1":
                    print("")
                    print(green + "[-] SHA 1")
                    word = str(input(green + "[#] Enter the word to be hashed > "))
                    enc_wrd = word.encode("UTF-8")
                    new = hashlib.sha1(enc_wrd.strip()).hexdigest()
                    print("[x] Hash is " + str(new))

                elif choice == "use 2":
                    print("")
                    print(green + "[-] SHA 256")
                    word = str(input(green + "[#] Enter the word to be hashed > "))
                    enc_wrd = word.encode("UTF-8")
                    new = hashlib.sha256(enc_wrd.strip()).hexdigest()
                    print("[x] Hash is " + str(new))

                elif choice == "use 3":
                    print("")
                    print(green + "[-] MD5")
                    word = str(input(green + "[#] Enter the word to be hashed > "))
                    enc_wrd = word.encode("UTF-8")
                    new = hashlib.md5(enc_wrd.strip()).hexdigest()
                    print("[x] Hash is " + str(new))

                elif choice == "use 4":
                    print("")
                    print(green + "[-] SHA 224")
                    word = str(input(green + "[#] Enter the word to be hashed > "))
                    enc_wrd = word.encode("UTF-8")
                    new = hashlib.sha224(enc_wrd.strip()).hexdigest()
                    print("[x] Hash is " + str(new))

                elif choice == "use 5":
                    print("")
                    print(green + "[-] SHA 384")
                    word = str(input(green + "[#] Enter the word to be hashed > "))
                    enc_wrd = word.encode("UTF-8")
                    new = hashlib.sha384(enc_wrd.strip()).hexdigest()
                    print("[x] Hash is " + str(new))
                elif choice == "back":
                    break
                else:
                    print(red + "[+] Wrong choice. (Type 'use <number>' to choose the option")
        except:
            print(red + "[+] 'hashlib' is not installed")
    all()



