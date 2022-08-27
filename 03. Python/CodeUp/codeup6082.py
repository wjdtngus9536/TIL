n = int(input())
for i in range(1, n+1) :
    units = i % 10
    tens = i//10
    if tens == 3:
        print('X', end='')
    elif units == 3 or units == 6 or units == 9 :
        print('X', end=' ')
    else:
        print(i, end=' ')