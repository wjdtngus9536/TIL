ns = list(map(int, input().split()))
ns.sort()

total = 0
cnt = 0 

for i in range(1, len(ns)):
    total+=ns[i]
    print(ns[i])
    cnt += 1

print(total, cnt)
print(total // cnt)
