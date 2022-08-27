import sys
sys.stdin = open('./20220802/input.txt')

N = int(sys.stdin.readline())
cnt = 0
names = set()

for i in range(N):
    name = sys.stdin.readline().rstrip()
    if name == 'ENTER':
        names = set()
    elif name not in names:
        names.add(name)
        cnt += 1
print(cnt)
