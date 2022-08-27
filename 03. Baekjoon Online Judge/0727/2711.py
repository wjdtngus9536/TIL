T = int(input())
for t in range(T):
    i, s = input().split()
    i = int(i)-1    
    s = s[:i] + s[i+1:]
    print(s)