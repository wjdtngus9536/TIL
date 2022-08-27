import sys
sys.stdin = open('input1989.txt', 'r')

def isPalindrome(s):
    i=len(s)
    if i%2 == 1:
        if(s[0:i//2] == s[i-1:i//2:-1]):
            return 1
        else:
            return 0
        return 1
    else:
        if(s[0:i//2] == s[i-1:i//2-1:-1]):
            return 1
        else:
            return 0
        return 1
        


T = int(input())
for test_case in range(1, T + 1):
    s = input()
    print('#%d %d'%(test_case, isPalindrome(s)))


    