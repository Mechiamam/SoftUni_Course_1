number = int(input())
number_is_prime = False
if number > 1:
    for i in range(2, int(number/2)+1):
        if (number % i) == 0:
            number_is_prime = False
            print(number_is_prime)
            break
    else:
        number_is_prime = True
        print(number_is_prime)
else:
    number_is_prime = False
    print(number_is_prime)