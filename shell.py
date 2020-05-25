import subprocess
import os
from colored import fg

green = fg("green")
red = fg("red")
blue = fg("blue")


def shell():
    print(" ")
    while True:
        command = str(input(green + "shell > "))
        if len(command) > 0:
            run = subprocess.run(command, shell=True, capture_output=True, text=True)
            answer = run.stdout
            error = run.returncode
            if command[:2] == "cd" and len(command) > 2:
                try:
                    os.chdir(command[3:])
                    new_path = os.getcwd()
                    print(new_path)
                    print(" ")

                except OSError:
                    print(red + "The system can't find the path specified")
                    print(" ")
            elif error != 0:
                print(red + run.stderr)
            elif command == "exit":
                break
            else:
                print(answer)
