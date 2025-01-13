import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'x', 'z']

print('Welcome to the PyPassword Generator!')
usernumbers = int(input('How many numbers would you like? '))
usersymbols = int(input('How many symbols would you like? '))
userletters = int(input('How many letters would you like? '))

randnumbers = random.choices(numbers, k=usernumbers)
randsymbols = random.choices(symbols, k=usersymbols)
randletters = random.choices(letters, k=userletters)

for number in range(len(randnumbers)):
    totalnumbers = str(randnumbers[number])
for symbol in range(len(randsymbols)):
    totalsymbols = str(randsymbols[symbol]) 
for letter in range(len(randletters)):
    totalletters = str(randletters[letter])


password = ''.join(totalsymbols) + ''.join(totalletters) + ''.join(totalnumbers)

print(password)