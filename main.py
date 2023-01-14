
def menu():
    print("[1] Run a Motor")
    print("[2] Run a Servo motor")
    print("[3] Pin I/O")
    print("[0] Exit")

menu()
option = int(input("Enter your option: "))

while option !=0:
    if option == 1:
        print("You are about to Run the motor!")
        import motor

    elif option == 2:

        print("You are about to Run the servo motor!")
        import servo_mod

    elif option == 3:        

        print("You are about to control I/O pins!")
        import pin

    else:
        print("Invalid option!")

    print()
    menu()
    option = int(input("Enter your option: "))


