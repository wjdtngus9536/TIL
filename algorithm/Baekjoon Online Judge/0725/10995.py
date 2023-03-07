T = int(input())

for i in range(1,T+1):
    if i%2 == 1:
        print('* '*T)
    else:
        print(' *'*T)