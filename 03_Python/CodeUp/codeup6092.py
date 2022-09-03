n = int(input())
a = map(int,input().split())

d = []
for i in range(24):
    d.append(0)

for i in a:
    d[i-1] += 1

for i in range(23):
    print(d[i], end=' ')
