A = list(map(int, input().split()))
B = list(map(int, input().split()))

a, b, win = 0, 0, 'D'
for i in range(10):
    if A[i] > B[i]:
        a += 3
        win = 'A'
    elif B[i] > A[i]:
        b += 3
        win = 'B'
    elif A[i] == B[i]:
        a += 1
        b += 1

print(a, b)
if a == b:
    print(win)
else:
    print('A' if a > b else 'B')