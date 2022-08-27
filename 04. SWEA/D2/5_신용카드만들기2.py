import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
for t in range(T):
    card = input()
    cnt = 0
    if card[0] not in '34569':          # 해당 번호로 시작하지 않는 경우 0 출렬
        print(f'#{t+1}', 0)
    else:                               # 34569로 시작하는 경우 중 다시 screening
        cnt = 0
        for i in card:
            if i == '-':                # -를 제외한 숫자를 counting input의 제약조건이 주어지지 않았다면 isdigit도 사용
                continue
            cnt += 1
        if cnt == 16:
            print(f'#{t+1}', 1)
        else:
            print(f'#{t+1}', 0)
