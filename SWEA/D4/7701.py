import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    names = [input() for _ in range(N)]
    
    names = list(set(names))
    names.sort()
    names = sorted(names, key = len)
    print('#%d'%t)
    for i in names:
        print(i)


