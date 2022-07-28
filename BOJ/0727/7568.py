import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
people = []
for i in range(1, T+1):
    people.append(list(map(int, input().split())))

for i in range(T):
    rank = 1
    if i == 3:
        pass
    for j in range(T):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    print(rank, end = ' ')