# 한수 counting
N = int(input())
if N < 100: # 2자리수 이하는 모두 한수
    print(N)
else:       # 3자리수의 경우
    cnt = 99
    for i in range(100,N+1):
        nlist = list(map(int, str(i)))
        if nlist[0] - nlist[1] == nlist[1] - nlist[2]:
            cnt += 1
    print(cnt)
