import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i in range(2,len(a)-2):
        if a[i] - max(a[i-2], a[i-1], a[i+1], a[i+2]) > 0:
            cnt += a[i] - max(a[i-2], a[i-1], a[i+1], a[i+2])

    print(f'#{t} {cnt}')