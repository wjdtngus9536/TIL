import sys
sys.stdin = open('./20220802/input.txt', 'r')

def check_brackets(s):
    brakets = []
    for c in s:
        if c in '([':
            brakets.append(c)
        elif c in ')]':
            if brakets:
                left = brakets.pop()
                if left == '(' and c == ')':
                    pass
                elif left == '[' and c == ']':
                    pass
                else:
                    return 'no'
            else:
                return 'no'
    else:
        if brakets:
            return 'no'
        else:
            return 'yes'

# while 1:
#     try:
#         s = sys.stdin.readline().rstrip(' \n')
#         if s == '.':    
#             raise EOFError
#         print(check_brackets(s))
#     except EOFError:
#         break   

'''
sys.stdin.readline()# 은 개행문자 \n도 함께 읽어온다는 점은 알겠다. 
# 하지만 마지막 .을 입력 받은 후 EOF를 입력받으면 except처리가 이뤄져야 하는 것 아닌가?
# 아마 input에 뭐가 더 있나보다.

s = 'fc   f\n'
print(len(s.rstrip('\n f'))) # rstrip()은 문자열 우측의 \n과 공백문자 모두를 제거한다.
'''