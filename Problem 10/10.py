import math

def is_prime(number):

    if(number == 2):
        return True

    else:

        for i in range(2, 1+int(math.sqrt(number))):

            if(number % i == 0):
                return False
        return True


sum = 0

for i in range(2, int(2e6)):

    if(is_prime(i)):
        sum += i

print(sum)
