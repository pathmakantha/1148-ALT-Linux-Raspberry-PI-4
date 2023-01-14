import RPi.GPIO as GPIO
import random
import time

GPIO.cleanup()

pins = [23,24,25,22,12,16,20,21,13]

GPIO.setmode(GPIO.BCM)  # use GPIO numbering, not generic
GPIO.setwarnings(False)

# setup all pins based on above configuration
for pin in pins:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

def menu2():
    print("[1] Turn On All")
    print("[2] Turn Off All")
    print("[3] Turn On Specific Pin")
    print("[4] Turn Off Specific Pin")
    print("[0] Exit")

menu2()
option = int(input("Enter your option: "))


while option !=0:
    if option == 1:
        print("All on")
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH)

    elif option == 2:
        print("All off")
        for pin in pins:
            GPIO.output(pin, GPIO.LOW)

    elif option == 3:
        pin_num = int(input("Enter GPIO port : "))
        print("pin on")
        GPIO.output(pin_num, GPIO.HIGH)

    elif option == 4:
        pin_num = int(input("Enter GPIO port : "))
        print("pin on")
        GPIO.output(pin_num, GPIO.LOW)
    else:
        print("Invalid option!")

    print()
    menu2()
    option = int(input("Enter your option: "))
