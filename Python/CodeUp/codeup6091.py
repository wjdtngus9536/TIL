m,n,k=map(int, input().split())
d=1
while not(d%m==0 and d%n==0 and d%k==0):
    d += 1
print(d)