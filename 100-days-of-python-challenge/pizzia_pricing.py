print("Welcome to Python Pizzia Deliveries!")
size = input("What size pissia do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#Figuure out the amount they need to pay based on choices
#S = 15 / M = 20 / L = 25 / Spepperoni = +2 / M+Lpepperoni = +3 / Any extra cheese = +1

if size == "S":
    Bill = 15
if size == "M":
    Bill = 20
if size == "L":
    Bill = 25
if pepperoni == "Y":
    if size == "S":
        Bill += 2
    if size == "M":
        Bill += 3
    if size == "L":
        Bill += 3
if extra_cheese == "Y":
    Bill += 1

print(f"Your total price is ${Bill}")