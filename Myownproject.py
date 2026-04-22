# Voice able calculator.


import win32com.client as wincl
import time

speak = wincl.Dispatch("SAPI.SpVoice")

def say(text):
    speak.Speak(text)
    time.sleep(0.3)

print("choose operators:")
print("1-Add")
print("2-Subtract")
print("3-Multiple")
print("4-Divide")
print("5-square")
print("6-cube")
print("7-squareroot")

say("Hello, I am Igris blood red, the calculator")
say("Press 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for square, 6 for cube, 7 for square root")

choice = input("Enter your operator (1/2/3/4/5/6/7): ")

#          INPUT SECTION 
if choice in ["1","2","3","4"]:
    say("Enter first number")
    a = int(input("Enter first number: "))

    say("Enter second number")
    b = int(input("Enter second number: "))

elif choice in ["5","6","7"]:
    say("Enter your number")
    N = int(input("Enter your number: "))

#           CALCULATION SECTION 
if choice == "1":
    result = a + b
    print("result",result)
    say(f"You choose addoition and your Result is,{result}")

elif choice == "2":
    result = a - b
    print("result",result)
    say(f"You choose subtraction and your Result is,{result}")

elif choice == "3":
    result = a * b
    print("result",result)
    say(f"You choose multiplication and your Result is,{result}")

elif choice == "4":
    if b != 0:
        result = a / b
        print("result",result)
        say(f"You choose division and your Result is,{result}")
    else:
        say("Error denominator cannot be zero")
        print("Error: cannot divide by zero")
        exit()

elif choice == "5":
    result = N * N
    print("result",result)
    say(f"You choose squaring and your Result is,{result}")

elif choice == "6":
    result = N * N * N
    print("result",result)
    say(f"You choose cubing and your Result is,{result}")

elif choice == "7":
    import math
    result = math.sqrt(N)
    print("result",result)
    say(f"You choose square root and your Result is,{result}")

else:
    say("Invalid choice")
    print("Invalid choice")
    exit()