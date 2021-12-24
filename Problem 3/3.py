'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

def is_prime(number):

    if(number == 2):
        return True

    else:

        for i in range(2, 1+int(math.sqrt(number))):

            if(number % i == 0):
                return False
        return True


for number in range(1, 600851475143 + 1):

    quotient, remainder = divmod(600851475143, number)

    if(remainder == 0):

        if(is_prime(quotient)):
            print(quotient)
            break
