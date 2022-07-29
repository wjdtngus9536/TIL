import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for i in range(T):
    num = list(map(int, input().split()))
    res = 0
    for j in range(1, 16):
        if j % 2 == 1:
            res += 2 * num[j-1]             # index는 0부터 시작하기에 -1씩 처리해 주었음
        else:
            res += num[j-1]
    print(f'#{i+1}', abs(res%10-10)%10)     # 마지막 숫자를 합해서 10을 나눴을 때 나머지가 0이 되는 숫자는
                                            # 더한 수에 한자리수만 남긴 후 -10을 뺀 절대값인데 10이 나올 수 있으므로 한번 더 mod연산
