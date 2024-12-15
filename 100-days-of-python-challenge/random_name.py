import random
friends = ["Alice", "Bob", "Charlie", "David", "Emmanual"]
random_int = random.randint(a=1,b=5)
if random_int == 1:
    print(friends[0])
elif random_int == 2:
    print(friends[1])
elif random_int == 3:
    print(friends[2])
elif random_int == 4:
    print(friends[3])
else:
    print(friends[4])