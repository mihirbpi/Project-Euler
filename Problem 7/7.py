'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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

num_primes = 0
i = 2

while(num_primes < 10001):

    if(is_prime(i)):
        last_prime = i
        num_primes += 1

    i += 1

print(last_prime)
