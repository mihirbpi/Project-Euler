'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

two_prev = 0
one_prev = 1
sum = 0
F = 0

while (F < 4e6):

    if (F % 2 == 0):
        sum += F

    F = two_prev + one_prev
    two_prev = one_prev
    one_prev = F

print(sum)