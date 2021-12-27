'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

answer = 0

for i in range(1, 101):
    answer += (i**2) * (i-1)

print(answer)
