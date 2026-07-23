#check greater than
x = 10
if x > 5:
    print("Big")
print("Done")
#odd or even
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#grade evaluation
marks = 85
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("D")
#multiple ifs
x = 15
if x > 10:
    print("A")
if x > 5:
    print("B")
if x > 0:
    print("C")
#logical operators
x = 10
y = 20
if x > 5 and y > 15:
    print("Both")
elif x > 5 or y > 15:
    print("At least one")
else:
    print("Neither")
#truthy or falsy
# if 0: print("A")
# if "": print("B")
# if None: print("C")
# if "hello": print("D")
# if 1: print("E")
if 0:
    print("A")   # Won't run (0 is falsy)

if "":
    print("B")   # Won't run (empty string is falsy)

if None:
    print("C")   # Won't run (None is falsy)

hello = "world"  # Define the variable
if hello:
    print("D")   # Will run (non-empty string is truthy)

if 1:
    print("E")   # Will run (1 is truthy)

#nested if
x = 5
if x > 3:
    if x > 7:
        print("A")
    else:
        print("B")
else:
    if x > 1:
        print("C")
    else:
        print("D")
#complex conditions
a = 10
b = 20
c = 30
if a > b:
    print("X")
elif b > c:
    print("Y")
elif a + b > c:
    print("Z")
else:
    print("W")
#boolean conversions
if "False": print("A")
if bool(""): print("B")
if bool(0): print("C")
if bool("0"): print("D")
#REAL USE CASES
#DISCOUNT LOGIC
cart_total = 1200
if cart_total > 1000:
    print("Apply 10% discount")
else:
    print("No discount")
#LOGIN CHECK
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Access granted")
else:
    print("Access denied")
#TRAFFIC SYSTEMS
#SIGNAL CONTROL
light = "red"
if light == "green":
    print("Go")
elif light == "yellow":
    print("Slow down")
else:
    print("Stop")
#EMAIL FILTERING - SPAM DETECTION
subject = "Win money now!"
if "win" in subject.lower() or "money" in subject.lower():
    print("Mark as spam")
else:
    print("Inbox")
#BANKING-ATM WITHDRWAL
balance = 500
withdraw = 600
if withdraw <= balance:
    print("Transaction successful")
else:
    print("Insufficient funds")
#GAMING-PLAYER HEALTH CHECK
health = 0
if health > 0:
    print("Player alive")
else:
    print("Game over")
#fizzbuzz program in python
# FizzBuzz program in Python

for i in range(1, 31):   # loop from 1 to 30
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
#prime check in python
# Prime number check from 1 to 50

for num in range(1, 51):   # loop through numbers 1 to 50
    if num > 1:            # prime numbers are greater than 1
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not prime")
                break
        else:
            print(num, "is prime")
    else:
        print(num, "is not prime")
#break condition
# Break loop when number reaches 13

for num in range(1, 21):   # loop from 1 to 20
    if num == 13:
        print("Loop stopped at", num)
        break
    print(num)
#continue condition
# Skip printing number 7 in the loop

for num in range(1, 16):   # loop from 1 to 15
    if num == 7:
        continue           # skip the rest of the loop for this iteration
    print(num)




