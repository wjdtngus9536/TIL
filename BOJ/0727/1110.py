N = int(input())
cnt=0
newN = N
while 1:
    cnt+=1
    n1 = newN//10
    n2 = newN%10
    newN = n2*10 + (n1+n2)%10
    if N == newN:
        print(cnt)
        break