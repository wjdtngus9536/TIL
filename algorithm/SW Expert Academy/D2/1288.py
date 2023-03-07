import sys
sys.stdin = open('input1288.txt', 'r')

def count(ht:list, N: int):
    for i in str(N):    ht[int(i)] = 1

def check(ht):
    for i in range(10):    
        if ht[i] == 0:    
            return 1

T = int(input())
for i in range(1, T+1):
    N = int(input())
    flag = [0]*10
    cnt = 1
    while 1:
        if N == 2:
            pass
        count(flag, N*cnt)
        if check(flag):
            cnt+=1
        else :
            break    
    print('#{} {}'.format(i, cnt*N))