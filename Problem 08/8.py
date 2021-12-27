import numpy as np

input =  list(map(int, list("".join(open("input.txt").read().split("\n")))))
highest_prod = 1

for i in range(0, len(input) - 13):
    prod_adjacent_digits = np.prod(input[i:i+13])

    if(prod_adjacent_digits > highest_prod):
        highest_prod = prod_adjacent_digits

print(highest_prod)
