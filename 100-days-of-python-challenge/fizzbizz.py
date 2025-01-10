# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Bizz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBizz"

numbers = list(range(1, 101))

for number in numbers:
    print(number)
    if number % 5 == 0 and number % 3 == 0:
        print('fizzbizz')
    elif number % 5 ==0:
        print('Bizz')
    elif number % 3 == 0:
        print('Fizz')
    else:
        print(number)



