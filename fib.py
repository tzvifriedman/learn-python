a, b = 0,1
while a < 1000000:
    print(a, end= ',')
    a, b = b, a+b
