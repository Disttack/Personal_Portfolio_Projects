import random

random_int = random.randint(a=0,b=2)
choice = input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors: ")

if choice == "0":
    print('''Your choice is: \n
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          ''')
elif choice == "1":
    print('''Your choice is: \n
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
          ''')
elif choice == "2":
    print('''Your choice is: \n
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          ''')
else:
    print("Please choose a valid number.")