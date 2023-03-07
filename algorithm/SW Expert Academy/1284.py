# 수도 요금 경쟁
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for i in range(1, T+1):
    res = 0
    P,Q,R,S,W = map(int,input().split())
    if W > R:
        res = Q + (W-R)*S   if Q+(W-R)*S<P*W else P * W
    else :
        res = Q             if Q < P * W     else P * W
    print('#%d %d'%(i, res))
