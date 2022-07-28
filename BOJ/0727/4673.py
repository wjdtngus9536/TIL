def d(n):
    for i in range(max(n - 9 * len(str(n)), 0), n):
        if n == i + sum(list(map(int, str(i)))):
            return 0
    else:
        return 1
    
for i in range(1, 10000):
    if d(i):
        print(i)