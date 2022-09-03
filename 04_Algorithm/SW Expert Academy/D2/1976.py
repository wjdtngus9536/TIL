import sys
sys.stdin = open('input1976.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    t1, m1, t2, m2 = map(int, input().split())
    t = t1 + t2
    m = m1 + m2
    if t > 12:
        t -=12
    if m > 60:
        t += 1
        m -=60
    print('#%d %d %d'%(test_case, t, m))