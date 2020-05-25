import listener
import gmail_bruteforcer
import hasher
import instructions
import wifi_stealer
import payload_maker
from colored import fg
import shell

green = fg("green")
blue = fg("blue")
red = fg("red")

print(blue + "                                                                                   ")
print(" $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $         ")
print(" $   ------------------------------------------------------------------------------    $         ")
print(" $  |  X         X    B B B B B       O O O O O     M         M    B B B B B       |   $         ")
print(" $  |    X     X     B         B    O           O   M  M   M  M   B         B      |   $         ")
print(" $  |       X        B B B B B B    O           O   M    M    M   B B B B B B      |   $         ")
print(" $  |    X     X     B           B  O           O   M         M   B           B    |   $         ")
print(" $  |  X         X   B B B B B B B    O O O O O     M         M   B B B B B B B    |   $         ")
print(" $  |                                                                              |   $         ")
print(" $   ------------------------------------------------------------------------------    $         ")
print(" $ $ $ $ $ $                   Your ignorance is my Power              $ $ $ $ $ $ $ $ $         ")
print(red + "             $   -----------------------------------------------------   $                 ")
print("             $  |              [+] Xbomb version 2.0                  |  $                       ")
print("             $  |            [+] Product of Computing lk              |  $                       ")
print("             $  |          [+] Author - Kavishka Gihan Fernando       |  $                       ")
print("             $  |        [+] Follow me on instagram - @_kavi.gihan    |  $                       ")
print("             $   -----------------------------------------------------   $                       ")
print("              $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $                      ")

while True:
    print(" ")
    enter = str(input(blue + "Xbomb > "))

    if enter == "list":
        print(green + "[X] Xbomb shell option list")
        print(" ")
        print("   1 ---> Password Hasher")
        print("   2 ---> Gmail Brute Forcer")
        print("   3 ---> WiFi Stealer (WINDOWS)")
        print("   4 ---> Crete a listener")
        print("   5 ---> Crete a payload")
        print(" ")
    elif enter == "help":
        instructions.help()
    elif enter == "credits":
        instructions.credit()
    elif enter == "shell":
        shell.shell()
    elif enter == "use 1":
        hasher.hasher()
    elif enter == "use 2":
        gmail_bruteforcer.gmail()
    elif enter == "use 3":
        wifi_stealer.wifi_stealer()
    elif enter == "use 4":
        listener.listener()
    elif enter == "use 5":
        payload_maker.payload_maker()
    elif enter == "info 1":
        instructions.info_1()
    elif enter == "info 2":
        instructions.info_3()
    elif enter == "info 3":
        instructions.info_4()
    elif enter == "info 4":
        instructions.info_5()
    elif enter == "info 5":
        instructions.info_6()
    elif enter == "exit":
        instructions.exit()
        break
    else:
        print(red + "[x] Wrong input (Use 'help' command to see all the options available)")
