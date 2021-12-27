
for m in range(1, 1000):

    for n in range(1, 1000):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2

        if(a>0 and b>0 and c>0):

            if(a+b+c == 1000):
                print(a*b*c)
