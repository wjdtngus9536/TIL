# Case #1: 1 + 1 = 2
T=int(input())
for i in range(T):
    a,b=map(int, input().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')
