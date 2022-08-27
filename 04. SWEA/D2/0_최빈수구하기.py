import sys

sys.stdin = open("_최빈수구하기.txt")

# 최빈수가 여러개일 경우 가장 큰 값 출력
T = int(input())
for i in range(1):
    input()
    scores = map(int, input().split())
    numbers = {}
    for j in scores:
        if numbers.get(j):
            numbers[j] += 1
        else:
            numbers[j] = 1
    print(f'#{i+1}',sorted(numbers.items(), key=lambda x:(-x[1], -x[0]))[0][0])
    # 람다 함수를 이용하여 우선순위를 정한다 1st. 빈도수(value) = -x[1] 2nd. 숫자 크기(key) = -x[0] <둘 다 내림차순 정렬>