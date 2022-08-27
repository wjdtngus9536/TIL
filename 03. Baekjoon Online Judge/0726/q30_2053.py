import sys
sys.stdin = open('input.txt', 'r')
try:
    score = []
    while 1:
        score.append(sum(list(map(int, input().split()))))
except:
    pass

finally:
    maxScore = max(score)
    print(score.index(maxScore)+1, maxScore)
