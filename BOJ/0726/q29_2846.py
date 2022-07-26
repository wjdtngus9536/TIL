N = int(input())
hill = list(map(int, input().split()))
gap = 0
maxGap = 0
for i in range(1,N):
    if hill[i] <= hill[i-1]: # 내리막 or 평지인 경우
        gap = 0
    else:                   # 오르막인 경우
        gap += hill[i] - hill[i-1]
        if maxGap < gap:
            maxGap = gap

print(maxGap)


