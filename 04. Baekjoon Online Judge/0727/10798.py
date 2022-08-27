import sys
sys.stdin = open('input.txt', 'r')

array2d = [[0]*15 for i in range(5)] 
for i in range(5):
    a = list(input())
    a_len = len(a)
    for j in range(a_len):
        array2d[i][j] = a[j]

for i in range(15):
    for j in range(5):
        if array2d[j][i] == 0:
            continue
        print(array2d[j][i], end='')