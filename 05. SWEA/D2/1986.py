# 지그재그 숫자
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(1, T+1):
    N = int(input())
    res = 0
    for j in range(1, N+1):
        if j%2 == 1:
            res+=j
        else:
            res-=j
    print('#%d %d'%(i, res))