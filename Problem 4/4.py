'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


best = 0

for n1 in range(100, 1000):

    for n2 in range(100, 1000):
        result = n1 * n2

        if(result >= 100000):

            a = result // 100000
            b = (result - 100000*a) // 10000
            c = (result - 100000*a - 10000*b) // 1000

            if(result == 100000*a + 10000*b + 1000*c + 100*c + 10*b + a and result >= best):
                best = result
print(best)
