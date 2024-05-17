#This is definatly not a normal program
#But hey! Who cares!
import time as t
a = input("Would you like to execute the script? [y/n]:")
def script():
    while True:
        try:
            i = 10
            while i == 10:
                print("HAHA!!!I WILL RUN FOREVER!!!")
        except KeyboardInterrupt:
            print("Grrr... I did not run forever.")
            break
if a == "y":
    print("Here you go!")
    t.sleep(1)
    script()
elif a == "n":
    print("Well too bad! Here you go!")
    t.sleep(1)
    script()
else:
    print("I'll take it as yes. Here you go!")
    t.sleep(1)
    script()
