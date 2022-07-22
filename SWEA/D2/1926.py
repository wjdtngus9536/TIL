N = int(input())

for i in range(1, N+1):
    if i//10 == 3 or i//10 == 6 or i//10 == 9:
        if i%10 == 3 or i%10 == 6 or i%10 == 9:
            print('--', end = ' ')
        else:
            print('-', end=' ')
    elif i%10 == 3 or i%10 == 6 or i%10 == 9:
        print('-', end=' ')
    else:
        print(i, end = ' ')
    