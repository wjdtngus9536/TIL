m = int(input())

if m//3==0 or m==12:
    print('winter')
elif m//3==1:
    print('spring')
elif m//3==2:
    print('summer')
else:
    print('fall')