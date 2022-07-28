import sys
sys.stdin = open('input.txt', 'r')

score = 0
answer = 0
for i in range(10):
    score += int(input())
    if abs(100 - score) <= 100 - answer:
        answer = score
print(answer)
