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


for number in range(2, 600851475143 + 1):

    if(600851475143 % number == 0):

        to_check = int(600851475143/number)

        if(is_prime(to_check)):
            print(to_check)
            break
